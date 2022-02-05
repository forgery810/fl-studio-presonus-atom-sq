import modes
from midi import *
import midi
import data
from buttons import Buttons
from notes import Notes
from knobs import Knobs
from modes import Modes

class Expedite:

	def __init__(self, event):
		self.event = event
		self.triage() 

	def triage(self):
		print(self.event.midiId, self.event.data1, self.event.data2, self.event.midiChanEx)

		if self.event.data1 in data.knob_list and self.event.midiChanEx in range(128, 131):
			print('in knobs')
			if self.event.data1 == 1:
				Buttons.touchpad_value = self.event.data2
			knob = Knobs(self.event)

		elif self.event.midiChanEx == 137:			# 137 selects for notes
			print('notes')
			notes = Notes(self.event)

		else:
			Buttons(self.event)



