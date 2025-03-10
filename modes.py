import ui
import patterns
import channels
import mixer
import device
import config
import transport
from lights import Lights
import lights
import data
from enum import Enum
from notes import Notes, Scales
import data
from midi_mapping import controller
import plugindata
import plugins

class MainMode(Enum):
    NOTES = 0
    STEP_SEQUENCER = 1
    PAD_PER_CHANNEL = 2
    MIXER_CONTROL = 3

class NoteSubmode(Enum):
    KEYBOARD = 0
    CONTINUOUS = 1
    DRUM = 2

class StepSequencerSubmode(Enum):
    STANDARD = 0
    PARAMETER_ENTRY = 1

class PadPerChannelSubmode(Enum):
    STANDARD = 0

class MixerControlSubmode(Enum):
    MUTE = 0
    SOLO = 1

class Mode:

    def __init__(self, state, lights_instance):
        if type(self) is Mode:
            raise Exception("Mode class cannot be instantiated directly. Use a subclass.")
        self.state = state
        self.lights_instance = lights_instance
        self.submode = None

    def enter(self):
        """Called when the mode is entered."""
        raise NotImplementedError

    def exit(self):
        """Called when the mode is exited."""
        raise NotImplementedError

    def handle_plus_button(self):
        """Handles the '+' button press."""
        raise NotImplementedError

    def handle_minus_button(self):
        """Handles the '-' button press."""
        raise NotImplementedError

    def update_display(self):
        """Updates the display (e.g., hint messages, LEDs) for this mode."""
        raise NotImplementedError

    def set_submode(self, submode):
        """Sets the submode for the mode."""
        self.submode = submode
        self.update_display()

    def cycle_submode(self, increment):
        self.set_plus_minus_leds()
        submodes = list(self.submode_enum)
        current_index = submodes.index(self.submode)
        new_index = (current_index + increment) % len(submodes)
        self.submode = submodes[new_index]
        self.update_display()

    def set_plus_minus_leds(self):
        if self.state.shift_status:
            led_2 = "plus_off"
        else:
            led_2 = "plus_white"
        self.lights_instance.update_octaves(( led_2, "minus_white"))

class ModeManager:
    def __init__(self, lights_instance, state):
        self.previous_layout = None  
        self.current_layout = None
        self.scales = Scales()
        self.modes = {
            MainMode.NOTES: NotesMode(lights_instance, state),
            MainMode.STEP_SEQUENCER: StepSequencerMode(lights_instance, state),
            MainMode.PAD_PER_CHANNEL: PadPerChannelMode(lights_instance, state),
            MainMode.MIXER_CONTROL: MixerControlMode(lights_instance, state)
        }
        self.active_modes = []

        for mode_name in config.ACTIVE_MODES:
            try:
                mode_enum = MainMode[mode_name]
                self.active_modes.append(mode_enum)
            except KeyError:
                print(f"Invalid Mode Name: {mode_name}")

        self.state = state
        self.current_mode_enum = MainMode.NOTES  # Store the current mode enum
        self.current_mode = self.modes[self.current_mode_enum]
        self.lights_instance = lights_instance

    def set_mode(self, mode_enum=None):

        if mode_enum is None:
            # Cycle to the next mode if no mode is specified
            mode_enums = list(self.active_modes)
            current_mode_index = mode_enums.index(self.current_mode_enum)
            next_mode_index = (current_mode_index + 1) % len(mode_enums)
            next_mode_enum = mode_enums[next_mode_index]
        else: 
            next_mode_enum = mode_enum

        if self.current_mode:
            self.current_mode.exit()

        self.current_mode_enum = next_mode_enum
        self.current_mode = self.modes[next_mode_enum]
        self.current_mode.enter()

    def get_mode(self):
        if self.current_mode:
            return self.current_mode_enum  
        else:
            return None

    def get_submode(self):
        if self.current_mode and hasattr(self.current_mode, "submode"):
            return self.current_mode.submode.name  # Return the name (string)
        else:
            return None

    def get_layout(self):
        if self.current_mode and hasattr(self.current_mode, "layout"):
            return self.current_mode.layout.name
        else:
            return None

    def refresh_leds(self):

        if self.get_layout() != "KEYBOARD" and self.get_layout() != "DEFAULT_PADS":
            print('refresh_leds')
            self.current_mode.update_display()

    def set_layout(self, layout):
        # If switching layouts, store the current one as the previous layout
        if self.current_layout and self.current_layout != layout:
            self.previous_layout = self.current_layout

        self.current_layout = layout
        if self.current_mode:
            self.current_mode.update_display()

