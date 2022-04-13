# name=Presonus Atom SQ-dev
# Author: ts-forgery
# Version 0.7.5
VERSION = '0.7.5-dev'

import device
import mixer
import general
import patterns
import transport
from midi import *
import midi
import data
import config
from notes import Notes, Shifter
from lights import Lights
from modes import Modes
from expedite import Expedite


indicate = Lights()
alt = Shifter()
current_pattern = 0

class Steps:
	"""this class makes sure functions that rely on current step/bar to be called are only called once
		when those conditions are met"""

	shift_called = False
	bar_iter = 0

	def call_shift(self):
		if Steps.shift_called == False:
			alt.shift_patterns()
			if Notes.accum_on:
				Notes.update_beat()
		Steps.shift_called = True

	def reset_shift(self):
		Steps.shift_called = False

	def bar_count(self):
		Steps.bar_iter += 1

	def reset_bar_count(self):
		Steps.bar_iter = 0

def OnUpdateBeatIndicator(data):
	"""called by Fl on every beat/bar"""

	steps = Steps()

	# print(transport.getSongPos(2))

	Modes.mode_init()
	if data == 1:
		# print(patterns.getPatternLength(patterns.patternNumber()))
		if patterns.getPatternLength(patterns.patternNumber()) < 32:
			# print(f'mixer step: {mixer.getSongStepPos()}')
			# current_pattern = patterns.patternNumber()
			steps.call_shift()
			steps.reset_shift()
		elif patterns.getPatternLength(patterns.patternNumber()) >= 32:
			steps.bar_count()
			if steps.bar_iter == 2:
				steps.call_shift()
				steps.reset_shift()
				steps.reset_bar_count()

def OnIdle():
	"""called by FL whether or not in play"""

	if transport.isPlaying() == True and Modes.mode == 1 and config.options['follow_step']:
		Modes.mode_init()
		device.midiOutMsg(144, 0, get_led_step(), 127)
		device.midiOutMsg(145, 1, get_led_step(), 60)

	# if transport.isPlaying() and mixer.getSongStepPos() == patterns.getPatternLength(patterns.patternNumber())-1:
	# 	# alt = Shifter()
	# 	steps.call_shift()
	# 	Steps.shift_called = True

	# if transport.isPlaying and mixer.getSongStepPos() == 0:
	# 	steps.reset_shift()

def OnRefresh(ref_num):
	"""called by FL when any change is made to the program. with mouse, keyboard, controller etc"""
	# print(ref_num)

	s = Steps()

	# if ref_num == 1024 and current_pattern != patterns.patternNumber():
	# 	if Notes.accum_on:
	# 		Notes.temp_reset_steps()

	if ref_num == 256:
		indicate.indicator = 0
		s.reset_bar_count()

	Modes.mode_init()

def OnInit():
	"""called when FL connects with controller"""

	print(f"Presonus Atom SQ - Version: {VERSION}")
	print(f'Scripting API Version: {general.getVersion()}')
	Lights.clear_pattern()

def OnMidiMsg(event):
	"""called by FL everytime a MIDI message is sent by controller"""

	expedite = Expedite(event)

def get_led_step():
	""" Looks up current step and sets offset for atom led pad. Prevents led step lights above 32 steps""" 

	offset = 36 + mixer.getSongStepPos() 
	if mixer.getSongStepPos() > 31:
		offset = 0
	return offset
	