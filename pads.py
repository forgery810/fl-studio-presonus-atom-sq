import ui
import channels
import device
import patterns
import plugins
import transport
import midi
from modes import Mode, MainMode, NotesMode, NoteSubmode, PadPerChannelMode
from lights import Lights
import data
import plugindata
import sys
from notes import Notes

class PadHandler:

    def __init__(self, event, mode_manager, lights_instance, state):
        self.event = event
        self.mode_manager = mode_manager
        self.original_state = 0
        self.pressed_pads = {}
        self.lights = lights_instance
        self.mode_manager = mode_manager
        self.state = state

    def handle_pad_event(self):
        """takes midi event data and passes it to appropriate function based on current mode found in Modes()"""
        # if ui.getFocusedPluginName() in plugindata.drum_plugs:
        #     return self.handle_drum_plugin_pad(self.event)
        if self.event.midiId == 144:
            return self.handle_pad_press()
        elif self.event.midiId == 128: 
            return self.handle_pad_release()
        current_mode = self.mode_manager.get_mode()

    def get_led_state(self, led_num):
         """Gets the current state of an LED from the lights instance."""
         for led, state, color in self.lights.led_state:  # Access using the property
             if led == led_num:
                 return (led, state, color)
         return (led_num, 0, "off")  # Default if not found

    def handle_pad_press(self):
        """Handle any function needed that is common to all pad presses rather than defering to the mode's handle_pad_press"""
        self.mode_manager.current_mode.handle_pad_press(self.event)

    def handle_pad_release(self):
        """Handles pad releases, restoring the original LED state."""
        if isinstance(self.mode_manager.current_mode, NotesMode):
            if self.mode_manager.current_mode.submode == NoteSubmode.KEYBOARD:
                self.mode_manager.current_mode.handle_keyboard_note(self.event)
            elif self.mode_manager.current_mode.submode == NoteSubmode.CONTINUOUS:
                self.mode_manager.current_mode.handle_continuous_note(self.event)
            elif self.mode_manager.current_mode.submode == NoteSubmode.DRUM:
                self.mode_manager.current_mode.handle_drum_plugin_pad(self.event)
        elif isinstance(self.mode_manager.current_mode, PadPerChannelMode):
            self.mode_manager.current_mode.handle_pad_press(self.event)
        pad_num = self.event.data1
        if self.get_led_state(pad_num):
            original_state = self.get_led_state(pad_num)  # Get and remove original state
            self.lights.update_led_state([original_state])
            self.lights.send_midi_messages()

    def handle_drum_plugin_pad(self, event):
        """called when a drum plugin window is focused and plays corresponding drum pad"""

        if plugins.getPluginName(channels.selectedChannel()) == 'FPC' and event.data1 in plugindata.atom_sq_pads:
            channels.midiNoteOn(channels.selectedChannel(), plugindata.FPC_pads[plugindata.atom_sq_pads.index(event.data1)], event.data2)
            event.handled = True
        elif plugins.getPluginName(channels.selectedChannel()) == 'Slicex':
            channels.midiNoteOn(channels.selectedChannel(), event.data1 + 24, event.data2)
            event.handled = True

    def get_mode(self):
        return Modes.mode

    def get_step_submode(self):
        return Modes.step_iter

    