class NotesLayout(Enum):
    KEYBOARD = (0, "Keyboard", "keyboard_leds")
    CONTINUOUS = (1, "Continuous", "continuous_leds")
    DRUM = (2, "DrumPlugin", "drum_plugin_leds")

    def __init__(self, value, layout_name, led_method_name):
        self._value_ = value
        self.layout_name = layout_name
        self.led_method_name = led_method_name

    def update_leds(self, lights_instance, state, color=None):
        """Calls the appropriate method to update the LEDs for this layout."""
        led_method = getattr(self, self.led_method_name)
        led_method(lights_instance, state)

    def keyboard_leds(self, lights_instance, state):
        """Updates LEDs for the keyboard layout."""
        new_led_state = []
        for key_num in range(36, 68): 
            if key_num in lights_instance.c_keys:
                new_led_state.append((key_num, 1, "blue"))  # C note: blue
            elif key_num in lights_instance.off_keys:
                new_led_state.append((key_num, 0, "off"))
            else:
                new_led_state.append((key_num, 1, "white"))  # Other notes: white
        new_led_state.append((0, 1, "yellow"))
        lights_instance.update_led_state(new_led_state)
        lights_instance.send_midi_messages()

    def continuous_leds(self, lights_instance, state):
        new_led_state = []
        scale = Scales.get_scale(state.scale_choice)
        root_note = Notes.root
        octave_base = Notes.get_octave()
        start_note = octave_base + root_note
        for i in range(32):  # Iterate over the 32 pads
            scale_index = i % len(scale)
            key_num = i + 36

            if 36 <= key_num < 68:
            #     # Check if the note is the root note
                if scale_index == 0:
                    new_led_state.append((key_num, 1, "purple"))  # Root note: blue
                else:
                    new_led_state.append((key_num, 1, "white"))  # Other notes in scale: white

        lights_instance.update_led_state(new_led_state)
        lights_instance.send_midi_messages()

    def drum_plugin_leds(self, lights_instance, state, color=None):
        """Updates LEDs for drum plugin layout."""
        new_led_state = []
        for key_num in range(36, 52):
            if key_num in lights.sequence_fours:
                new_led_state.append((key_num, 1, "light_purple"))  # Set all pads to orange
            else:
                new_led_state.append((key_num, 1, "purple"))  # Set all pads to orange
        for key_num in range(52, 68):
            if key_num in lights.sequence_fours:
                new_led_state.append((key_num, 1, "light_blue"))  # Set all pads to orange
            else:
                new_led_state.append((key_num, 1, "blue"))  # Set all pads to orange
        lights_instance.update_led_state(new_led_state)
        lights_instance.send_midi_messages()

