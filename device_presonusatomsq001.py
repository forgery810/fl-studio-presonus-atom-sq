# name=Presonus Atom SQ
# Author: ts-forgery
# Version .01

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


one = 0
two = 0
three = 0
four = 0
i = 0 
step = 0
indicate = Lights()
# 144 white, 145 - red, 146 - green, 147 - blue - (36 - )

# def OnUpdateBeatIndicator(event):
# 	indicate.follow_beat()

# def OnUpdateBeatIndicator(data):
	# global step
	# # print(val)
	# # indicate.active_step(val)
	# if data < 3:
	# 	step += 2
	# if step >= patterns.getPatternLength(patterns.patternNumber()):
	# 	step = 0
	# # print('light note')
	# Lights.update_pattern()
	# device.midiOutMsg(144, 0, step + 36, 127)
	# device.midiOutMsg(124, 3, step + 36, 5)



def OnRefresh(ref_num):
	print(f"OnRefresh: {ref_num}")
	if ref_num == 65824:
		if Modes.mode == 1:
			Lights.update_pattern()
	# elif ref_num == 65831:
	# 	print('295')
	# 	if plugins.getPluginName(channels.selectedChannel()) == 'Slicex':
	# 		Lights.update_pattern() 


	# transport.setLoopMode()


def OnInit():
	print("Presonus Atom SQ")
	Lights.clear_pattern()
	one = 0
	two = 0
	three = 0
	four = 0

def OnMidiMsg(event):
	expedite = Expedite(event)

