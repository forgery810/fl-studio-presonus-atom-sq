# name=Presonus Atom SQ-dev
# Author: ts-forgery
# Version 0.6.4

import device
import mixer
import general
import transport
from midi import *
import midi
import data
import config
from notes import Notes
from lights import Lights
from modes import Modes
from expedite import Expedite

indicate = Lights()
md = Modes(Modes.e)

def OnUpdateBeatIndicator(data):
	Notes.update_beat(data)
	md.mode_init()

def OnIdle():
	if transport.isPlaying() == True and Modes.mode == 1 and config.options['follow_step']:
		md.mode_init()
		device.midiOutMsg(144, 0, mixer.getSongStepPos() + 36, 127)
		device.midiOutMsg(145, 1, mixer.getSongStepPos() + 36, 60)

def OnRefresh(ref_num):
	if ref_num == 1024:
		if Notes.accum_on:
			Notes.temp_reset_steps()
	elif ref_num == 256:
		indicate.indicator = 0
	md.mode_init()

def OnInit():
	print("Presonus Atom SQ - Version: 0.6.2")
	(f'Scripting API Version: {general.getVersion()}')
	Lights.clear_pattern()

def OnMidiMsg(event):
	expedite = Expedite(event)



