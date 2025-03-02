# name=Presonus Atom SQ - ATM SQ
# Author: ts-forgery
VERSION = '1.0'

import mixer
import general
import transport
import config
from lights import Lights
import modes
from handler import MidiHandler
import midi_mapping
import action
from modes import ModeManager, MainMode, NoteSubmode
import state
import patterns

lights = Lights()
state = state.State()
mode_manager = ModeManager(lights, state)
encoder_action = action.EncoderAction(mode_manager, state)
action = action.Action(mode_manager, state)

def OnInit():
	"""called when FL connects with controller"""
	print(f"Presonus Atom SQ - Version: {VERSION}")
	print(f'Scripting API Version: {general.getVersion()}')
	mode_manager.set_mode(modes.MainMode.NOTES)
	state.set_plus_minus_leds()

def OnRefresh(ref_num):
	"""called by FL when any change is made to the program. with mouse, keyboard, controller etc"""
	# print(f"OnRefresh: {ref_num}")
	mode_manager.refresh_leds()
	if ref_num == 65824:
		state.channel_index = -1

def OnMidiMsg(event):
	"""called by FL everytime a MIDI message is sent by controller"""
	print(event.midiId, event.data1, event.data2, event.midiChanEx, event.midiChan)
	handler = MidiHandler(event, midi_mapping.controller, mode_manager, action, lights, encoder_action, state)

def check_for_pattern_change():
	if state.current_pattern != state.next_pattern:
		patterns.jumpToPattern(state.next_pattern)
		state.current_pattern = state.next_pattern

if mode_manager.get_layout() == 'PATTERN_ACCESS' or config.LIGHT_CURRENT_STEP:
	def OnIdle():
		"""called by FL whether or not in play mode"""

		if transport.isPlaying():
			if mode_manager.get_mode() == modes.MainMode.STEP_SEQUENCER and config.LIGHT_CURRENT_STEP:
				mode_manager.current_mode.layout.update_active_step(lights)
			if mode_manager.get_layout() == 'PATTERN_ACCESS' and state.current_pattern != state.next_pattern:
				if patterns.getPatternLength(patterns.patternNumber()) - 1 == mixer.getSongStepPos():
					patterns.jumpToPattern(state.next_pattern)
					state.current_pattern = state.next_pattern

