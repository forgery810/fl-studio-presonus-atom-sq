import device
import channels
import midi
import ui
import mixer
# import general
import playlist
import transport
import patterns
import plugins
# import modes
from midi import *



# from modes import Modes
top_keys = [52, 53, 55, 56, 57, 59, 60, 62, 63, 64, 66, 67]
c_keys = [36, 43, 50]


class Lights():

	global step

	def __init__(self):
		print('self')
		self.indicator = 0
		self.step = 0
		# mode = Modes.mode
		# s = self.update_pattern()


	@staticmethod 	
	def update_pattern():							# reset leds in step mode 

		for i in range(0,16):
			if channels.getGridBit(channels.selectedChannel(), i) == 0:
				# print('0')
				device.midiOutMsg(144, 0, i + 36, 0)
					# event.handled = True
			elif channels.getGridBit(channels.selectedChannel(), i) == 1: 
				# print('1')
				device.midiOutMsg(144, 0, i + 36, 127)
				device.midiOutMsg(145, 0, i + 36, 0)
				# event.handled = True

	@staticmethod
	def update_second():							# light 2nd pattern in 32 step mode
		for i in range(16, 32):
			if channels.getGridBit(channels.selectedChannel(), i) == 0:
				print('0')
				device.midiOutMsg(144, 0, i + 36, 0)
					# event.handled = True
			elif channels.getGridBit(channels.selectedChannel(), i) == 1: 
				# print('1')
				device.midiOutMsg(144, 0, i + 36, 127)
				device.midiOutMsg(146, 0, i + 36, 0)
				# event.handled = True

	@staticmethod
	def light_pattern():
		for i in range(16, 32):
			device.midiOutMsg(144, 0, i + 36, 127)
		device.midiOutMsg(144, 0, patterns.patternNumber() + 52, 127)

	@staticmethod
	def light_pattern_two():
		for i in range(16, 32):
			device.midiOutMsg(144, 0, i + 36, 127)
		device.midiOutMsg(144, 0, patterns.patternNumber() + 52, 127)


		# else:
		# 	print('else')
		# 	for i in range(0,16):
		# 			device.midiOutMsg(144, 0, i + 36, 127)
		# 			device.midiOutMsg(145, 0, i + 36, 0)
		# 			device.midiOutMsg(144, 0, i + 52, 0)
		# 			device.midiOutMsg(146, 0, i + 52, 22)		
	@staticmethod
	def light_channels():
		print('light_channels')
		for i in range(0, channels.channelCount()):
			device.midiOutMsg(144, 0, 36 + i, 127)
			device.midiOutMsg(147, 0, 36 + i, 0)
		for x in range(channels.channelCount(), 16):
			device.midiOutMsg(144, 0, 36 + x, 127)	


	def active_step(self, data):
		if data == 2:
			self.step += 1
		if self.step >= patterns.getPatternLength(patterns.patternNumber()):
			self.step = 0
		# print('light note')
		Lights.update_pattern()
		device.midiOutMsg(144, 0, self.step + 36, 127)


	def keyboard_lights():
		for i in range(36, 52):
			device.midiOutMsg(144, 0, i, 127)

		for k in c_keys:
			device.midiOutMsg(145, 0, k, 0)

		for y in top_keys:
			device.midiOutMsg(144, 0, y, 127)

	def refresh(mode, submode):
		if mode == 1:
			Lights.update_pattern()

	def follow_beat(self):
		self.current_step(self.indicator)
		self.indicator += 1
		if self.indicator == patterns.getPatternLength(patterns.patternNumber())-1:
			self.indicator = 0


	def current_step(self, step):
		print(self.indicator)
		device.midiOutMsg(144, 0, self.indicator + 36, 127)




		




	def clear_pattern():							
		print('clear_pattern')
		# for i in range(0, 16):
		# 	device.midiOutMsg(144, 0, i + 36, 127)
		# 	device.midiOutMsg(145, 0, i + 36, 0)
		# for i in range(16, 32):
		# 	device.midiOutMsg(140, 0, i + 36, 127)
		# 	device.midiOutMsg(145, 0, i + 36, 0)
		for i in range(0,16):
			device.midiOutMsg(144, 0, i + 36, 127)
			device.midiOutMsg(145, 0, i + 36, 0)
			device.midiOutMsg(144, 0, i + 52, 127)
			device.midiOutMsg(146, 0, i + 52, 22)			


