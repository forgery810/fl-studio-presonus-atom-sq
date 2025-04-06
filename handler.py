import modes
import data
from action import Action, EncoderAction
from notes import Notes
from modes import StepSequencerMode, StepSequencerSubmode
import modes
from direction import Directions
from enum import Enum
import ui
from pads import PadHandler
from midi_mapping import controller
import config
import config_layout
import channels
import patterns
import mixer
import plugins
import plugindata  
import device

class MidiId(Enum):
    PRESSURE = 208
    NOTE_ON = 144
    NOTE_OFF = 128
    PITCH_BEND = 224
    CONTROL_CHANGE = 176

class EventType(Enum):
    DIRECTION = 1
    BUTTON = 2
    KNOB = 3
    OTHER = 4

class MidiHandler:
    def __init__(self, event, cc_data, mode_manager, action, lights_instance, encoder_action, state):

        self.event = event
        self.mode_manager = mode_manager
        self.event_handlers = {
            MidiId.PRESSURE: self.handle_pressure,
            MidiId.NOTE_ON: self.handle_note_on,
            MidiId.NOTE_OFF: self.handle_note_on,
            MidiId.PITCH_BEND: self.handle_pitch_bend,
            MidiId.CONTROL_CHANGE: self.handle_control_change,
        }
        self.cc_data = cc_data
        self.action = action
        self.lights = lights_instance
        self.state = state

        self.pad_handler = PadHandler(self.event, self.mode_manager, self.lights, self.state)
        self.encoder_action = encoder_action
        self.triage()

    def handle_pressure(self):
        print('Pressure event')

    def handle_note_on(self):
        if self.event.midiChan == 9:        # Special handling for channel 9 (pads)
            self.handle_channel_9()

        else:
            if self.event.data2 > 0:
                ButtonHandler.act_out(self.event, self.mode_manager, self.action, self.state)

    def handle_channel_9(self):
        self.pad_handler.handle_pad_event()

    def handle_pitch_bend(self):
        PitchBendHandler(self.event, self.mode_manager, self.encoder_action, self.state)

    def handle_control_change(self):
        """Handles control change messages for encoders and buttons."""
        midi_channel = self.event.midiChan
        midi_id = self.event.data1

        if ( midi_channel in self.cc_data["encoders"]) and (midi_id in self.cc_data["encoders"][midi_channel]): # check to make sure that it is in both 
            encoder_handler = EncoderHandler(self.event, self.cc_data, self.mode_manager, self.action, self.lights, self.encoder_action, self.state)
            encoder_handler.set()
        elif (midi_channel in self.cc_data["buttons"]) and (midi_id in self.cc_data["buttons"][midi_channel]): # check to make sure that it is in both
            if self.event.data2 > 0:
                ButtonHandler.act_out(self.event, self.mode_manager, self.action, self.state)
        else:
             print(f"Warning: Unhandled control change message - Channel: {midi_channel}, ID: {midi_id}") # not all messages are expected
    def triage(self):
        handler = self.event_handlers.get(MidiId(self.event.midiId))
        if handler:
            handler()
        else:
            print('Unhandled MIDI event:', self.event.midiId, self.event.data1, self.event.data2, self.event.midiChanEx, self.event.midiChan)
            self.event.handled = True