class MixerControlLayout(Enum):

    MUTE = (0, "Mute Tracks", "mute_track_leds", "mute_pad_action")
    SOLO = (1, "Solo Tracks", "solo_track_leds", "solo_pad_action")

    def __init__(self, value, layout_name, led_method_name, pad_action_method_name):
        self._value_ = value  
        self.layout_name = layout_name
        self.led_method_name = led_method_name
        self.pad_action_method_name = pad_action_method_name
        self.recent_step = -1
        self.pattern_access_range = 0
        self.channel_access_range = 0

    def __str__(self):
        return self.name 

    def update_leds(self, lights_instance, state, color=None):
       """Calls the appropriate method to update the LEDs for this layout."""
       led_method = getattr(self, self.led_method_name)
       led_method(lights_instance, state, color)

    def handle_pad_press(self, pad_handler, event, state):
        """Calls the appropriate handler method for pad press events."""
        # self.pad_action_method(pad_handler, event)
        method = getattr(self, self.pad_action_method_name)
        method(pad_handler, event, state)

    def mute_pad_action(self, pad_handler, event, state):
        """Handles default step mode pad press behavior."""
        track = event.data1 - 35
        if event.data2 > 0:
            mixer.muteTrack(track)
        event.handled = True

    def solo_pad_action(self, pad_handler, event, state):
        """Handles default step mode pad press behavior."""
        track = event.data1 - 35
        if event.data2 > 0:
            mixer.soloTrack(track)
        event.handled = True

    def mute_track_leds(self, lights_instance, state, color=None):
        new_led_state = []
        for i in range(1, 33):
            if mixer.isTrackMuted(i):
                new_led_state.append((35 + i, 0, "off"))
            else:
                new_led_state.append((35 + i, 1, "light_green"))
        lights_instance.update_led_state(new_led_state)
        lights_instance.send_midi_messages()

    def solo_track_leds(self, lights_instance, state, color=None):
        new_led_state = []
        for i in range(1, 33):
            if mixer.isTrackMuted(i):
                new_led_state.append((35 + i, 0, "off"))
            else:
                new_led_state.append((35 + i, 1, "mid_purple"))
        lights_instance.update_led_state(new_led_state)
        lights_instance.send_midi_messages()

