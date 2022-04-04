import device
import channels
import midi
import ui
import mixer
import playlist
import transport
import channels
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

	colors = {'purple': 146, 'white': 144, 'yellow': 127, 'blue': 145, }
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
				elif color == 'light_blue':
					device.midiOutMsg(145, 0, s + 36, 66)

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
				elif color == 'light_blue':
					print('light_blue')
					device.midiOutMsg(145, 0, s + 36, 66)

	def pattern_select():	
		"""lights top row white in pattern access mode"""

		for i in range(16, 32):
			device.midiOutMsg(144, 0, i + 36, 127)

	def active_pattern(pattern_num):
		"""light active pattern in pattern access mode"""

		device.midiOutMsg(146, 0, pattern_num + 52, 127)

	def channel_select(color):
		"""lights top row leds according to color sent"""

		for led in range(16, 16 + Lights.get_channel_count(16)):
			device.midiOutMsg(144, 0, led + 36, 127)						# turn white first
			if color == 'light_purple':
				device.midiOutMsg(146, 2, led + 36, 60)
			elif color == 'white':
				pass
			elif color == 'yellow':
				device.midiOutMsg(147, 0, led + 36, 60)	

	def muted_channels():
		"""lights muted and unmuted channels accordingly in channel mute mode"""

		Lights.pattern_select()
		for l in range(52, 52 + Lights.get_channel_count(16)):
			if not channels.isChannelMuted(l - 52):
				device.midiOutMsg(147, 0, l, 23)
 
	def light_channels():
		"""lights channels for pad per channel mode"""

		for i in range(0, Lights.get_channel_count(32)):
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


	def get_channel_count(limit):
		channel_count = channels.channelCount()
		if channel_count > limit:
			return limit
		else:
			return channel_count