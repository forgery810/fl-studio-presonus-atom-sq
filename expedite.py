
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
from buttons import Buttons
from notes import Notes
from knobs import Knobs
from lights import Lights
from midi2 import Midi2
from modes import Modes
import plugindata

class Expedite:

	def __init__(self, event):
		self.event = event
		self.triage() 

	def triage(self):
		if self.event.data1 in data.knob_list:
			print('in knobs')
			knob = Knobs(self.event)

		elif self.event.midiId == 144 and self.event.midiChanEx == 137:			# 137 selects for notes
			print('notes')
			notes = Notes(self.event)

		else:
			Buttons(self.event)