class StepSequencerLayout(Enum):

    STEP_32 = (0, "32 Step", "step_32_leds", "default_pad_action")
    PATTERN_ACCESS = (1, "Pattern Access", "pattern_select_leds", "pattern_select_action")
    CHANNEL_SELECT = (2, "Channel Select", "channel_select_leds", "channel_select_action")
    CHANNEL_MUTE = (3, "Channel Mute", "channel_mute_leds", "channel_mute_action")


    def __init__(self, value, layout_name, led_method_name, pad_action_method_name):
        self._value_ = value  
        self.layout_name = layout_name
        self.led_method_name = led_method_name
        self.pad_action_method_name = pad_action_method_name
        self.sequence_fours = [52, 56, 60, 64]
        self.recent_step = -1
        self.pattern_access_range = 0
        self.channel_access_range = 0

    def __str__(self):
        return self.name

    def update_leds(self, lights_instance, state, color=None):
        """Calls the appropriate method to update the LEDs for this layout."""
        led_method = getattr(self, self.led_method_name)
        led_method(lights_instance, state, color)
        self.step_16_leds(lights_instance, state, color)
    
    def step_32_leds(self, lights_instance, state, color=None):
        new_led_state = []
        for i in range(16, 32):
            if channels.getGridBit(channels.selectedChannel(), i) == 1:
                new_led_state.append((36 + i, 1, color if color else "white"))  # Use color if provided
            else:
                new_led_state.append((36 + i, 0, "off"))
        lights_instance.update_led_state(new_led_state)
        lights_instance.send_midi_messages()

    def step_16_leds(self, lights_instance, state, color=None):
        new_led_state = []
        for i in range(16):
            if channels.getGridBit(channels.selectedChannel(), i) == 1:
                new_led_state.append((36 + i, 1, color if color else "white"))  # Use color if provided
            else:
                new_led_state.append((36 + i, 0, "off"))
        lights_instance.update_led_state(new_led_state)
        lights_instance.send_midi_messages()


    def channel_select_leds(self, lights_instance, state, color):
        """Updates LEDs for the channel select layout."""
        new_led_state = []
        for i in range(16):
            if i == channels.selectedChannel():
                new_led_state.append((52 + i, 1, "white"))  # Non-selectable channels off
            elif i < channels.channelCount():
                if (i + 52) in self.sequence_fours:
                    new_led_state.append((i + 52, 1, "mid_purple") )
                else:
                    new_led_state.append((52 + i, 1, "purple"))  # Indicate selectable channels
            else:
                new_led_state.append((52 + i, 0, "off"))  # Non-selectable channels off
        lights_instance.update_led_state(new_led_state)
        lights_instance.send_midi_messages()

    def handle_pad_press(self, pad_handler, event, state):
        """Calls the appropriate handler method for pad press events."""
        # self.pad_action_method(pad_handler, event)
        method = getattr(self, self.pad_action_method_name)
        method(pad_handler, event, state)

    def default_pad_action(self, pad_handler, event, state):
        """Handles default step mode pad press behavior."""
        if event.data2 > 0:
            if channels.getGridBit(channels.selectedChannel(), event.data1 - 36) == 0:
                 channels.setGridBit(channels.selectedChannel(), event.data1 - 36, 1)
            else:
                channels.setGridBit(channels.selectedChannel(), event.data1 - 36, 0)
        event.handled = True

    def pattern_select_action(self, pad_handler, event, state):
        """Handles pad presses in Pattern Select layout."""
        pattern_pressed = event.data1 - 51 + (16 * self.pattern_access_range)
        if event.data2 > 0:
            if state.pattern_change_immediate or not transport.isPlaying():
                patterns.jumpToPattern(pattern_pressed)
                event.handled = True
            elif not state.pattern_change_immediate:
                state.next_pattern = event.data1 - 51 + (16 * self.pattern_access_range)
                event.handled = True
            else:
                event.handled = True

    def pattern_select_leds(self, lights_instance, state, color):
        """Updates LEDs for the pattern select layout."""
        new_led_state = []
        pattern_led = patterns.patternNumber() - (self.pattern_access_range * 16) - 1
        for i in range(16):
            if i == pattern_led:
                new_led_state.append((52 + i, 1, "blue"))
            elif (i) == self.pattern_access_range * 4:
                new_led_state.append((i + 52, 1, "purple") )
            elif (i + 52) in self.sequence_fours:
                new_led_state.append((i + 52, 1, "light_purple") )
            else:
                new_led_state.append((i + 52, 1, "white") )
        lights_instance.update_led_state(new_led_state)
        lights_instance.send_midi_messages()

    def channel_select_action(self, pad_handler, event, state):
        """Handles pad presses in channel select layout."""
        if event.data2 > 0:
            if event.data1 - 52 >= channels.channelCount() - (16 * self.channel_access_range):
                return
            else:
                channels.selectOneChannel((event.data1 - 52) + (16 * self.channel_access_range))
                event.handled = True

    def channel_mute_action(self, pad_handler, event, state):
        """Handles pad presses in channel mute layout"""
        if event.data2 > 0:
            if event.data1 - 52 >= channels.channelCount() - (16 * self.channel_access_range):
                 return
            else:
                 channels.muteChannel((event.data1 - 52) + (16 * self.channel_access_range))
                 event.handled = True

    def channel_mute_leds(self, lights_instance, state, color):
        """Updates LEDs for the channel mute layout."""
        new_led_state = []
        for i in range(16):
            if (16 * self.channel_access_range) + i < channels.channelCount():
                if channels.isChannelMuted((16 * self.channel_access_range) + i):
                    new_led_state.append((52 + i, 1, "light_yellow"))  # Muted, LED off
                else:
                    new_led_state.append((52 + i, 1, "yellow"))  # Not muted, LED yellow
            else:
                new_led_state.append((52 + i, 0, "off"))  # Beyond channel count, LED off
        lights_instance.update_led_state(new_led_state)
        lights_instance.send_midi_messages()

    def update_active_step(self, lights_instance):

        current_step = mixer.getSongStepPos() % 32 # get the current step, make sure not over the sequence length
        new_led = current_step + 36
        new_led_state = [] # create a new blank instance for lights
        new_led_state.append(self.get_led_state(new_led, lights_instance))
        current_step_state = []
        if current_step != self.recent_step:
            current_step_state.append((new_led, 1, "white"))
            lights_instance.update_led_state(current_step_state)  # Turn on the new LED
            lights_instance.send_midi_messages()

        lights_instance.update_led_state(new_led_state)  # Turn on the new LED
        self.recent_step = current_step

    def get_led_state(self, led_num, lights_instance):
        for led, state, color in lights_instance.led_state:  # Access using the property
            if led == led_num:
                return (led, state, color)
        return (led_num, 0, "off")  # Default if not found

