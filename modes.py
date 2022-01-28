import ui
import patterns
import channels
import device
from lights import Lights

class Modes:
	mode = 0
	step_iter = 0

	def __init__(self, event):
		self.event = event
		self.mode_selected = ['Notes', 'Step Entry', 'Pads per Channel']
		self.step_submodes = ['32 Step', 'Parameter Entry', 'Pattern Access', 'Random Notes']
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
		print('mode_init')
		if Modes.mode == 0:
			Lights.keyboard_lights()
			# Lights.clear_pattern()
			print('mode 0')
		elif Modes.mode == 1:
			Lights.update_pattern()
			if Modes.step_iter == 0 or Modes.step_iter == 1:			# check if in 32 step (0) or parameter entry modes
				Lights.update_second()									# light steps 17-32
			elif Modes.step_iter == 2:									# check if pattern select mode
				Lights.light_pattern()									# light top row as currently selected pattern

		elif Modes.mode == 2:							
			Lights.light_channels()										# light channels for channel play mode

	def sub_mode(self):
		if Modes.mode == 1:
			Modes.step_iter += 1

			if Modes.step_iter >= len(self.step_submodes):
				Modes.step_iter = 0
			print(self.step_submodes[self.step_iter])
			ui.setHintMsg(self.step_submodes[self.step_iter])
		self.mode_init()



	# @staticmethod 
	# def get_submode():
	# 	return Modes.submode

