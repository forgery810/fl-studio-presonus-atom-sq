import ui
import channels
import device
import patterns
import plugins
import transport
import midi
from modes import Modes
from lights import Lights
import data
import plugindata
import sys

temp_step = [0]
random = 2
param_edit = 1
continuous = 1
pat = 0
chan = 1
evnt = 2
intvl = 3
limit = 4
count = 5
orig = 6
root = 7
scale = 8
n_orig = 9
n_count = 10

jump_to_pattern = 1
channel_access = 2
channel_mute = 3
step_select = 4
step_mode = 1
standard = 0
keyboard = 0 
two_bars = 0
accumulator = 1
pads_per_channel = 2
alter = 3

class Notes():

	mult = 1         # changed by c button 
	scale_choice = 0
	root_note = 0
	accum_chan = 0
	interval = 0
	pass_trig = 0
	p_iter = 0      # counts the amount of passes/reset everytime note altered
	trig_iter = 0   # incremented everytime note altered
	t_limit = 4     # after this many time note altered / start over
	pass_limit = 0  # decided by knob 4 when accumulator active
	original_note = 0
	accum_steps = []   # pattern, channel, step, 
	accum_dict = {}
	accu_count = 0
	accum_on = True

	def __init__(self, event):
		
		if event.midiId == 144: 			# store last note played for parameter edit
			temp_step.clear()
			temp_step.append(event.data1)
		self.light = Lights()
		self.p = Modes(event)
		self.decide(event)
	
	def decide(self, event):
		"""takes midi event data and passes it to appropriate function based on current mode found in Modes()"""

		if ui.getFocusedPluginName() in plugindata.drum_plugs:
			self.drum_plugins(event)
		elif self.get_mode() == 0:
			if Modes.note_iter == keyboard:
				self.keyboard(event)
			elif Modes.note_iter == continuous:
				self.continuous(event)
		elif self.get_mode() == step_mode and event.data2 > 0:
			self.step_mode(event)
		elif self.get_mode() == pads_per_channel:
			self.pad_channel(event)
		elif self.get_mode() == alter and event.data2 > 0:
			self.alter_steps(event)
			Modes.mode_init()
			event.handled = True

	def keyboard(self, event):
		"""calls for keyboard led layout and takes incoming midi data and converts to approprite note in key_dict"""

		Lights.keyboard_lights()
		if str(event.data1) in data.key_dict:
			channels.midiNoteOn(channels.selectedChannel(), data.key_dict[str(event.data1)] + Modes.get_octave(), event.data2)
		else:
			channels.midiNoteOn(channels.selectedChannel(), event.data1, event.data2)
		event.handled = True
	
	def continuous(self, event):
		"""controls what happens to notepad presses when in continuous mode. -24 adjusts step data1 to tolerable range of notes within scale"""

		channels.midiNoteOn(channels.selectedChannel(), data.scales[Modes.scale_iter][Modes.root_iter][event.data1-24], event.data2)
		Modes.mode_init()
		event.handled = True


	def alter_steps(self, event):
		"""decides what class/function gets called when in alter mode and note/step is pressed"""

		if Modes.alter_iter == 1:
			if Notes.accum_on and event.data1 - 36 < patterns.getPatternLength(patterns.patternNumber()):
				Notes.original_note = channels.getCurrentStepParam(channels.selectedChannel(), event.data1-36, 0)

				if Notes.original_note in data.scales[Notes.scale_choice][Notes.root_note]:
					Notes.accum_steps.append([patterns.patternNumber(), channels.channelNumber(), event.data1-36, 
						Notes.interval, Notes.pass_limit, 0, Notes.original_note, Notes.root_note, Notes.scale_choice, 
						Notes.original_note, 0])

				Notes.accum_chan = channels.channelNumber()
				Modes.mode_init()
				event.handled = True

			else:
				Modes.mode_init()
				event.handled = True

	def step_mode(self, event):
		"""controls notepad presses when in step mode"""

		if Modes.step_iter == jump_to_pattern and event.data1 >= 52:		# Pattern Select Mode
			patterns.jumpToPattern(event.data1 - 51 + (16 * Modes.get_mult()))
			Modes.mode_init()
			event.handled = True

		elif Modes.step_iter == channel_access and event.data1 >= 52:		# channel select
			if event.data1 - 52 >= channels.channelCount() - (16 * Modes.get_mult()):
				Modes.mode_init()
				event.handled = True
			else:
				channels.selectOneChannel((event.data1 - 52) + (16 * Modes.get_mult()))
				Modes.mode_init()
				event.handled = True

		elif Modes.step_iter == channel_mute and event.data1 >= 52: 		# channel mute
			if event.data1 - 52 >= channels.channelCount() - (16 * Modes.get_mult()):
				Modes.mode_init()
				event.handled = True
			else:
				channels.muteChannel((event.data1 - 52) + (16 * Modes.get_mult()))
				Modes.mode_init()
				event.handled = True
														
		elif Modes.get_step_submode() != param_edit:      						  # sets step as long as param edit not active
			if channels.getGridBit(channels.selectedChannel(), event.data1 - 36) == 0:						
				channels.setGridBit(channels.selectedChannel(), event.data1 - 36, 1)
				Modes.mode_init()	
				event.handled = True
			else:															
				channels.setGridBit(channels.selectedChannel(), event.data1 - 36, 0)
				Modes.mode_init()    
				event.handled = True

		elif Modes.get_step_submode() == param_edit or Modes.mode == 3:
			ui.setHintMsg(f'Note: {data.midi_notes[channels.getCurrentStepParam(channels.selectedChannel(), event.data1-36, 0)]}')#{data.midi_notes[channels.getGridBit(channels.selectedChannel(), event.data1 - 36)]}')
			Modes.mode_init()
			event.handled = True

		else:
			Modes.mode_init()
			event.handled = True

	def pad_channel(self, event):
		"""takes event midi data from pad press and plays corresponding channel"""

		if event.data1 == 67:
			transport.globalTransport(midi.FPT_TapTempo, 1)
			event.handled = True
		elif  event.data1 < (channels.channelCount() + 36) and event.midiId != 208:
			channels.selectOneChannel(event.data1-36) 
			channels.midiNoteOn(event.data1-36, 60, event.data2)
			event.handled = True
		else:
			event.handled = True
		Modes.mode_init()

	def drum_plugins(self, event):
		"""called when a drum plugin window is focused and plays corresponding drum pad"""

		if event.midiId == 128 and event.data2 != 0:
			print('skip')
		elif plugins.getPluginName(channels.selectedChannel()) == 'FPC' and event.data1 in plugindata.atom_sq_pads:
			print('FPC')
			Lights.clear_pattern()
			channels.midiNoteOn(channels.selectedChannel(), plugindata.FPC_pads[plugindata.atom_sq_pads.index(event.data1)], event.data2)
			event.handled = True
		elif plugins.getPluginName(channels.selectedChannel()) == 'Slicex':
			Lights.clear_pattern()
			channels.midiNoteOn(channels.selectedChannel(), event.data1 + 24, event.data2)
			event.handled = True

	def get_mode(self):
		return Modes.mode

	def get_step_submode(self):
		return Modes.step_iter

	def update_beat():
		"""used for accumulator. tracks every step when transport is active"""

		for step in Notes.accum_steps:
			if step[chan] <= channels.channelCount()-1:									# in case channels are deleted and 
				step[count] += 1 														# iterate each counter per step
				if step[count] <= step[limit] and len(Notes.accum_steps) > 0:			# if there are steps saved and the are below count send to accumulator function
					Notes.accumulator(step)
				elif step[count] > step[limit] and len(Notes.accum_steps) > 0:			# else if count had gone over limit reset count and set to intial note value
					# print(f'note reset: {step[6]}')
					step[count] = 0
					step[n_orig] = step[orig]
					channels.setStepParameterByIndex(step[chan], step[pat], step[evnt], 0, step[orig])

		# ([patterns.patternNumber(), channels.channelNumber(), event.data1-36, Notes.interval, Notes.pass_limit, 0, Notes.original_note, Notes.root_note, Notes.scale_choice, step_val, note_in_scale])
		#   		0 							1 						2 			 3 					4  		  5 		6 					7 				8  					9        10

	def temp_reset_steps():
		"""rests accumulator steps to original notes"""

		for s in Notes.accum_steps:
			s[n_orig] = s[orig]

	def accumulator(step_info):
		"""step_info list for step to apply accumulator to. loops through pattern steps. gets current note, adds interval and resets note. """

		stp = step_info
		for beat in range(patterns.getPatternLength(stp[pat])): 						# only applies to current pattern. may need to use stored pattern
			if beat == stp[evnt]:
				# print(f'Step Val: {t[9]}')				
				if stp[n_orig] < 0:														# this catches potential -1 error and resets to root note
					print('-1 error')
					stp[n_orig] = stp[orig]
				stp[n_count] = data.scales[stp[scale]][stp[root]].index(stp[n_orig])   	# find current note is in selected scale
				channels.setStepParameterByIndex(stp[chan], stp[pat], beat, 0, data.scales[stp[scale]][stp[root]][stp[n_count] + stp[intvl]])
				stp[n_orig] = data.scales[stp[scale]][stp[root]][stp[n_count] + stp[intvl]]
	
	def reset_steps():
		"""resets all accumulator steps to original note stored in pattern"""

		for r in Notes.accum_steps:
			if r[pat] == patterns.patternNumber():
				for st in range(patterns.getPatternLength(patterns.patternNumber())):
					if st == r[evnt]:
						channels.setStepParameterByIndex(r[chan], r[pat], st, 0, r[orig])
		Notes.accum_steps.clear()
		ui.setHintMsg('Accum steps cleared')