class PadPerChannelLayout(Enum):

    DEFAULT_PADS = (0, "Default", "default_leds", "default_action")

    def __init__(self, value, layout_name, led_method_name, pad_action_method_name):
        self._value_ = value  
        self.layout_name = layout_name
        self.led_method_name = led_method_name
        self.pad_action_method_name = pad_action_method_name
        self.channel_access_range = 0

    def update_leds(self, lights_instance, color=None):
        """Calls the appropriate method to update the LEDs for this layout."""
        led_method = getattr(self, self.led_method_name)
        led_method(lights_instance, color)

    def default_leds(self, lights_instance, color=None):
        lights_instance.clear_all_leds()
        channel_count = channels.channelCount()
        new_led_state = []
        for i in range(32):
            if i + (self.channel_access_range * 32) < channels.channelCount():
                new_led_state.append((36 + i, 1, "purple"))
            else:
                new_led_state.append(((36 + i), 1, "off"))

        lights_instance.update_led_state(new_led_state)
        lights_instance.send_midi_messages()

class MixerControlMode(Mode):
    def __init__(self, lights_instance, state):
        super().__init__(state, lights_instance)
        self.mode_id = MainMode.MIXER_CONTROL
        self.layout = MixerControlLayout.MUTE 
        self.submode = MixerControlSubmode.MUTE 
        self.submode_enum = MixerControlSubmode 
        self.lights = lights_instance
        self.state = state  

    def set_layout(self, layout):
        if isinstance(layout, MixerControlLayout):
            self.layout = layout 
        else:
            print(f"Warning: Invalid layout type: {type(layout)}")
        self.update_display()

    def handle_pad_press(self, event):
        self.layout.handle_pad_press(self, event, self.state)         

    def enter(self):
        print("Entering Mixer Control Mode")
        self.update_display()

    def exit(self):
        print("Exiting Mixer Control Mode")

    def handle_plus_button(self):
        self.cycle_layout(1)

    def handle_minus_button(self):
        self.cycle_layout(-1)

    def update_display(self):
        ui.setHintMsg(f"Mixer Control - {(self.submode.name).capitalize()}")
        if self.submode == MixerControlSubmode.MUTE:
            self.layout = MixerControlLayout.MUTE  
        elif self.submode == MixerControlSubmode.SOLO:
            self.layout = MixerControlLayout.SOLO
        self.layout.update_leds(self.lights, self.state) 

    def cycle_layout(self):
        self.set_plus_minus_leds()
        pass

