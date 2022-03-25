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

def OnUpdateBeatIndicator(data):
	"""called by Fl on every beat/bar"""

	Notes.update_beat(data)
	Modes.mode_init()

def OnIdle():
	"""called by FL whether or not in play"""

	if transport.isPlaying() == True and Modes.mode == 1 and config.options['follow_step']:
		Modes.mode_init()
		device.midiOutMsg(144, 0, mixer.getSongStepPos() + 36, 127)
		device.midiOutMsg(145, 1, mixer.getSongStepPos() + 36, 60)

def OnRefresh(ref_num):
	"""called by FL when any change is made to the program. with mouse, keyboard, controller etc"""

	if ref_num == 1024:
		if Notes.accum_on:
			Notes.temp_reset_steps()
	elif ref_num == 256:
		indicate.indicator = 0
	Modes.mode_init()

def OnInit():
	"""called when FL connects with controller"""

	print("Presonus Atom SQ - Version: 0.6.4")
	print(f'Scripting API Version: {general.getVersion()}')
	Lights.clear_pattern()

def OnMidiMsg(event):
	"""called by FL everytime a MIDI message is sent by controller"""

	expedite = Expedite(event)