class Shifter():

	shift_data = []
	shift_type = 0
	shifter_on = True
	new_list = []
	new_pattern = []
	
	def __init__(self):
		self.pat = 0
		self.chan = 1
		self.direction = 2
		self.new_pat = 4
		self.pattern = []
		self.formatted = []

	def shift_patterns(self):
		"""this function will go through stored shift data and call other functions to convert pattern to int and then to 
			binary be able to have bit shifting applied. It will then convert it back and write to pattern(s)"""

		if Shifter.shifter_on:
			for l in Shifter.shift_data:								# loop through list with shifter info
				# print(f'L: {l}')
				if l[1] < channels.channelCount():
					l[3] = self.pattern_to_string(l)						# pattern stored as string in list
					# print(f'str_pat: {l[3]}')

					l[3] = self.str_to_int(l[3])							# converted to int 
					# print(f'int_pattern: {l[3]}')	

					if l[self.direction] == 0:									# get direction set in list 
						l[4] = format(self.shift_left(l[3], l[0]), self.get_format(l[0]))			# route to appropriate bit shifter
																				# and format to binary number
					elif l[self.direction] == 1:
						l[4] = format(self.shift_right(l[3], l[0]), self.get_format(l[0]))

					elif l[self.direction] == 2:
						l[4] = format(self.invert(l[3], l[0]), self.get_format(l[0]))

					# print(f'Type l[4]: {l[4]}')
					l[5] = self.str_to_list(l[4][2:])						# convert back to list. [2:] removes leading 0b 

					if len(l[5]) > patterns.getPatternLength(l[0]):										# remove added step
						l[5].pop(0)

					self.write_to_pattern(l[5], l[0], l[1])			
					l[5].clear()

	def pattern_to_string(self, l):
		"""takes pattern info and returns in string format"""

		self.pattern.clear()
		for bit in range(0, patterns.getPatternLength(l[0])):
			self.pattern.append(str(channels.getGridBit(l[1], bit)))
		return ''.join(self.pattern)

	def str_to_int(self, pattern):
		"""takes pattern as string of numbers and returns int"""

		return int(pattern, 2)

	def shift_left(self, pat, pat_num):

		# print(f'left in: {pat}')
		out = (pat << 1) | (pat >> (patterns.getPatternLength(pat_num) - 1))
		# print(f'out: {out}')
		return out

	def shift_right(self, pat, pat_num):

		x = patterns.getPatternLength(pat_num)
		out = (pat >> 1) | (pat << (x - 1)) & self.max_bits(x)
		return out

	def invert(self, pat, pat_num):

		x = patterns.getPatternLength(pat_num)
		return (pat ^ self.max_bits(x))

	def str_to_list(self, s):
		"""takes string, s, and returns list"""

		out_list = []
		for i in s:
			out_list.append(int(i))
		return out_list

	def write_to_pattern(self, p, pat_num, chan):
		"""writes bit shifted pattern to approriate channel"""

		inx = 0
		if patterns.patternNumber() == pat_num:
			for i in range(patterns.getPatternLength(pat_num)):    # clear pattern
				channels.setGridBit(chan, i, 0)
			for step in p:
				channels.setGridBit(chan, inx, step)
				inx += 1
		
	def set_shift(self):
		"""writes shift info based on channel, pattern and type set by knob 5"""

		if Shifter.shift_type == 3:
			self.clear_channel()
		else:
			Shifter.shift_data.append([patterns.patternNumber(), channels.selectedChannel(), Shifter.shift_type, 0, 0, 0, ])
											# 0 					1 						2 			3    4 new_pat								
		print(f'shift data: {Shifter.shift_data}')

	def clear_channel(self):
		"""erases data in shift_data for currently selected channel"""

		for info in Shifter.shift_data:
			if info[0] == patterns.patternNumber() and info[1] == channels.channelNumber():
				del Shifter.shift_data[Shifter.shift_data.index(info)]

	def max_bits(self, num):
		"""returns the maximun integer based on num in bits"""

		max_num = (1 << num) - 1
		print(max_num)
		return max_num

	def get_format(self, pat_num):
		"""gets patterns num and returns appropriate string to format in into bits"""

		length = patterns.getPatternLength(pat_num) + 2
		return f'#0{length}b'