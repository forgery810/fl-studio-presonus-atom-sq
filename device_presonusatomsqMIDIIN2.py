# name=Presonus Atom SQ MIDIIN2
# Author: ts-forgery
VERSION = '0.8.1'

import device
import general
import transport
import channels
import arrangement
import patterns
import general
import ui
import playlist
import mixer
import midi
from midi_mapping import controller
import config_layout
from enum import Enum
from direction import Directions

def OnInit():
    """called when FL connects with controller"""

    print(f"Presonus Atom SQ MIDIIN2 - Version: {VERSION}")

def OnMidiMsg(event):
    """called by FL everytime a MIDI message is sent by controller"""
    print(event.midiId, event.data1, event.data2, event.midiChanEx, event.midiChan)
    handler = MidiHandler(event)

class MidiId(Enum):
    PRESSURE = 208
    NOTE_ON = 144
    NOTE_OFF = 128
    PITCH_BEND = 224
    CONTROL_CHANGE = 176

class Midi2Action:
    
    """ Holds all functions assignable to buttons and jog wheel. Functions can be added from the Action class so long 
    as they do not rely on mode_manager or state variables. """

    def start(self):   
        return transport.start()

    def start_reset(self):
        if transport.isPlaying():
            transport.stop()
            transport.start()
        else:
            transport.start()

    def stop(self):
        return transport.stop()

    def record(self):
        return transport.record()

    def song_pat(self):
        return transport.setLoopMode()

    def step_rec(self):
        return transport.globalTransport(midi.FPT_StepEdit, 114)

    def overdub(self):
        return transport.globalTransport(midi.FPT_Overdub, 112)

    def metronome(self):
        return transport.globalTransport(midi.FPT_Metronome, 110)

    def loop_record(self):
        return transport.globalTransport(midi.FPT_LoopRecord, 113)

    def tap_tempo(self):
        transport.globalTransport(midi.FPT_TapTempo, 100)

    def wait_for_input(self):
        transport.globalTransport(midi.FPT_WaitForInput, 111)

    def item_menu(self):
        transport.globalTransport(midi.FPT_ItemMenu, 91)

    def menu(self):
        transport.globalTransport(midi.FPT_Menu, 90)

    def undo_up(self):
        transport.globalTransport(midi.FPT_UndoUp, 21)

    def undo_down(self):
        general.undoDown()

    def countdown(self):
        transport.globalTransport(midi.FPT_CountDown, 115)

    def new_pattern(self):
        transport.globalTransport(midi.FPT_F4, 63)

    def clone_pattern(self):
        patterns.clonePattern()

    def save(self):
        transport.globalTransport(midi.FPT_Save, 92)

    def countdown(self):
        transport.globalTransport(midi.FPT_CountDown, 115)

    def jog_wheel_up(self):
        if ui.getFocused(midi.widChannelRack) or ui.getFocused(midi.widMixer):
            print('jog_wheel_up')
            return ui.jog(1)

    def jog_wheel_down(self):
        if ui.getFocused(midi.widChannelRack) or ui.getFocused(midi.widMixer):
            return ui.jog(-1)
    
    def jog_tempo_up(self):
        return transport.globalTransport(midi.FPT_TempoJog, 1)

    def jog_tempo_down(self):
        return transport.globalTransport(midi.FPT_TempoJog, -1)

    def undo(self):
        transport.globalTransport(midi.FPT_Undo, 20)

    def loop_record(self):
        return transport.globalTransport(midi.FPT_LoopRecord, 113)

    def left(self):
        if ui.getFocused(5) and channels.getChannelType(channels.selectedChannel()) != midi.CT_Sampler:
            return ui.previous()
        elif ui.getFocused(midi.widChannelRack):
            return transport.globalTransport(midi.FPT_PatternJog, -1)        
        elif ui.getFocused(midi.widPlaylist):
            return arrangement.jumpToMarker(0, 1)
        else:
            return ui.left()

    def right(self):
        if ui.getFocused(5) and channels.getChannelType(channels.selectedChannel()) != midi.CT_Sampler:
            return ui.next()
        elif ui.getFocused(midi.widChannelRack):
            return transport.globalTransport(midi.FPT_PatternJog, 1)        
        elif ui.getFocused(midi.widPlaylist):
            arrangement.jumpToMarker(1, 1)
        else:
            return ui.right()

    def solo(self):
        if ui.getFocused(midi.widMixer):
            mixer.soloTrack(mixer.trackNumber())
        else:
            channels.soloChannel(channels.selectedChannel())

    def arm(self):
        mixer.armTrack(mixer.trackNumber())

    def mute(self):
        if ui.getFocused(midi.widMixer):
            return mixer.muteTrack(mixer.trackNumber())
        else:
            return channels.muteChannel(channels.selectedChannel())

    def escape(self):
        ui.escape()

midi2_action = Midi2Action()  

class MidiHandler:
    def __init__(self, event):
        self.event = event
        self.handle_event() 

    def handle_event(self):
        if self.event.data1 in Directions.ud_arrow:
             Directions(self.event)
        elif self.event.midiId == MidiId.CONTROL_CHANGE.value:
            self.handle_jog_wheel(self.event)
        elif self.event.midiId == midi.MIDI_NOTEON and midi2_inputs.get(controller["buttons"][self.event.midiChan].get(self.event.data1)) and self.event.data2 > 0:
            print('handle_jog_wheel')
            self.handle_button_press(self.event)
        else:
            self.event.handled = True

    def _call_action_method(self, action_name):
      action_method = getattr(midi2_action, action_name, None)
      if action_method:
        try:
            action_method()
            self.event.handled = True
        except Exception as e:
            print(f"Problem enacting action_method. {e}")
            self.event.handled = True
      else:
         print(f"Warning: Action method '{action_name}' not found in Midi2Action.")
         self.event.handled = False

    def handle_jog_wheel(self, event):
        if event.midiId == MidiId.CONTROL_CHANGE.value: # check that midiId is correct
            jog_action = midi2_inputs["jog_wheel"][0 if event.data2 < 64 else 1]
            self._call_action_method(jog_action)
        else:
            self.event.handled = True

    def handle_button_press(self, event):
        button_id = event.data1
        action_name = midi2_inputs.get(controller["buttons"][event.midiChan].get(button_id))
        print(action_name)
        if action_name:
          self._call_action_method(action_name)
        else:
            print(f"Warning: No button data found for button ID {button_id}. Event data: {event.midiId}, {event.data1}, {event.data2}, {event.midiChanEx}, {event.midiChan}")
            self.event.handled = False


midi2_inputs = {

    "start": "start_reset",
    "stop": "stop",
    "record": "record",
    "metronome": "metronome",
    "shift_stop": "undo",
    "shift_start": "loop_record",
    "shift_record": "save",
    "left_arrow": "left",
    "right_arrow": "right",
    "solo": "solo",
    "mute": "mute",
    "arm": "arm",
    "jog_wheel": ["jog_wheel_up", "jog_wheel_down"],
}