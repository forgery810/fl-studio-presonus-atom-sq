import mixer
import channels
import data
import ui
import device
from modes import Modes
from notes import Notes
import notes
import patterns
import plugins
import plugindata
from lights import Lights
from buttons import Buttons
one = 0
two = 0
three = 0
four = 0
class Knobs:

	def __init__(self, event):
		print(event.midiId)
		self.get_track = 0
		# self.data_one = data_one + offset[offset_iter]
		# self.data_two = data_two
		# self.focused = focused
		self.first = 0
		self.second = 0
		self.third = 0
		self.offset = event.midiChanEx - 128
		self.knob_turn(event)




	def knob_turn(self, event):
		print('knob_turn')
		global one
		global two 
		global three 
		global four 


		self.data_one = event.data1
		self.data_two = event.data2
		self.pad_step = notes.temp_step[0]
		print(f'{self.data_one} {self.data_two}')
		self.pattern = patterns.patternNumber()
		self.channel = channels.channelNumber()



		if ui.getFocused(0):

			if event.data1 == data.knobs["knob_five"]:
				# one = event.data2
				mixer.setTrackVolume(mixer.trackNumber(), mapvalues(event.data2, 0, 1, 0, 127))
				# device.midiOutMsg(one+30, two, three, four)
				# print(f'{one + 30}, {two}, {three}, {four}')
				# one += 1
			elif event.data1 == data.knobs["knob_six"]:
				mixer.setTrackPan(mixer.trackNumber(), mapvalues(event.data2, -1, 1, 0, 127))
				# two = event.data2
				# device.midiOutMsg(one+30, two, three, four)
				# print(f'{one+30}, {two}, {three}, {four}')

			elif event.data1 == data.knobs["knob_seven"]:
				three = event.data2
				# device.midiOutMsg(one+30, two, three, four)
				# print(f'{one+30}, {two}, {three}, {four}')
				# three += 1

			elif event.data1 == data.knobs["knob_eight"]:
				four = event.data2
				# device.midiOutMsg(one+30, two, three, four)
				# print(f'{one+30}, {two}, {three}, {four}')


		elif ui.getFocused(1):
			print('in channels')
			if Modes.mode == 1:
				if Modes.step_iter == 1:
		
					if event.data1 <= 20:
						ui.setHintMsg(data.parameters[self.data_one - 14])

					if 6 <= self.data_one - 14 >= 5:
						channels.setStepParameterByIndex(self.channel, self.pattern, self.pad_step - 36, self.data_one - 14, int(mapvalues(self.data_two, 0 , 255, 0, 127)), 1)
						event.handled = True
					elif self.data_one - 14 == 3:
						channels.setStepParameterByIndex(self.channel, self.pattern, self.pad_step - 36, self.data_one - 14, int(mapvalues(self.data_two, 0 , 240, 0, 127)), 1)
						event.handled = True
					else:
						# Lights.light_note(self.data_two)
						channels.setStepParameterByIndex(self.channel, self.pattern, self.pad_step - 36, self.data_one - 14, self.data_two, 1)
						event.handled = True

				elif Modes.step_iter == 3:

					if event.data1 == data.knobs["knob_five"]:
						Buttons.root_note == int(mapvalues(self.data_two, 0, 25, 0, 127))
						ui.setHintMsg(data.notes_list[int(mapvalues(self.data_two, 0, 11, 0, 127))])

					elif event.data1 == data.knobs["knob_six"]:
						Buttons.scale == int(mapvalues(self.data_two, 0, 25, 0, 127))
						ui.setHintMsg(data.scale_names[int(mapvalues(self.data_two, 0, len(data.scale_names)-1, 0, 127))])
					
					elif event.data1 == data.knobs["knob_seven"]:
						Buttons.lower_limit = int(mapvalues(self.data_two, 0, 25, 0, 127))
						ui.setHintMsg("Setting Lower Limit")

					elif event.data1 == data.knobs["knob_eight"]:
						Buttons.upper_limit = int(mapvalues(self.data_two, 50, 0, 0, 127))
						ui.setHintMsg("Setting Upper Limit")

				elif event.data1-14 < channels.channelCount():
					channels.setChannelVolume(event.data1-14, mapvalues(event.data2, 0, 1, 0, 127))

			elif event.data1-14 < channels.channelCount():
				channels.setChannelVolume(event.data1-14, mapvalues(event.data2, 0, 1, 0, 127))
			


		elif ui.getFocused(5) and plugins.isValid(self.channel):
			self.plugin_control(event)





	def plugin_control(self, event):
		
		self.plugin = plugins.getPluginName(self.channel)	
		self.param_count = plugins.getParamCount(self.channel)

		if self.data_one < self.param_count + 19:				#this is probably unneccessary
			if self.plugin in plugindata.plugin_dict:
				print(self.offset)
				print('has plugin')			
				# print(plugin_dict[self.plugin][knob_num.index(self.data_one)])                                                                             																		
				# plugins.setParamValue(mapvalues(self.data_two, 0, 1, 0, 127), plugindata.plugin_dict[self.plugin][plugindata.knob_num.index(self.data_one + (self.offset * 8))], self.channel)
				plugins.setParamValue(mapvalues(self.data_two, 0, 1, 0, 127), plugindata.plugin_dict[self.plugin][plugindata.knob_num.index(self.data_one + (self.offset * 8))], self.channel)
				return

			else:		
				print('else')
				plugins.setParamValue(mapvalues(self.data_two, 0, 1, 0, 127), self.data_one - 14, self.channel)
				return







