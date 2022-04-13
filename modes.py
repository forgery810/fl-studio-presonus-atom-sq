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
	octave_iter = 3
	sub_step_iter = 0
	channels_iter = 0
	root_iter = 0
	scale_iter = 0
	alter_iter = 0 
	octave_values = (-36, -24, -12, 0, 12, 24, 36)

	mode_selected = ['Notes', 'Step Sequencer', 'Pad per Channel', 'Alter']
	step_sub_names = ['Standard',  'Parameter Entry', 'Random Notes']
	step_layouts = ['32 Step', 'Pattern Access', 'Channel Select', 'Channel Mute', 'Step Select']
	note_layouts = ['Keyboard', 'Continuous']
	alter_submodes = ['Shifter', "Accumulator"]
	shifter_options = ['Left', ' Right', 'Invert', 'Clear']

	octave_names = ['-3', '-2', '-1', '0', '1', '2', '3']
	continuous_modes = ['Play Notes', 'Set Scale']

	def __init__(self, event):
		self.event = event
		
	def mode_change(self):
		"""increments through major modes"""

		Modes.mode += 1
		Modes.step_iter = 0        # reset iter to zero when mode changes
		Modes.sub_step_iter = 0
		if Modes.mode >= len(Modes.mode_selected):
			Modes.mode = 0
		Modes.mode_init()
		ui.setHintMsg(Modes.mode_selected[Modes.mode])

	def mode_init():			
		"""Determines lighting based on what modes are active. Calls appropriate Light() method"""

		if Modes.mode == Modes.mode_selected.index('Notes'):								
			if Modes.note_iter == 0:
				Lights.keyboard_lights()
			elif Modes.note_iter == 1:
				Lights.continuous_notes()

		elif Modes.mode == Modes.mode_selected.index('Step Sequencer'):							

			if Modes.step_layouts[Modes.step_iter] == 'Channel Select':
				Lights.channel_select('light_purple')
				Lights.active_channel(channels.channelNumber())

			elif Modes.step_layouts[Modes.step_iter] == 'Channel Mute':
				Lights.muted_channels()
				

			elif Modes.step_layouts[Modes.step_iter] == 'Pattern Access':
				Lights.pattern_select()
				Lights.active_pattern(patterns.patternNumber())

			elif Modes.step_layouts[Modes.step_iter] == "Step Select":
				Lights.step_select_lights()

			if Modes.step_sub_names[Modes.sub_step_iter] == 'Parameter Entry':				
				Lights.lower_steps('white')
				if Modes.step_iter == 0:
					Lights.upper_steps('white')

			elif Modes.step_sub_names[Modes.sub_step_iter] == 'Random Notes':							# random
				Lights.lower_steps('purple')
				if Modes.step_iter == 0:
					Lights.upper_steps('purple')

			elif Modes.step_sub_names[Modes.sub_step_iter] == 'Standard':														# standard
				Lights.lower_steps('blue')
				if Modes.step_iter == 0:						# check if in 32 step (0) or parameter entry modes
					Lights.upper_steps('blue')

		elif Modes.mode == Modes.mode_selected.index('Pad per Channel'):							# Pad per Channel
			Lights.light_channels()										# light channels for channel play mode

		elif Modes.mode == Modes.mode_selected.index('Alter'):							# Shifter
			if Modes.alter_submodes[Modes.alter_iter] == 'Shifter':
				Lights.lower_steps('light_blue')
				Lights.upper_steps('light_blue')

			elif Modes.alter_submodes[Modes.alter_iter] == 'Accumulator':							# accumulator
				Lights.lower_steps('yellow')
				if Modes.step_iter == 0:
					Lights.upper_steps('yellow')

	def rotate_layout(self):			# formally def sub_mode(self)
		"""iterates through second level of modes - submodes"""

		Modes.sub_step_iter = 0   									# reset sub sub mode to zero when sub mode changes

		if Modes.mode == 1:
			Modes.step_iter += 1
			if Modes.step_iter >= len(Modes.step_layouts):
				Modes.step_iter = 0
			ui.setHintMsg(Modes.step_layouts[Modes.step_iter])
			Modes.mode_init()

		elif Modes.mode == 0:
			Modes.note_iter += 1
			if Modes.note_iter >= len(Modes.note_layouts):
				Modes.note_iter = 0
			ui.setHintMsg(Modes.note_layouts[Modes.note_iter])
			Modes.mode_init()

	def sub_mode(self, increment):					# formally sub_sub_mode
		"""increments through various sub sub modes, increment variable dictates by how much"""

		if Modes.mode == 0:
			if Modes.note_iter == 0:   										# check if in keyboard mode
				Modes.octave_iter += increment
				if Modes.octave_iter >= len(Modes.octave_names):
					Modes.octave_iter = 0
				elif Modes.octave_iter < 0:
					Modes.octave_iter = len(Modes.octave_names) - 1
				ui.setHintMsg(Modes.octave_names[Modes.octave_iter])
				Modes.mode_init()

			elif Modes.note_iter == 1:										# continuous mode
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
				Modes.get_roots()
				Modes.mode_init()

		elif Modes.mode == 1:												# check if in step mode
			Modes.sub_step_iter += increment
			if Modes.sub_step_iter >= len(Modes.step_sub_names):
				Modes.sub_step_iter = 0
			elif Modes.sub_step_iter < 0:
				Modes.sub_step_iter = len(Modes.step_sub_names) - 1
			ui.setHintMsg(Modes.step_sub_names[Modes.sub_step_iter])
			Modes.mode_init()

		elif Modes.mode == 3:												# check if in Alter Mode
			Modes.alter_iter += increment
			if Modes.alter_iter >= len(Modes.alter_submodes):
				Modes.alter_iter = 0
			elif Modes.alter_iter < 0:
				Modes.alter_iter = len(Modes.alter_submodes) - 1
			ui.setHintMsg(Modes.alter_submodes[Modes.alter_iter])
			Modes.mode_init()

	def get_roots():
		"""finds root notes to set blue for currently selected scale and adds to list for Lights function to use
			C is 0 and root_iter that is used to increment through root options is used as offset for other notes"""

		for note in data.scales[Modes.scale_iter][Modes.root_iter][12:44]:
			for c in data.cs:
				if note == c + Modes.root_iter:
						Lights.root_list.append(data.scales[Modes.scale_iter][Modes.root_iter].index(note)+24)

	def get_octave():
		return Modes.octave_values[Modes.octave_iter]

	def get_step_submode():
		return Modes.sub_step_iter

	def get_alter_mode():
		return Modes.alter_iter

	def get_mode():
		print(f'get_mode = {Modes.mode}')
		return Modes.mode

