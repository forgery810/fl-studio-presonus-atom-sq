# name=Presonus Atom SQ
# Author: ts-forgery
# Version 0.5.1

import arrangement
import device
import ui
import channels
import mixer
import general
import playlist
import transport
import patterns
import plugins
import modes
from midi import *
import midi
import data
from notes import Notes
from knobs import Knobs
from lights import Lights


from modes import Modes
from expedite import Expedite
import plugindata


step = 0
indicate = Lights()


def OnUpdateBeatIndicator(data):

	Notes.update_beat(data)
	# print(data)

	# print(data) 
# 	# indicate.active_step(val)
# 	if data < 3:
# 		step += 2
# 	if step >= patterns.getPatternLength(patterns.patternNumber()):
# 		step = 0  
# 	# print('light note')
# 	Lights.update_pattern()
# 	Lights.update_second()
# 	device.midiOutMsg(144, 0, step + 36, 127)
# 	device.midiOutMsg(124, 3, step + 36, 5)

def OnRefresh(ref_num):
	print(f"OnRefresh: {ref_num}")

	if ref_num == 1024:
		if Notes.accum_on:
			Notes.temp_reset_steps()


	if ref_num == 65824 or ref_num == 1024:
		# if Modes.mode == 1:
		# 	Lights.update_pattern(Modes.step_iter)
		# 	if Modes.step_iter == 0:
		# 		Lights.update_second(Modes.step_iter)


		if Modes.mode == 1:							# Step Entry
			if Modes.sub_sub_step_iter == 2:
				Lights.update_pattern('accum')
				if Modes.step_iter != 2:
					Lights.update_second('accum')
				else:
					Lights.pattern_select()
			else:
				Lights.update_pattern(Modes.step_iter)
				if Modes.step_iter == 0 or Modes.step_iter == 1:			# check if in 32 step (0) or parameter entry modes
					Lights.update_second(Modes.step_iter)									# light steps 17-32

				elif Modes.step_iter == 2:									# check if pattern select mode
					print('refresh pattern_select lightsS')
					Lights.pattern_select()									# light top row as currently selected pattern


	# elif ref_num == 65831:
	# 	print('295')
	# 	if plugins.getPluginName(channels.selectedChannel()) == 'Slicex':
	# 		Lights.update_pattern() 

def OnInit():
	print("Presonus Atom SQ COPY")
	Lights.clear_pattern()

def OnMidiMsg(event):
	expedite = Expedite(event)

# def OnPitchBend(event):
# 	pass
	

