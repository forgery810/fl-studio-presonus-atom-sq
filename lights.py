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




# lights 30-40, 0, 83 top row off

#lue green
# if white (145, 0, x, 0-127) == turquoise 0 bright - 127 white
# if white ( 146 " "     "  ) == purple
# "			147		"         == yellow
# if any color
 # (144, x, x, 0) == off




# device.midiOutMsg(144, 0, 2, 127) - turned step 66 red
	# device.midiOutMsg(144, 0, 0, 127) - turned + blue


	"""
36, 0, 0, 0 = step one purple if light blue in intial mode
		else turns these buttons off

36,1, 0, 0 every second button off

52, 59, 0, 0 = step ~12b off
0, 1, 0, 0 = - button off
0, 15 or 16, 0 , 0 = + button off
0, 0, 127, 0 = turns + turquiose if going up?
51, 2, 0, 0 = step 16 off if white
47, 2, 0, 0 = step 12 off if white
if x, y, 0, 0 x = step number, if y =0 every step is turned off, if 1 every two steps. etc if not white
145, 2, 44, 42 = yellow if purple or white
144, 2, 44, 42 = purple if yellow or white or turq
143, "   "   " nothing
146, 2, 42, 42 purple if anything
148, 2, 42, 42 yellow "    "

145, 1, 45, 32 blue if anything
146, 0, 39, 32 purple
145, 3, 46, 32 yellow 




	""