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
import data

top_keys = [52, 53, 55, 56, 57, 59, 60, 62, 63, 64, 66, 67]
continuous_black = [37, 39, 42, 44, 46, 49, 51, 54, 56, 58, 61, 63, 66]
off_keys = (54, 58, 61, 65)
c_keys = [36, 43, 50]
c_keys_cont = [36, 48, 60]

class Lights():

	root_list = [36, 48, 60]

	def __init__(self):
		self.indicator = 0
		self.step = 0

	def lower_steps(color):
		"""takes in color and sends midi data to change lower row pads appropriate color"""
		for s in range(0, 16):
			if channels.getGridBit(channels.selectedChannel(), s) == 0:
				device.midiOutMsg(144, 0, s + 36, 0)						# turn step leds off
			elif channels.getGridBit(channels.selectedChannel(), s) == 1:
				device.midiOutMsg(144, 0, s + 36, 127)						# turn white first
				if color == 'blue':
					device.midiOutMsg(145, 0, s + 36, 0)
				elif color == 'yellow':
					device.midiOutMsg(147, 0, s + 36, 37)
				elif color == 'purple':
					device.midiOutMsg(146, 0, s + 36, 0)
				elif color == 'white':
					device.midiOutMsg(144, 0, s + 36, 0)
					device.midiOutMsg(144, 0, s + 36, 127)


	def upper_steps(color):
		"""takes in color and sends midi data to change upper row pads appropriate color"""
		for s in range(16, 32):
			if channels.getGridBit(channels.selectedChannel(), s) == 0:
				device.midiOutMsg(144, 0, s + 36, 0)						# turn step leds off
			elif channels.getGridBit(channels.selectedChannel(), s) == 1:
				device.midiOutMsg(144, 0, s + 36, 127)						# turn white first
				if color == 'blue':
					device.midiOutMsg(145, 0, s + 36, 0)
				elif color == 'yellow':
					device.midiOutMsg(147, 0, s + 36, 37)
				elif color == 'purple':
					device.midiOutMsg(146, 0, s + 36, 0)
				elif color == 'white':
					device.midiOutMsg(144, 0, s + 36, 127)


	def pattern_select():								
		"""lights top row white in pattern select mode"""
		for i in range(16, 32):
			device.midiOutMsg(144, 0, i + 36, 127)
		# device.midiOutMsg(144, 0, patterns.patternNumber() + 52, 127)

	def light_channels():
		for i in range(0, channels.channelCount()):
			device.midiOutMsg(144, 0, 36 + i, 127)
			device.midiOutMsg(146, 0, 36 + i, 0)
		for x in range(channels.channelCount(), 32):
			device.midiOutMsg(144, 0, x + 36, 0)

	def keyboard_lights():
		"""sets pad leds to keyboard layout. sets c notes blue"""
		for i in range(36, 52):
			device.midiOutMsg(144, 0, i, 127)

		for c in c_keys:
			device.midiOutMsg(145, 0, c, 0)

		for tk in top_keys:
			device.midiOutMsg(144, 0, tk, 127)

		for off in off_keys:
			device.midiOutMsg(144, 0, off, 0)

	def continuous_notes():
		"""sets all keys white except root notes which are set blue depending on current scale selected"""
		for z in range(36, 68):
			device.midiOutMsg(144, 0, z, 127)

		for rn in Lights.root_list:
			device.midiOutMsg(145, 0, rn, 0)

	def refresh(mode, submode):
		if mode == 1:
			Lights.update_pattern()

	def follow_beat(self, data):
		self.indicator += 2
		if self.indicator >= patterns.getPatternLength(patterns.patternNumber()) or data == 1:
			self.indicator = 0
		self.current_step(self.indicator)

	def current_step(self, step):
		device.midiOutMsg(144, 0, self.indicator + 36, 127)
		device.midiOutMsg(145, 1, self.indicator + 36 , 80)

	def clear_pattern():			
		"""sets bottom row blue and top row purple"""			
		for i in range(0,16):
			device.midiOutMsg(144, 0, i + 36, 127)
			device.midiOutMsg(145, 0, i + 36, 0)
			device.midiOutMsg(144, 0, i + 52, 127)
			device.midiOutMsg(146, 0, i + 52, 22)			


