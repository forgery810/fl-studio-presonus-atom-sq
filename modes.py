import ui
import patterns
import channels
import device
from lights import Lights

class Modes:

	mode = 0
	step_iter = 0
	note_iter = 0
	step_sub_iter = 0
	sub_sub_key_iter = 3
	sub_sub_step_iter = 0
	octave_values = (-36, -24, -12, 0, 12, 24, 36)

	def __init__(self, event):
		self.event = event
		self.mode_selected = ['Notes', 'Step Sequencer', 'Pad per Channel']
		self.step_sub_sub = ['Standard', 'Random Notes', 'Accumulator']
		self.step_submodes = ['32 Step', 'Parameter Entry', 'Pattern Access']
		self.note_submodes = ['Keyboard', 'Continuous' ]
		self.octave_names = ['-3', '-2', '-1', '0', '1', '2', '3']
		self.continuous_modes = ['Play Notes', 'Set Notes']
		

	def mode_change(self):
		# Modes.step_iter = 0
		# Modes.note_iter = 0
		Modes.mode += 1
		Modes.step_iter = 0        # reset iter to zero when mode changes
		Modes.sub_sub_step_iter = 0
		if Modes.mode >= len(self.mode_selected):
			Modes.mode = 0
		self.mode_init()
		ui.setHintMsg(self.mode_selected[Modes.mode])
		print(self.mode_selected[Modes.mode])
		self.event.handled == True
	
	def mode_init(self):
		if Modes.mode == self.mode_selected.index('Notes'):								# Keyboard
			if Modes.note_iter == 0:
				Lights.keyboard_lights()
			elif Modes.note_iter == 1:
				Lights.continuous_notes()

		elif Modes.mode == self.mode_selected.index('Step Sequencer'):							# Step Entry
			print(f'step sub iter: {Modes.sub_sub_step_iter}')
			if Modes.sub_sub_step_iter == 2:
				Lights.update_pattern('accum')
				print(f'step_iter: {self.step_iter}')
				if self.step_iter == 2:
					print('mode_init pattern select')
					Lights.pattern_select()
				else:
					print('mode_int 2nd accum')
					Lights.update_second('accum')
			else:
				Lights.update_pattern(Modes.step_iter)
				if Modes.step_iter == 0 or Modes.step_iter == 1:			# check if in 32 step (0) or parameter entry modes
					Lights.update_second(Modes.step_iter)									# light steps 17-32

				elif Modes.step_iter == 2:									# check if pattern select mode
					Lights.pattern_select()									# light top row as currently selected pattern

		elif Modes.mode == self.mode_selected.index('Pad per Channel'):							# Pad per Channel
			Lights.light_channels()										# light channels for channel play mode

	def sub_mode(self):
		Modes.sub_sub_step_iter = 0   # reset sub sub mode to zero when sub mode changes
		if Modes.mode == 1:
			Modes.step_iter += 1
			if Modes.step_iter >= len(self.step_submodes):
				Modes.step_iter = 0
			print(self.step_submodes[self.step_iter])
			ui.setHintMsg(self.step_submodes[self.step_iter])
			self.mode_init()

		elif Modes.mode == 0:
			Modes.note_iter += 1
			if Modes.note_iter >= len(self.note_submodes):
				Modes.note_iter = 0
			print(self.note_submodes[self.note_iter])
			ui.setHintMsg(self.note_submodes[self.note_iter])
			self.mode_init()

	def sub_sub_mode(self):
		if Modes.mode == 0:
			if Modes.note_iter == 0:   				# check if in keyboard mode
				Modes.sub_sub_key_iter += 1
				if Modes.sub_sub_key_iter >= len(self.octave_names):
					Modes.sub_sub_key_iter = 0
				ui.setHintMsg(self.octave_names[Modes.sub_sub_key_iter])
				print(self.octave_names[Modes.sub_sub_key_iter])
				self.mode_init()

			elif Modes.note_iter == 1:				# continuous mode
				Modes.step_sub_iter += 1 								
				if Modes.step_sub_iter >= len(self.continuous_modes):
					Modes.step_sub_key_iter = 0
				ui.setHintMsg(self.continuous_modes[Modes.step_sub_iter])
				print(self.continuous_modes[Modes.step_sub_iter])
				self.mode_init()

		elif Modes.mode == 1:							# check if in step mode
			if Modes.step_iter != 1:
				Modes.sub_sub_step_iter += 1
				if Modes.sub_sub_step_iter >= len(self.step_sub_sub):
					Modes.sub_sub_step_iter = 0
				ui.setHintMsg(self.step_sub_sub[Modes.sub_sub_step_iter])
				self.mode_init()

	@staticmethod
	def call_init():
		self.mode_init(self)

	def get_octave(self):
		return self.octave_values[Modes.sub_sub_key_iter]


	# def plus_minus(self):
	# 	print('plusminus')
