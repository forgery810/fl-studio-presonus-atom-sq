import ui
import channels
import device
import patterns
import plugins
from modes import Modes
from lights import Lights
import data
import plugindata

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
step_mode = 1
standard = 0
keyboard = 0 
two_bars = 0
accumulator = 3
pads_per_channel = 2

class Notes():

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
	accum_step = []   # pattern, channel, step, 
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

	def keyboard(self, event):
		"""calls for keyboard led layout and takes incoming midi data and converts to approprite note in key_dict"""
		Lights.keyboard_lights()
		if str(event.data1) in data.key_dict:
			channels.midiNoteOn(channels.selectedChannel(), data.key_dict[str(event.data1)] + Modes.octave_values[Modes.sub_sub_key_iter], event.data2)
		else:
			channels.midiNoteOn(channels.selectedChannel(), event.data1, event.data2)
		event.handled = True
	
	def continuous(self, event):
		"""controls what happens to notepad presses when in continuous mode. -24 adjusts step data1 to tolerable range of notes within scale"""
		channels.midiNoteOn(channels.selectedChannel(), data.scales[Modes.scale_iter][Modes.root_iter][event.data1-24], event.data2)
		self.p.mode_init()
		event.handled = True

	def step_mode(self, event):
		"""controls notepad presses when in step mode"""

		if Modes.step_iter == jump_to_pattern and event.data1 >= 52:		# Pattern Select Mode
			patterns.jumpToPattern(event.data1 - 51)
			self.p.mode_init()
			event.handled = True

		elif Modes.step_iter == channel_access and event.data1 >= 52:		# channel select
			if event.data1 >= channels.channelCount() + 52:
				self.p.mode_init()
				event.handled = True
			else:
				channels.selectOneChannel(event.data1 - 52)
				self.p.mode_init()
				event.handled = True

		elif Modes.step_iter == channel_mute and event.data1 >= 52: 		# channel mute
			if event.data1 >= channels.channelCount() + 52:
				self.p.mode_init()
				event.handled = True
			else:
				channels.muteChannel(event.data1 - 52)
				self.p.mode_init()
				event.handled = True

															# ACCUMULATOR
		elif  Modes.sub_sub_step_iter == accumulator:	
			if Notes.accum_on and event.data1 - 36 < patterns.getPatternLength(patterns.patternNumber()):
				Notes.original_note = channels.getCurrentStepParam(channels.selectedChannel(), event.data1-36, 0)

				if Notes.original_note in data.scales[Notes.scale_choice][Notes.root_note]:
					Notes.accum_step.append([patterns.patternNumber(), channels.channelNumber(), event.data1-36, 
						Notes.interval, Notes.pass_limit, 0, Notes.original_note, Notes.root_note, Notes.scale_choice, 
						Notes.original_note, 0])

				Notes.accum_chan = channels.channelNumber()
				self.p.mode_init()
				event.handled = True

			else:
				self.p.mode_init()
				event.handled = True

																
		elif Modes.sub_sub_step_iter != param_edit:        # sets step as long as param edit not active
			if channels.getGridBit(channels.selectedChannel(), event.data1 - 36) == 0:						
				channels.setGridBit(channels.selectedChannel(), event.data1 - 36, 1)
				self.p.mode_init()	
				event.handled = True
			else:															
				channels.setGridBit(channels.selectedChannel(), event.data1 - 36, 0)
				self.p.mode_init()    
				event.handled = True

		elif Modes.sub_sub_step_iter == param_edit:
			ui.setHintMsg(f'Note: {data.midi_notes[channels.getCurrentStepParam(channels.selectedChannel(), event.data1-36, 0)]}')#{data.midi_notes[channels.getGridBit(channels.selectedChannel(), event.data1 - 36)]}')
			self.p.mode_init()
			event.handled = True

		else:
			self.p.mode_init()
			event.handled = True

	def pad_channel(self, event):
		"""takes event midi data from pad press and play corresponding channel"""
		if  event.data1 < (channels.channelCount() + 36) and event.midiId != 208:
			channels.selectOneChannel(event.data1-36) 
			channels.midiNoteOn(event.data1-36, 60, event.data2)
			event.handled = True
		else:
			event.handled = True
		self.p.mode_init()

	def drum_plugins(self, event):
		"""called when drum plugin window focused and plays corresponding drum pad"""
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

	def update_beat(beat):
		"""used for accumulator. tracks every step when transport is active"""
		if beat == 1 and Notes.accum_on:
			for l in Notes.accum_step:
				if l[chan] <= channels.channelCount()-1:
					l[count] += 1 												# iterate each counter per step
					if l[count] <= l[limit] and len(Notes.accum_step) > 0:			# if there are steps saved and the are below count send to accumulator function
						Notes.accumulator(l)
					elif l[count] > l[limit] and len(Notes.accum_step) > 0:			# else if count had gone over limit reset count and set to intial note value
						# print(f'note reset: {l[6]}')
						l[count] = 0
						l[n_orig] = l[orig]
						channels.setStepParameterByIndex(l[chan], l[pat], l[evnt], 0, l[orig])

		# ([patterns.patternNumber(), channels.channelNumber(), event.data1-36, Notes.interval, Notes.pass_limit, 0, Notes.original_note, Notes.root_note, Notes.scale_choice, step_val, note_in_scale])
		#   		0 							1 						2 			 3 					4  		  5 		6 					7 				8  					9        10

	def temp_reset_steps():
		for n in Notes.accum_step:
			n[n_orig] = n[orig]

	def accumulator(step_info):
		"""step_info list for step to apply accumulator to. loops through pattern steps. gets current note, adds interval and resets note. """
		t = step_info
		for step in range(patterns.getPatternLength(t[pat])): # only applies to current pattern. may need to used stored pattern
			if step == t[evnt]:
				# print(f'Step Val: {t[9]}')				
				if t[n_orig] < 0:						# this catches potential -1 error and resets to root note
					print('-1 error')
					t[n_orig] = t[orig]
				t[n_count] = data.scales[t[scale]][t[root]].index(t[n_orig])   # find current note is in selected scale
				channels.setStepParameterByIndex(t[chan], t[pat], step, 0, data.scales[t[scale]][t[root]][t[n_count] + t[intvl]])
				t[n_orig] = data.scales[t[scale]][t[root]][t[n_count] + t[intvl]]
	
	def reset_steps():
		"""resets all accumulator steps to original note stored in pattern"""
		for r in Notes.accum_step:
			if r[pat] == patterns.patternNumber():
				for st in range(patterns.getPatternLength(patterns.patternNumber())):
					if st == r[evnt]:
						channels.setStepParameterByIndex(r[chan], r[pat], st, 0, r[orig])
		Notes.accum_step.clear()
		ui.setHintMsg('Accum steps cleared')

 