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
random = 1
param_edit = 1
jump_to_pattern = 2
step_mode = 1
standard = 0
keyboard = 0 
two_bars = 0
accumulator = 2 
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
		print(f'notes event: {event.data1}')

		if event.midiId == 144: 			# store last note played for parameter edit
			temp_step.clear()
			temp_step.append(event.data1)
		self.light = Lights()
		self.decide(event)

	def decide(self, event):

		if ui.getFocusedPluginName() in plugindata.drum_plugs:
			self.drum_plugins(event)
		elif self.get_mode() == keyboard:
			self.keyboard(event)
			# Lights.clear_pattern()
		elif self.get_mode() == step_mode and event.data2 > 0:
			self.step_mode(event)
		elif self.get_mode() == pads_per_channel:
			self.pad_channel(event)

	def keyboard(self, event):
		if Modes.note_iter == 1:
			channels.midiNoteOn(channels.selectedChannel(), event.data1, event.data2)
			Lights.continuous_notes()
		elif Modes.note_iter == 0:
			Lights.keyboard_lights()
			if str(event.data1) in data.key_dict:
				channels.midiNoteOn(channels.selectedChannel(), data.key_dict[str(event.data1)] + Modes.octave_values[Modes.sub_sub_key_iter], event.data2)
			else:
				channels.midiNoteOn(channels.selectedChannel(), event.data1, event.data2)
			print('keyboard')
			event.handled = True
				
	def step_mode(self, event):
		
		if Modes.step_iter == jump_to_pattern and event.data1 >= 52:		# Pattern Select Mode
			print('select pattern')
			patterns.jumpToPattern(event.data1 - 51)
			Lights.pattern_select()
			event.handled = True

		elif Modes.step_iter == param_edit: 								# what to do with lights in param edit mode
			self.light.update_pattern(Modes.step_iter)
			self.light.update_second(Modes.step_iter)
			event.handled = True

		elif Modes.step_iter != param_edit and Modes.sub_sub_step_iter == accumulator:							# ACCUMULATOR
			# print('in step in accum edit')
			if Notes.accum_on and event.data1 - 36 < patterns.getPatternLength(patterns.patternNumber()):
				Notes.original_note = channels.getCurrentStepParam(channels.selectedChannel(), event.data1-36, 0)
				print(Notes.original_note)
				if Notes.original_note in data.scales[Notes.scale_choice][Notes.root_note]:
					Notes.accum_step.append([patterns.patternNumber(), channels.channelNumber(), event.data1-36, Notes.interval, Notes.pass_limit, 0, Notes.original_note, Notes.root_note, Notes.scale_choice, Notes.original_note, 0])
				Notes.accum_chan = channels.channelNumber()
				# print(f'Accu_step: {Notes.accum_step}')
				event.handled = True

			else:
				event.handled = True
																# make sure not in accum or param entry modes
		elif Modes.step_iter != param_edit or Modes.step_iter == jump_to_pattern and event.data1 < 52:       
			if channels.getGridBit(channels.selectedChannel(), event.data1 - 36) == 0:						
				channels.setGridBit(channels.selectedChannel(), event.data1 - 36, 1)	
				event.handled = True
			else:															
				channels.setGridBit(channels.selectedChannel(), event.data1 - 36, 0)    
				event.handled = True		
			Lights.update_pattern(Modes.step_sub_iter)

			if Modes.step_iter == jump_to_pattern:
				self.light.pattern_select()
			else:	
				self.light.update_second(Modes.step_iter)	

	def pad_channel(self, event):
		print('in pad channel')
		if  event.data1 < (channels.channelCount() + 36) and event.midiId != 208:
			channels.selectOneChannel(event.data1-36) 
			channels.midiNoteOn(event.data1-36, 60, event.data2)
			Lights.light_channels()
			event.handled = True
		else:
			Lights.light_channels()
			event.handled = True


	def drum_plugins(self, event):

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

	@staticmethod
	def update_beat(beat):
		if beat == 1 and Notes.accum_on:
			for l in Notes.accum_step:
				l[5] += 1 												# iterate each counter per step
				if l[5] <= l[4] and len(Notes.accum_step) > 0:			# if there are steps saved and the are below count send to accumulator function
					Notes.accumulator(l)
				elif l[5] > l[4] and len(Notes.accum_step) > 0:			# else if count had gone over limit reset count and set to intial note value
					# print(f'note reset: {l[6]}')
					l[5] = 0
					l[9] = l[6]
					channels.setStepParameterByIndex(l[1], l[0], l[2], 0, l[6])

		# ([patterns.patternNumber(), channels.channelNumber(), event.data1-36, Notes.interval, Notes.pass_limit, 0, Notes.original_note, Notes.root_note, Notes.scale_choice, step_val, note_in_scale])
		#   		0 							1 						2 			 3 					4  		  5 		6 					7 				8  					9        10
	@staticmethod
	def temp_reset_steps():
		for n in Notes.accum_step:
			n[9] = n[6]

	@staticmethod
	def accumulator(step_info):
		t = step_info
		# print(Notes.accum_step)
		for step in range(patterns.getPatternLength(patterns.patternNumber())):
			if step == t[2]:
				# print(f'Step Val: {t[9]}')				# this catches -1 error and resets to root note
				if t[9] < 0:					
					print('-1 error')
					t[9] = t[6]
				t[10] = data.scales[t[8]][t[7]].index(t[9])   # find current note is in selected scale
				# print(f'note_in_scale: {t[10]}')
				# print(f'noteinscale + t[3]: {t[10] + t[3]}')
				channels.setStepParameterByIndex(t[1], t[0], step, 0, data.scales[t[8]][t[7]][t[10] + t[3]])
				t[9] = data.scales[t[8]][t[7]][t[10] + t[3]]

	@staticmethod
	def reset_steps():
		for r in Notes.accum_step:
			if r[0] == patterns.patternNumber():
				for st in range(patterns.getPatternLength(patterns.patternNumber())):
					if st == r[2]:
						channels.setStepParameterByIndex(r[1], r[0], st, 0, r[6])
		Notes.accum_step.clear()
		ui.setHintMsg('Accum steps cleared')

 