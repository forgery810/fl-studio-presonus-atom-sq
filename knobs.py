import mixer
import channels
import data
import ui
import device
from modes import Modes
from notes import Notes, Shifter
import notes
import patterns
import plugins
import plugindata
from lights import Lights
from buttons import Buttons
from config import options

class Knobs:

	def __init__(self, event):
		self.get_track = 0
		self.offset = event.midiChanEx - 128
		self.knob_turn(event)

	def knob_turn(self, event):
		"""handles majority of knob based events"""
		
		self.data_one = event.data1
		self.data_two = event.data2
		self.pad_step = notes.temp_step[0]
		self.pattern = patterns.patternNumber()
		self.channel = channels.channelNumber()

		if ui.getFocused(0) and self.data_one != 1:      # when mixer is focused

			if event.data1 == data.knobs["knob_five"]:
				mixer.setTrackVolume(mixer.trackNumber(), mapvalues(event.data2, 0, 1, 0, 127))
			elif event.data1 == data.knobs["knob_six"]:
				mixer.setTrackPan(mixer.trackNumber(), mapvalues(event.data2, -1, 1, 0, 127))
			elif event.data1 == data.knobs["knob_seven"]:
				three = event.data2
			elif event.data1 == data.knobs["knob_eight"]:
				four = event.data2

		elif ui.getFocused(1) and self.data_one != 1:

			if Modes.mode == 1:				
				if Modes.get_step_submode() == 1:									# Set Step Parameters
					if self.data_one == data.knobs["knob_one"]:
						ui.setHintMsg(f'Note: {data.midi_notes[self.data_two]}')
					elif self.data_one <= 20:
						ui.setHintMsg(f'{data.parameters[self.data_one - 14]}: {event.data2}')
					if 6 <= self.data_one - 14 >= 5:
						channels.setStepParameterByIndex(self.channel, self.pattern, self.pad_step - 36, self.data_one - 14, int(mapvalues(self.data_two, 0 , 255, 0, 127)), 1)
						event.handled = True
					elif self.data_one - 14 == 3:
						channels.setStepParameterByIndex(self.channel, self.pattern, self.pad_step - 36, self.data_one - 14, int(mapvalues(self.data_two, 0 , 240, 0, 127)), 1)
						event.handled = True
					else:
						channels.setStepParameterByIndex(self.channel, self.pattern, self.pad_step - 36, self.data_one - 14, self.data_two, 1)
						event.handled = True

				elif Modes.get_step_submode() == 2:								# Random Mode - set scale/key

					if event.data1 == data.knobs["knob_five"]:
						Buttons.root_note = int(mapvalues(self.data_two, 0, 11, 0, 127))
						print(f'button.root_note: {Buttons.root_note}')
						ui.setHintMsg(data.notes_list[Buttons.root_note])
					elif event.data1 == data.knobs["knob_six"]:
						Buttons.scale = int(mapvalues(self.data_two, 0, len(data.scale_names)-1, 0, 127))
						ui.setHintMsg(data.scale_names[int(mapvalues(self.data_two, 0, len(data.scale_names)-1, 0, 127))])				
					elif event.data1 == data.knobs["knob_seven"]:
						Buttons.lower_limit = int(mapvalues(self.data_two, 0, 25, 0, 127))
						ui.setHintMsg(f"Setting Lower Limit  {self.data_two}")
					elif event.data1 == data.knobs["knob_eight"]:
						Buttons.upper_limit = int(mapvalues(self.data_two, 127, 0, 0, 127))
						ui.setHintMsg(f"Setting Upper Limit {self.data_two}")
																		# standard mode
				elif self.data_one == data.knobs['knob_five']:
					channels.setChannelVolume(channels.selectedChannel(), mapvalues(event.data2, 0, 1, 0, 127))
				elif self.data_one == data.knobs['knob_six']:
					channels.setChannelPan(channels.selectedChannel(), mapvalues(event.data2, -1, 1, 0, 127))
				elif self.data_one == data.knobs['knob_seven'] and options['saved_patterns'] == True:
					self.set_pattern(int(mapvalues(self.data_two, 0, len(data.preset_patterns)-1, 0, 127)))
					# event.handled = True

				elif self.data_one == data.knobs['knob_eight']:
					channels.setChannelColor(channels.selectedChannel(), data.colors[int(mapvalues(event.data2, 0, len(data.colors)-1, 0, 127))])

			elif Modes.mode == 3:   								# Alter
				if Modes.get_alter_mode() == 0:
					if self.data_one == data.knobs['knob_five']:
						Shifter.shift_type = int(mapvalues(self.data_two, 0, len(Modes.shifter_options) - 1, 0, 127))
						ui.setHintMsg(f'Shift Type: {Modes.shifter_options[Shifter.shift_type]}')

				elif Modes.get_alter_mode() == 1:		
					if self.data_one == data.knobs['knob_five']:
						Notes.root_note = int(mapvalues(self.data_two, 0, 11, 0, 127))
						ui.setHintMsg(data.notes_list[int(mapvalues(self.data_two, 0, 11, 0, 127))])
					elif event.data1 == data.knobs["knob_six"]:
						Notes.scale_choice = int(mapvalues(self.data_two, 0, len(data.scale_names)-1, 0, 127))
						ui.setHintMsg(data.scale_names[int(mapvalues(self.data_two, 0, len(data.scale_names)-1, 0, 127))])		
					elif event.data1 == data.knobs["knob_seven"]:
						Notes.interval = int(mapvalues(self.data_two, -12, 12, 0, 127))
						ui.setHintMsg(f'Note Interval: {int(mapvalues(self.data_two, -12, 12, 0, 127))}')
					elif event.data1 == data.knobs["knob_eight"]:
						Notes.pass_limit = int(mapvalues(self.data_two, 0, 10, 0, 127))
						ui.setHintMsg(f'Count: {int(mapvalues(self.data_two, 0, 10, 0, 127))}')
					event.handled = True

		elif ui.getFocused(5) and plugins.isValid(self.channel):
			self.plugin_control(event)

	def plugin_control(self, event):
		"""Called when plugin is focused. Knobs are set to control parameters on focused plugin"""
		self.plugin = plugins.getPluginName(self.channel)	
		self.param_count = plugins.getParamCount(self.channel)

		if self.plugin in plugindata.touchpad_params:
			if self.data_one == 1:												# this controls what touchpad does
				for param in plugindata.touchpad_params[self.plugin]:
					plugins.setParamValue(mapvalues(self.data_two, param[1], param[2], 0, 127), param[0], self.channel)
					event.handled = True

		if self.plugin in plugindata.plugin_dict and self.data_one != 1:
			plugins.setParamValue(mapvalues(self.data_two, 0, 1, 0, 127), plugindata.plugin_dict[self.plugin][plugindata.knob_num.index(self.data_one + (self.offset * 8))], self.channel)
			event.handled = True

		else:		
			plugins.setParamValue(mapvalues(self.data_two, 0, 1, 0, 127), self.data_one - 14, self.channel)
			event.handled = True

	def set_pattern(self, pattern):
		"""receives pattern number and looks up saved patterns. Sets chose pattern"""
		for i in range(patterns.getPatternLength(patterns.patternNumber())):    # clear pattern
			channels.setGridBit(channels.channelNumber(), i, 0)
		for count, value in enumerate(data.preset_patterns[pattern]):
			channels.setGridBit(channels.selectedChannel(), count, value)	

def mapvalues(value, to_min, to_max, from_min, from_max):
	"""takes in value and range and returns value within another range"""
	input_value = value
	solution = to_min + (to_max-(to_min))*((input_value - from_min) / (from_max - (from_min)))
	if value > from_max:
		solution = to_max
	if  -0.01 < solution < 0.01:
		solution = 0
	return solution