class EncoderHandler:

    def __init__(self, event, cc_data, mode_manager, action_handler, lights, encoder_action, state):
        # super().__init__(event, cc_data, mode_manager, action_handler, lights)
        self.event = event
        self.mode_manager = mode_manager
        self.action_handler = action_handler
        self.lights = lights
        self.cc_data = cc_data
        self.encoder_action = encoder_action
        self.state = state

    def set(self):
        if self.mode_manager.current_mode.submode == StepSequencerSubmode.PARAMETER_ENTRY:
            self.handle_parameter_entry_encoder(self.event)
        elif ui.getFocused(5) and plugins.isValid(channels.selectedChannel()): 
            self.control_plugin()
        else:
            try:
                channel_adjusted_knob = self.event.data1
                knob = config_layout.encoder_mappings[controller["encoders"][self.event.midiChan][channel_adjusted_knob]]
                self.set_data(knob)
                encoder_function = knob["functions"][self.state.shift_status]
                # Get the method from action_handler using getattr
                action_method = getattr(self.encoder_action, encoder_function)
                # Call the method with necessary arguments
                action_method(self.event)
            except Exception as e:
                print(f"Error occured: {e}. A function may not be assigned. Check entry in config_layout.py")
            else:
                pass

    def set_data(self, d):
        if config.FOLLOW_TRACK and mixer.trackNumber() != 0:
            track_offset = (mixer.trackNumber() // 8) * 8
        else:
            track_offset = 0
        self.state.track_number = d["track"] + track_offset

    def control_plugin(self):
        plugin_name = plugins.getPluginName(channels.selectedChannel())  
        param_count = plugins.getParamCount(channels.selectedChannel())
        if plugin_name in plugindata.plugin_dict and self.event.data1 in plugindata.knob_numbers:  #plugindata.knob_numbers.index(self.event.data1) < len(plugindata.plugin_dict[plugin]):
            try:
                parameter_index = plugindata.plugin_dict[plugin_name][plugindata.knob_numbers.index(self.event.data1) + (self.event.midiChan * controller["knob_count"])]
                parameter_value =  self.event.data2/127.0 
                plugins.setParamValue(parameter_value, parameter_index, channels.selectedChannel())
                self.event.handled = True
            except:
                print('Knob not assigned. Add to plugin in plugindata.py')
        else:   
            parameter_index = self.event.data1 - config.PLUGIN_KNOB_OFFSET
            plugins.setParamValue(self.event.data2/127.0, parameter_index, channels.selectedChannel())
            self.event.handled = True

    def jogWheel(self, data):
        if data[self.event.data1].get(self.event.data2, {}):
            # print(data[self.event.data1][self.event.data2]['actions'])
            Main.transport_act(self, data[self.event.data1][self.event.data2]['actions'], Action.get_shift_status())

    def channel_link(cc):
        tracks = [i for i in range(0, 128)]
        if cc >= 65:
            if Encoder.link_chan > 0:
                Encoder.link_chan -= 1
        elif Encoder.link_chan < 127:
            Encoder.link_chan += 1
        return tracks[Encoder.link_chan]

    def handle_parameter_entry_encoder(self, event):
        """Handles encoder events in PARAMETER_ENTRY submode."""

        encoder_id = event.data1
        encoder_value = event.data2

        if 14 <= encoder_id <= 20:                  
            self.state.parameter_index = encoder_id - 14  
            param_layout = self.mode_manager.current_mode.parameter_entry_layout
            action_func_name = param_layout.action_func_name
            action_method = getattr(self.encoder_action, action_func_name, None)
            if action_method:
                # Call the specific action method (e.g., set_parameter_ramp)
                action_method(self.event)
                self.event.handled = True # Mark event as handled
            else:
                print(f"Warning: Action method '{action_func_name}' not found in EncoderAction for layout '{param_layout.name}'.")
                self.event.handled = True 

        elif encoder_id == 21:
            channels.closeGraphEditor(True)
            self.event.handled = True


class ButtonHandler():
    @staticmethod
    def act_out(event, mode_manager, action_handler, state):
        """Handles button inputs and assigns function from FL Studio API."""
        button_id = event.data1
        button_data = config_layout.buttons.get(controller["buttons"][event.midiChan].get(button_id))
        if button_data["functions"][state.shift_status]:
            print(f"Shift Status: {state.shift_status}")
            state.track_original = button_data["track"] 
            action_method = getattr(action_handler, button_data["functions"][state.shift_status], None)
            if action_method:
                try:
                    action_method()
                except Exception as e:
                    print(f"Error with action: {e}. ")
            else:
                print(f"Warning: Method '{button_data["functions"][state.shift_status]}' not found in action_handler.")
        else:
            print(f"Warning: No button data found for button ID {button_id}.")
        if button_data["functions"][state.shift_status] != 'nothing':
            event.handled = True

class PitchBendHandler:
    """Handles events from the '+' and '-' buttons, adjusting parameters
    contextually based on the current mode and submode.
    """
    zero_status = True  # Tracks if buttons are in a neutral state

    def __init__(self, event, mode_manager, encoder_action, state):
        self.event = event
        self.plus_status = False
        self.minus_status = False
        self.mode_manager = mode_manager
        self.encoder_action = encoder_action
        self.state = state
        self.handle_bend_event()

    def handle_bend_event(self):
        """Processes '+' and '-' button presses, preventing rapid triggering."""
        if self.mode_manager.get_mode().name == "NOTES":
            if config_layout.pitch_bend[self.state.shift_status] == "pitch_bend":
                print('pitch_bend')
                # channels.setChannelPitch(channels.selectedChannel(), -1.0)

                self.event.handled = False
            else:
                self.convert_plus_minus()
                self.event.handled = True
        else:
            self.convert_plus_minus()
            self.event.handled = True
        self.state.set_plus_minus_leds()

    def convert_plus_minus(self):


        if self.event.data2 > 64:  # '+' button pressed
            if self.plus_status != True and PitchBendHandler.zero_status == True:
                self.plus_status = True
                PitchBendHandler.zero_status = False
                self.modify_parameter_by_increment(1)
            elif self.plus_status == True:
                self.plus_status = False

        elif self.event.data2 < 64:  # '-' button pressed
            if self.minus_status != True and PitchBendHandler.zero_status == True:
                self.minus_status = True
                PitchBendHandler.zero_status = False
                self.modify_parameter_by_increment(-1)
            elif self.minus_status == True:
                self.minus_status = False

        elif self.event.data1 == 0 and self.event.data2 == 64:  # Button released
            PitchBendHandler.zero_status = True
            self.plus_status = False
            self.minus_status = False


    def modify_parameter_by_increment(self, increment):
        """Calls the appropriate handler on the current mode object based on the increment.

        Args:
            increment (int): 1 for '+' button, -1 for '-' button.
        """
        if self.mode_manager.current_mode:
            if increment > 0:
                self.mode_manager.current_mode.handle_plus_button()
            else:
                self.mode_manager.current_mode.handle_minus_button()