class NotesMode(Mode):
    def __init__(self, lights_instance, state):
        super().__init__(state, lights_instance)  # Call Mode's __init__
        self.submode_options = [NoteSubmode[mode_name] for mode_name in config.NOTES_SUBMODES]
        self.display_name = "Notes"
        self.submode = NoteSubmode.KEYBOARD
        self.submode_enum = NoteSubmode
        self.mode_id = MainMode.NOTES
        self.octave_iter = 3
        self.root_iter = 0
        self.scale_iter = 0
        self.octave_names = ['-3', '-2', '-1', '0', '1', '2', '3']
        self.lights = lights_instance
        self.layout = NotesLayout.KEYBOARD

    def enter(self):
        print("Entering Notes Mode")
        self.update_display()

    def exit(self):
        print("Exiting Notes Mode")

    def cycle_submode(self, increment):
        current_index = self.submode_options.index(self.submode)
        new_index = (current_index + increment) % len(self.submode_options)
        self.set_submode(self.submode_options[new_index])
        self.update_display()

    def set_submode(self, submode):
        if submode in self.submode_options:
            self.submode = submode
            if self.submode == NoteSubmode.KEYBOARD:
                self.layout = NotesLayout.KEYBOARD
            elif self.submode == NoteSubmode.CONTINUOUS:
                self.layout = NotesLayout.CONTINUOUS
            elif self.submode == NoteSubmode.DRUM:
                self.layout = DrumPluginLayout.DRUM_PLUGIN  
            self.update_display()
        else:
            print(f"Warning: Invalid submode '{submode}' for NotesMode")

    def get_submode(self):
        return self.submode

    def handle_plus_button(self):
        self.state.octave_index = (self.state.octave_index + 1) % len(self.octave_names)
        ui.setHintMsg(f"Octave: {self.octave_names[self.state.octave_index]}")
        self.update_display()

    def handle_minus_button(self):
        self.state.octave_index = (self.state.octave_index - 1) % len(self.octave_names)
        ui.setHintMsg(f"Octave: {self.octave_names[self.state.octave_index]}")
        self.update_display()

    def adjust_root_note(self, increment):
        self.root_iter += increment
        if self.root_iter >= len(data.notes_list):
            self.root_iter = 0
        self.update_display()

    def adjust_scale(self, increment):
        self.scale_iter += increment
        if self.scale_iter >= len(data.scale_names):
            self.scale_iter = 0
        self.update_display()

    def update_display(self):
        if self.submode == NoteSubmode.KEYBOARD:
            self.layout = NotesLayout.KEYBOARD  
        elif self.submode == NoteSubmode.CONTINUOUS:
            self.layout = NotesLayout.CONTINUOUS  
        elif self.submode == NoteSubmode.DRUM:
            self.layout = NotesLayout.DRUM  
        self.layout.update_leds(self.lights, self.state) 

    def handle_pad_press(self, event):
        if self.submode == NoteSubmode.DRUM:
            self.handle_drum_plugin_pad(event)
        elif self.submode == NoteSubmode.KEYBOARD:
            self.handle_keyboard_note(event)
        elif self.submode == NoteSubmode.CONTINUOUS:
            self.handle_continuous_note(event)


    def handle_keyboard_note(self, event):
        octave = Notes.octaves[self.state.octave_index]
        if str(event.data1) in data.key_dict:
            channels.midiNoteOn(channels.channelNumber(), data.key_dict[str(event.data1)] + octave, event.data2)
        else:
            channels.midiNoteOn(channels.channelNumber(), event.data1, event.data2)
        event.handled = True

    def handle_continuous_note(self, event):
        scale = Scales.get_scale(self.state.scale_choice)
        root = self.state.root_note
        index = (event.data1 - 36) % len(scale)
        octave = Notes.octaves[self.state.octave_index]
        offset =  ((event.data1 - 36) // (len(scale))) * 12
        note = octave + scale[index] + root + offset + 36
        channels.midiNoteOn(channels.channelNumber(), note, event.data2)
        event.handled = True

    def handle_drum_plugin_pad(self, event):
        """called when a drum plugin window is focused and plays corresponding drum pad"""
        print(channels.channelNumber())
        try:
            if event.data1 in plugindata.atom_sq_pads:
                channels.midiNoteOn(channels.channelNumber(), plugindata.FPC_pads[plugindata.atom_sq_pads.index(event.data1)], event.data2)
                event.handled = True
        except Exception as e:
            print(e)
        event.handled = True

    def get_octave(self):
        return self.octave_iter

    def cycle_range(self):
        pass

class StepSequencerMode(Mode):
    def __init__(self, lights_instance, state):
        super().__init__(state, lights_instance)
        self.mode_id = MainMode.STEP_SEQUENCER
        self.layout = StepSequencerLayout.STEP_32
        self.active_layouts = [
            layout for layout in StepSequencerLayout
            if layout.name in config.STEP_SEQUENCER_LAYOUTS
        ]
        if not self.active_layouts:
            # Fallback to all layouts if the config is empty
            self.active_layouts = list(StepSequencerLayout)
        self.current_layout_index = 0  # Track current layout index

        self.submode = StepSequencerSubmode.STANDARD
        self.submode_enum = StepSequencerSubmode
        self.lights = lights_instance

    def set_layout(self, layout):
        if isinstance(layout, StepSequencerLayout):
            self.layout = layout 
        else:
            print(f"Warning: Invalid layout type: {type(layout)}")
        self.update_display()

    def handle_pad_press(self, event):
        if self.submode == StepSequencerSubmode.PARAMETER_ENTRY:
            print("PARAMETER_ENTRY")
            pad_index = event.data1 - 36
            if 0 <= pad_index < 32:
                self.state.selected_step = pad_index
                self.update_leds_for_parameter_entry()  
                event.handled = True 
        elif event.data1 < 52:
            self.layout.default_pad_action(self, event, self.state)
        else:
            self.layout.handle_pad_press(self, event, self.state) 

    def enter(self):
        print("Entering Step Sequencer Mode")
        self.update_display()

    def exit(self):
        print("Exiting Step Sequencer Mode")

    def handle_plus_button(self):
        self.cycle_layout(1)

    def handle_minus_button(self):
        self.cycle_layout(-1)

    def cycle_range(self):
        if self.get_layout() == "PATTERN_ACCESS":
            self.layout.pattern_access_range += 1
            if self.layout.pattern_access_range >= 4:
                self.layout.pattern_access_range = 0
            ui.setHintMsg(f"Pattern Range: {(self.layout.pattern_access_range * 16) + 1} - {(self.layout.pattern_access_range * 16) + 16}")
        elif self.get_layout() != 'STEP_32':
            self.layout.channel_access_range += 1
            if self.layout.channel_access_range >= 2:
                self.layout.channel_access_range = 0
            ui.setHintMsg(f"Channel Range: {(self.layout.channel_access_range * 16) + 1} - {(self.layout.channel_access_range * 16) + 16}")
        self.update_display()

    def cycle_submode(self, increment):
        submodes = list(StepSequencerSubmode)
        current_index = submodes.index(self.submode)
        new_index = (current_index + increment) % len(submodes)
        self.submode = submodes[new_index]
        channels.closeGraphEditor(channels.selectedChannel())
        self.update_display()

    def update_display(self):
        ui.setHintMsg(f"Step Sequencer - {self.layout.layout_name}")

        if self.submode == StepSequencerSubmode.STANDARD:
            self.layout.update_leds(self.lights, self.state, "blue")  
        elif self.submode == StepSequencerSubmode.PARAMETER_ENTRY:
            # self.layout.update_leds(self.lights, "white") 
            self.update_leds_for_parameter_entry() 


    def update_leds_for_parameter_entry(self):
        """Updates the LEDs to indicate the selected step in parameter entry mode."""
        new_led_state = []
        for i in range(32):
            if i == self.state.selected_step:
                new_led_state.append((36 + i, 1, "purple"))  # Highlight selected step
            elif channels.getGridBit(channels.selectedChannel(), i) == 1:
                new_led_state.append((36 + i, 1, "white"))  # Use white for other steps
            else:
                new_led_state.append((36 + i, 0, "off"))
        self.lights.update_led_state(new_led_state)
        self.lights.send_midi_messages()

    def get_layout(self):
        return self.layout.name

    def set_layout(self, layout):
        if isinstance(layout, StepSequencerLayout):
            self.layout = layout
        else:
            print(f"Warning: Invalid layout type: {type(layout)}")
        self.update_display()

    def cycle_layout(self, increment):
        self.current_layout_index = (self.current_layout_index + increment) % len(self.active_layouts)
        self.set_layout(self.active_layouts[self.current_layout_index])
        # layouts = list(StepSequencerLayout)
        # current_index = layouts.index(self.layout)
        # new_index = (current_index + increment) % len(layouts)
        # self.set_layout(layouts[new_index])

class PadPerChannelMode(Mode):
    def __init__(self, lights_instance, state):
        self.mode_id = MainMode.PAD_PER_CHANNEL
        self.submode = PadPerChannelSubmode.STANDARD
        self.layout = PadPerChannelLayout.DEFAULT_PADS
        self.submode_enum = PadPerChannelSubmode
        self.mult_options = ['1-16', '17-32']
        self.lights = lights_instance
        self.channel_access_range = 0
        self.lights_instance = lights_instance
        self.state = state

    def set_layout(self, layout):
        if isinstance(layout, PadPerChannelLayout):
            self.layout = layout 
        else:
            print(f"Warning: Invalid layout type: {type(layout)}")
        self.update_display()

    def enter(self):
        print("Entering Pad Per Channel Mode")
        ui.setHintMsg(MainMode.PAD_PER_CHANNEL.name)
        self.update_display()

    def exit(self):
        print("Exiting Pad Per Channel Mode")

    def handle_plus_button(self):
        pass

    def handle_minus_button(self):
        pass 

    def update_display(self):
        ui.setHintMsg(f"Pad Per Channel: {self.mult_options[self.channel_access_range]}")
        self.layout.update_leds(self.lights)

    def handle_pad_press(self, event):
        """takes event midi data from pad press and plays corresponding channel"""
        if (event.data1-36) + (self.layout.channel_access_range * 32) < channels.channelCount():
            channels.selectOneChannel((event.data1-36) + (self.layout.channel_access_range * 32))
            channels.midiNoteOn(channels.channelNumber() + (self.layout.channel_access_range * 32), 60, event.data2)
            event.handled = True
        else:
            event.handled = True

    def handle_pad_release(self, event):
        """takes event midi data from pad press and plays corresponding channel"""
        if (event.data1-36) + (self.layout.channel_access_range * 32) < (channels.channelCount()):
            channels.selectOneChannel((event.data1-36) + (self.layout.channel_access_range * 32))
            channels.midiNoteOn(channels.channelNumber() + (self.layout.channel_access_range * 32), 60, event.data2)
            event.handled = True
        else:
            event.handled = True

    def cycle_range(self):
        self.layout.channel_access_range += 1
        if self.layout.channel_access_range >= 2:
            self.layout.channel_access_range = 0
        self.update_display()
        ui.setHintMsg(f"Channel Range - {self.layout.channel_access_range}")

class DrumPluginLayout(Enum):
    DRUM_PLUGIN = (0, "DrumPlugin", "drum_plugin_leds")

    def __init__(self, value, layout_name, led_method_name):
        self._value_ = value
        self.layout_name = layout_name
        self.led_method_name = led_method_name

    def update_leds(self, lights_instance, color=None):
        """Calls the appropriate method to update the LEDs for this layout."""
        led_method = getattr(self, self.led_method_name)
        led_method(lights_instance, color)

    def drum_plugin_leds(self, lights_instance, color=None):
        """Updates LEDs for drum plugin layout."""
        new_led_state = []
        for key_num in range(36, 52):
            if key_num in lights.sequence_fours:
                new_led_state.append((key_num, 1, "light_purple"))  # Set all pads to orange
            else:
                new_led_state.append((key_num, 1, "purple"))  # Set all pads to orange
        for key_num in range(52, 68):
            if key_num in lights.sequence_fours:
                new_led_state.append((key_num, 1, "light_blue"))  # Set all pads to orange
            else:
                new_led_state.append((key_num, 1, "blue"))  # Set all pads to orange
        lights_instance.update_led_state(new_led_state)
        lights_instance.send_midi_messages()

