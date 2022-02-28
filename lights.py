import device
import channels
import midi
import ui
import mixer
import playlist
import transport
import patterns
import plugins
from midi import *

top_keys = [52, 53, 55, 56, 57, 59, 60, 62, 63, 64, 66, 67]
continuous_black = [37, 39, 42, 44, 46, 49, 51, 54, 56, 58, 61, 63, 66]
off_keys = (54, 58, 61, 65)
c_keys = [36, 43, 50]
c_keys_cont = [36, 48, 60]

class Lights():

	def __init__(self):
		self.indicator = 0
		self.step = 0

	@staticmethod 	
	def update_pattern(mode):							# reset leds in step mode 
		for i in range(0,16):
			if channels.getGridBit(channels.selectedChannel(), i) == 0:
				device.midiOutMsg(144, 0, i + 36, 0)
			elif channels.getGridBit(channels.selectedChannel(), i) == 1: 
				device.midiOutMsg(144, 0, i + 36, 127)
				if mode == 'accum':
					device.midiOutMsg(147, 0, i + 36, 37)
				elif mode != 1:
					device.midiOutMsg(145, 0, i + 36, 0)


	@staticmethod
	def update_second(mode):							# light 2nd pattern in 32 step mode
		for i in range(16, 32):
			if channels.getGridBit(channels.selectedChannel(), i) == 0:
				# print('0')
				device.midiOutMsg(144, 0, i + 36, 0)
					# event.handled = True
			elif channels.getGridBit(channels.selectedChannel(), i) == 1: 
				# print('1')
				device.midiOutMsg(144, 0, i + 36, 127)
				if mode == 'accum' :
					print('in accum lights')
					device.midiOutMsg(147, 0, i + 36, 37)
				elif mode != 1:
					device.midiOutMsg(146, 0, i + 36, 0)

	@staticmethod
	def pattern_select():								# Lights Top row white in pattern select mode
		print('Lights: Light Pattern Select')
		for i in range(16, 32):
			device.midiOutMsg(144, 0, i + 36, 127)
		# device.midiOutMsg(144, 0, patterns.patternNumber() + 52, 127)

	@staticmethod
	def light_pattern_two():
		print('Lights: light_pattern_two')
		for i in range(16, 32):
			device.midiOutMsg(144, 0, i + 36, 127)
		device.midiOutMsg(144, 0, patterns.patternNumber() + 52, 127)

	@staticmethod
	def light_channels():
		print('light_channels')
		for i in range(0, channels.channelCount()):
			device.midiOutMsg(144, 0, 36 + i, 127)
			device.midiOutMsg(146, 0, 36 + i, 0)
		for x in range(channels.channelCount(), 32):
			device.midiOutMsg(144, 0, x + 36, 0)

	def keyboard_lights():
		print('Lights: keyboard_lights')
		for i in range(36, 52):
			device.midiOutMsg(144, 0, i, 127)

		for c in c_keys:
			device.midiOutMsg(145, 0, c, 0)

		for tk in top_keys:
			device.midiOutMsg(144, 0, tk, 127)

		for off in off_keys:
			device.midiOutMsg(144, 0, off, 0)

	def continuous_notes():
		print('continuous_notes')
		for z in range(36, 68):
			device.midiOutMsg(144, 0, z, 127)

		# for b in continuous_black:					# adding this code will change black keys to be light blue in continuous mode
		# 	device.midiOutMsg(145, 1, b, 80)

		for ck in c_keys_cont:
			device.midiOutMsg(145, 0, ck, 0)


	def refresh(mode, submode):
		print('Lights: refresh')
		if mode == 1:
			Lights.update_pattern()

	def follow_beat(self):
		print('Lights: follow_beat')
		self.current_step(self.indicator)
		self.indicator += 1
		if self.indicator == patterns.getPatternLength(patterns.patternNumber())-1:
			self.indicator = 0

	def current_step(self, step):
		print('Lights: current_step')
		print(self.indicator)
		device.midiOutMsg(144, 0, self.indicator + 36, 127)


	def clear_pattern():							
		# print('Lights: clear_pattern')
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


