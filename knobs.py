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
		self.pattern = patterns.patternNumber()
		self.channel = channels.channelNumber()

		if ui.getFocused(0) and self.data_one != 1:

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


		elif ui.getFocused(1) and self.data_one != 1:
			print('in channels')
			if Modes.mode == 1:												
				if Modes.step_iter == 1:									# Set Step Parameters
		
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

				elif Modes.sub_sub_step_iter == 1:								# set scale/key

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

				# elif event.data1-14 < channels.channelCount():
				# 	channels.setChannelVolume(event.data1-14, mapvalues(event.data2, 0, 1, 0, 127))

			# elif event.data1-14 < channels.channelCount():				# set channel volume
				
				elif self.data_one == data.knobs['knob_five']:
					channels.setChannelVolume(channels.selectedChannel(), mapvalues(event.data2, 0, 1, 0, 127))
				elif self.data_one == data.knobs['knob_six']:
					channels.setChannelPan(channels.selectedChannel(), mapvalues(event.data2, -1, 1, 0, 127))
				elif self.data_one == data.knobs['knob_seven']:
					mixer.linkTrackToChannel(1)
				elif self.data_one == data.knobs['knob_eight']:
					channels.setChannelColor(channels.selectedChannel(), data.colors[int(mapvalues(event.data2, 0, len(data.colors)-1, 0, 127))])

		elif ui.getFocused(5) and plugins.isValid(self.channel):
			self.plugin_control(event)

	def plugin_control(self, event):
		
		self.plugin = plugins.getPluginName(self.channel)	
		self.param_count = plugins.getParamCount(self.channel)

		if self.data_one < self.param_count + 19:				#this is probably unneccessary
			if self.plugin in plugindata.touchpad_params:
				if self.data_one == 1:												# this controls what touchpad does
					for param in plugindata.touchpad_params[self.plugin]:
						print(param)
						# plugins.setParamValue(eval(str(mapvalues ( self.data_two , 0, 1, 0, 127) )) + param[2] + str(param[1]), param[0], self.channel)
						# plugins.setParamValue(eval(  str(mapvalues(self.data_two, 0, 1, 0, 127))  + param[2] + str(param[1])),    param[0], self.channel)
						plugins.setParamValue(mapvalues(self.data_two, param[1], param[2], 0, 127), param[0], self.channel)
						event.handled = True

			if self.plugin in plugindata.plugin_dict and self.data_one != 1:
				plugins.setParamValue(mapvalues(self.data_two, 0, 1, 0, 127), plugindata.plugin_dict[self.plugin][plugindata.knob_num.index(self.data_one + (self.offset * 8))], self.channel)
				return

			else:		
				plugins.setParamValue(mapvalues(self.data_two, 0, 1, 0, 127), self.data_one - 14, self.channel)
				return

def mapvalues(value, to_min, to_max, from_min, from_max):
	input_value = value
	solution = to_min + (to_max-(to_min))*((input_value - from_min) / (from_max - (from_min)))
	if value > from_max:
		solution = to_max
	if  -0.01 < solution < 0.01:
		solution = 0
	return solution






