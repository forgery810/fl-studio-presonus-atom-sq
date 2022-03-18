import ui
import patterns
import channels
import device
from lights import Lights
import data

class Modes:

	mode = 0
	step_iter = 0
	note_iter = 0
	step_sub_iter = 0
	sub_sub_key_iter = 3
	sub_sub_step_iter = 0
	octave_values = (-36, -24, -12, 0, 12, 24, 36)
	root_iter = 0
	scale_iter = 0
	e = None

	def __init__(self, event):
		self.event = event
		Modes.e = self.event
		self.mode_selected = ['Notes', 'Step Sequencer', 'Pad per Channel']
		self.step_sub_sub = ['Standard',  'Parameter Entry', 'Random Notes', 'Accumulator']
		self.step_submodes = ['32 Step', 'Pattern Access']
		self.note_submodes = ['Keyboard', 'Continuous']
		self.octave_names = ['-3', '-2', '-1', '0', '1', '2', '3']
		self.continuous_modes = ['Play Notes', 'Set Scale']
		
	def mode_change(self):
		"""increments through major modes"""
		Modes.mode += 1
		Modes.step_iter = 0        # reset iter to zero when mode changes
		Modes.sub_sub_step_iter = 0
		if Modes.mode >= len(self.mode_selected):
			Modes.mode = 0
		self.mode_init()
		ui.setHintMsg(self.mode_selected[Modes.mode])
		self.event.handled == True

	def mode_init(self):			
		"""Determines lighting based on what modes are active. Calls appropriate Light() method"""
		if Modes.mode == self.mode_selected.index('Notes'):								# Keyboard
			if Modes.note_iter == 0:
				Lights.keyboard_lights()
			elif Modes.note_iter == 1:
				Lights.continuous_notes()

		elif Modes.mode == self.mode_selected.index('Step Sequencer'):							# Step Entry

			if self.step_sub_sub[Modes.sub_sub_step_iter] == 'Parameter Entry':				# parameter entry
				Lights.lower_steps('white')
				if self.step_iter == 1:
					Lights.pattern_select()
				else:
					Lights.upper_steps('white')

			elif self.step_sub_sub[Modes.sub_sub_step_iter] == 'Accumulator':							# accumulator
				Lights.lower_steps('yellow')
				if self.step_iter == 1:
					Lights.pattern_select()
				else:
					Lights.upper_steps('yellow')

			elif self.step_sub_sub[Modes.sub_sub_step_iter] == 'Random Notes':							# random
				Lights.lower_steps('purple')
				if self.step_iter == 1:
					Lights.pattern_select()
				else:
					Lights.upper_steps('purple')

			elif self.step_sub_sub[Modes.sub_sub_step_iter] == 'Standard':														# standard
				Lights.lower_steps('blue')
				if Modes.step_iter == 0:						# check if in 32 step (0) or parameter entry modes
					Lights.upper_steps('blue')
				elif Modes.step_iter == 1:									# check if pattern select mode
					Lights.pattern_select()									# light top row as currently selected pattern

		elif Modes.mode == self.mode_selected.index('Pad per Channel'):							# Pad per Channel
			Lights.light_channels()										# light channels for channel play mode

	def sub_mode(self):
		"""iterates through submodes"""
		Modes.sub_sub_step_iter = 0   # reset sub sub mode to zero when sub mode changes

		if Modes.mode == 1:
			Modes.step_iter += 1
			if Modes.step_iter >= len(self.step_submodes):
				Modes.step_iter = 0
			ui.setHintMsg(self.step_submodes[self.step_iter])
			self.mode_init()

		elif Modes.mode == 0:
			Modes.note_iter += 1
			if Modes.note_iter >= len(self.note_submodes):
				Modes.note_iter = 0
			ui.setHintMsg(self.note_submodes[self.note_iter])
			self.mode_init()

	def sub_sub_mode(self, increment):
		"""increments through various sub sub modes, increment variable dictates by how much"""

		if Modes.mode == 0:
			if Modes.note_iter == 0:   				# check if in keyboard mode
				Modes.sub_sub_key_iter += increment
				if Modes.sub_sub_key_iter >= len(self.octave_names):
					Modes.sub_sub_key_iter = 0
				elif Modes.sub_sub_key_iter < 0:
					Modes.sub_sub_key_iter = len(self.octave_names) - 1
				ui.setHintMsg(self.octave_names[Modes.sub_sub_key_iter])
				self.mode_init()

			elif Modes.note_iter == 1:				# continuous mode
				Lights.root_list.clear()
				if increment == 1:
					Modes.root_iter += 1
					if Modes.root_iter >= len(data.notes_list):
						Modes.root_iter = 0
					ui.setHintMsg(f'Root Note: {data.notes_list[Modes.root_iter]}')

				elif increment == -1:
					Modes.scale_iter += 1
					if Modes.scale_iter >= len(data.scale_names):
						Modes.scale_iter = 0
					ui.setHintMsg(f'Scale: {data.scale_names[Modes.scale_iter]}')
				self.get_roots()
				self.mode_init()

		elif Modes.mode == 1:							# check if in step mode
			Modes.sub_sub_step_iter += increment
			if Modes.sub_sub_step_iter >= len(self.step_sub_sub):
				Modes.sub_sub_step_iter = 0
			elif Modes.sub_sub_step_iter < 0:
				Modes.sub_sub_step_iter = len(self.step_sub_sub) - 1
			ui.setHintMsg(self.step_sub_sub[Modes.sub_sub_step_iter])
			self.mode_init()

	def get_roots(self):
		"""finds root notes to set blue for currently selected scale and adds to list for Lights function to use
			C is 0 and root_iter that is used to increment through root options is used as offset for other notes"""
		for note in data.scales[Modes.scale_iter][Modes.root_iter][12:44]:
			for c in data.cs:
				if note == c + Modes.root_iter:
						Lights.root_list.append(data.scales[Modes.scale_iter][Modes.root_iter].index(note)+24)

	def get_octave(self):
		return self.octave_values[Modes.sub_sub_key_iter]

