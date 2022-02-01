import ui
import patterns
import channels
import device
from lights import Lights

class Modes:
	mode = 0
	step_iter = 0
	note_iter = 0

	def __init__(self, event):
		self.event = event
		self.mode_selected = ['Notes', 'Step Entry', 'Pad per Channel']
		self.step_submodes = ['32 Step', 'Parameter Entry', 'Pattern Access', 'Random Notes']
		self.note_submodes = ['Continuous', 'Keyboard']
		submode = self.step_submodes

	def mode_change(self):
		Modes.mode += 1
		if Modes.mode >= len(self.mode_selected):
			Modes.mode = 0
		self.mode_init()
		ui.setHintMsg(self.mode_selected[Modes.mode])
		print(self.mode_selected[Modes.mode])
		self.event.handled == True

	def mode_init(self):
		if Modes.mode == 0:								# Notes
			if Modes.note_iter == 0:
				Lights.continuous_notes()
			elif Modes.note_iter == 1:
				Lights.keyboard_lights()

		elif Modes.mode == 1:							# Step Entry
			Lights.update_pattern()
			if Modes.step_iter == 0 or Modes.step_iter == 1:			# check if in 32 step (0) or parameter entry modes
				Lights.update_second()									# light steps 17-32
			elif Modes.step_iter == 2:									# check if pattern select mode
				Lights.light_pattern()									# light top row as currently selected pattern

		elif Modes.mode == 2:							# Pad per Channel
			Lights.light_channels()										# light channels for channel play mode

	def sub_mode(self):
		if Modes.mode == 1:
			Modes.step_iter += 1

			if Modes.step_iter >= len(self.step_submodes):
				Modes.step_iter = 0
			print(self.step_submodes[self.step_iter])
			ui.setHintMsg(self.step_submodes[self.step_iter])

		elif Modes.mode == 0:
			Modes.note_iter += 1
			if Modes.note_iter >= len(self.note_submodes):
				Modes.note_iter = 0
			print(self.note_submodes[self.note_iter])
			ui.setHintMsg(self.note_submodes[self.note_iter])

		self.mode_init()