def mapvalues(value, tomin, tomax, frommin, frommax):
	input_value = value
	solution = tomin + (tomax-(tomin))*((input_value - frommin) / (frommax - (frommin)))
	if  -0.01 < solution < 0.01:
		solution = 0
#	print(f"Solution: {solution}")
	return solution



# 			elif self.focused == 1 and mixer_num == 1:
# 				mixer.setTrackPan(self.data_one-19, mapvalues(self.data_two, -1, 1, 0, 127))
# 			elif self.focused == 0 and self.data_one-20 < channels.channelCount():
# 				print("Channel Count")
# 				print(channels.channelCount())
# 				print("Active Channel")
# 				print(self.data_one-20)
# 				channels.setChannelVolume(self.data_one-20, mapvalues(self.data_two, 0, 1, 0, 127))

# 		elif proceed == True and temp_chan != self.data_one - 19:
# 			print("proceed no more")
# 			proceed = False		

# 	def step_param(self, pat, param):

# 		self.pattern = pat
# 		self.parameter = param
# #		print(f"Parameter:  {self.parameter}")
# #		print(f"Data One:  {self.data_one}")
# #		print(f"Pattern:  {self.pattern}")
# 		if channels.getGridBit(channels.channelNumber(), self.data_one - 20) == 1:
# 			print("getGridBit gotten")
# 			if 6 <= self.parameter >= 5:
# 				channels.setStepParameterByIndex(self.channel, self.pattern, self.data_one - 20, self.parameter, int(mapvalues(self.data_two, 0 , 255, 0, 127)), 1)

# 			elif parameter == 3:
# 				channels.setStepParameterByIndex(self.channel, self.pattern, self.data_one - 20, self.parameter, int(mapvalues(self.data_two, 0 , 240, 0, 127)), 1)
			
# 			else:	
# 				channels.setStepParameterByIndex(channels.channelNumber(), patterns.patternNumber(), self.data_one - 20, self.parameter, self.data_two, 1)
			
# 		else:
# 			print("getGridbit not gotten")

# 	def plugin_control(self):
# 		print('mapped value')
# 		print(mapvalues(self.data_two, 0, 1, 0, 127))
# 		plugins.setParamValue(mapvalues(self.data_two, 0, 1, 0, 127), self.data_one - 20, self.channel)
		
# def mapvalues(value, tomin, tomax, frommin, frommax):
# 	input_value = value
# 	solution = tomin + (tomax-(tomin))*((input_value - frommin) / (frommax - (frommin)))
# 	if  -0.01 < solution < 0.01:
# 		solution = 0
# #	print(f"Solution: {solution}")
# 	return solution