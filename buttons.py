import device
import ui
import channels
import mixer
import general
import playlist
import transport
import midi
import patterns
import data
import plugins
import config
from direction import Directions
from lights import Lights
from modes import Modes	
from notes import Notes
import _random
from midi import *

current_arrow = 0
arrow_index = 0

class Buttons:

	scale = 0
	scale_choice = 0
	note = 0
	root_note = 0
	touchpad_value = 0
	lower_limit = 0
	upper_limit = 0
	g_rotate = [2, 3, 4]
	g_iter = 0
	interval = 0
	accu_steps = []
	clear_toggle = False
	six_options = ['Press A to clear accum steps...']
	tempo_toggle = False
	button_6_iter = 0

	def __init__(self, event):
		self.push = Modes(event)
		self.act_out(event)

	def act_out(self, event):
		"handles button inputs and assigns function from fl studio api"
		if event.midiId == 144:			

			if event.data2 > 0:

				if event.data1 == data.tsport["play"]:
					transport.start()
					print('Play')
					event.handled = True

				elif event.data1 == data.tsport["stop"]:
					transport.stop()
					print('Stop')	
					event.handled = True

				elif event.data1 == data.tsport["record"]:
					transport.record()
					print('Toggle Record')	
					event.handled = True 

				elif event.data1 == data.buttons['zoom']:
					event.handled = True 

				elif event.data1 == data.tsport["metronome"]:	 
					print('Toggle Metronome')
					transport.globalTransport(midi.FPT_Metronome, 110)
					event.handled = True

				elif event.data1 == data.tsport["shift_play"]:
					transport.globalTransport(midi.FPT_LoopRecord, 113)
					print('Toggle Loop')	
					event.handled = True 

				elif event.data1 == data.tsport["shift_stop"]:
					transport.globalTransport(midi.FPT_Undo, 20)
					print('Undo/Redo')
					event.handled = True

				elif event.data1 == data.tsport["shift_record"]:
					transport.globalTransport(midi.FPT_Save, 92)
					print('Save')
					event.handled = True

				elif event.data1 in data.buttons["solo"]:
					if ui.getFocused(0):
						mixer.soloTrack(mixer.trackNumber())
						event.handled = True
					elif ui.getFocused(1):
						channels.soloChannel(channels.channelNumber())	
						event.handled = True
					else:
						event.handled = True

				elif event.data1 in data.buttons["mute"]: 
					if ui.getFocused(0):
						mixer.muteTrack(mixer.trackNumber())
						event.handled = True

					elif ui.getFocused(1):
						channels.muteChannel(channels.channelNumber())	
						event.handled = True	
					else:
						event.handled = True		

				elif event.data1 in data.buttons["arm"]:
					if ui.getFocused(0):
						mixer.armTrack(mixer.trackNumber())
						event.handled = True
					elif ui.getFocused(1):
						mixer.linkTrackToChannel(0)
						event.handled = True
					else:
						event.handled = True

				# elif event.data1 == data.buttons["zoom"]: 

				elif event.data1 == data.pads['left_arrow']:
					if ui.getFocused(5) and plugins.isValid(channels.selectedChannel()):
						print('plugin')
						plugins.prevPreset(channels.selectedChannel())
						event.handled = True

					elif ui.getFocused(1):
						transport.globalTransport(midi.FPT_PatternJog, -1)
						event.handled = True

					else:
						ui.left()
						event.handled = True

				elif event.data1 == data.pads['right_arrow']:
					if ui.getFocused(5) and plugins.isValid(channels.selectedChannel()):
						print('plugin')
						plugins.nextPreset(channels.selectedChannel())
						event.handled = True

					elif ui.getFocused(1):
						transport.globalTransport(midi.FPT_PatternJog, 1)
						event.handled = True

					else:
						ui.right()
						print('right')
						event.handled = True

		if event.midiId == 176 and event.data1 == data.pads['touch']:				# this selects for touchpad and allows it to go to zero
			Buttons.touchpad_value = event.data2

		if event.midiId == 176 and event.data2 > 0:
			
			if event.data1 == data.knobs["jog_wheel"]:
				print('jogging')

				if event.data2 == 1:
					ui.next()
				elif ui.getFocused(0):
					if event.data2 == 65 and mixer.trackNumber() > 0:
						ui.previous()
						event.handled = True
				elif event.data2:
					ui.previous()

			if event.midiChanEx == 130 and event.data2 > 0:												# 1-6 buttons

				if event.data1 == data.buttons["button_1"]:
					print('quantize')
					channels.quickQuantize(channels.channelNumber())
					event.handled = True

				elif event.data1 == data.buttons["button_4"]:
					print("Random")
					for i in range(patterns.getPatternLength(patterns.patternNumber())):    # clear pattern
						channels.setGridBit(channels.channelNumber(), i, 0)
					for z in range (patterns.getPatternLength(patterns.patternNumber())):
						y = num_gen()
						if y > (Buttons.touchpad_value * 516):
							channels.setGridBit(channels.channelNumber(), z, 1)
						else:
							channels.setGridBit(channels.channelNumber(), z, 0)
					self.push.mode_init()
					event.handled = True

				elif event.data1 == data.buttons["button_5"]:
					self.note_gen()

				elif event.data1 == data.buttons["button_6"]:
					print(Buttons.clear_toggle)
					if Modes.sub_sub_step_iter == 3:				# if in accumulator mode
						if Buttons.clear_toggle == False:
							ui.setHintMsg(Buttons.six_options[0])
							Buttons.clear_toggle = True
						elif Buttons.clear_toggle == True:
							Buttons.clear_toggle = False
							ui.setHintMsg('Clear option off')
					else:
						print('Set Tempo...or something')		# not used currently

			if event.midiChanEx == 128:						# A - H Buttons

				if event.data1 == data.pads["a"]:
					if ui.getFocused(4):
						ui.selectBrowserMenuItem()	

					elif Modes.sub_sub_step_iter == 3: 				# accumulator mode
						if Buttons.clear_toggle == True:
							# Notes.accum_step.clear()
							Notes.reset_steps()
							Buttons.clear_toggle = False
							event.handled = True
						elif Notes.accum_on == True and Buttons.clear_toggle == False:
							Notes.accum_on = False
							ui.setHintMsg("Accumulator Off")
						elif Notes.accum_on == False and Buttons.clear_toggle == False:
							Notes.accum_on = True	
							ui.setHintMsg("Accumulator On")
					else:	
						ui.enter()
						print('enter')
			

				elif event.data1 == data.pads["b"]:
					print('b')

				elif event.data1 == data.pads["c"]:
					channels.showCSForm(channels.channelNumber(), -1)
					print('c')
					
				elif event.data1 == data.pads["d"]:
					print('View Plugin Picker')
					transport.globalTransport(midi.FPT_F8, 67)
					event.handled = True	

				elif event.data1 == data.pads["e"]:
					print('e')
					self.push.mode_change()

				elif event.data1 == data.pads["f"]:
					print('sub-mode')
					self.push.sub_mode()

				elif event.data1 == data.pads["g"]:
					Buttons.g_iter += 1
					if Buttons.g_iter >= len(config.options['g_button']):
						Buttons.g_iter = 0
					ui.setFocused(config.options['g_button'][Buttons.g_iter])
					print(config.options['g_button'][Buttons.g_iter])

				elif event.data1 == data.pads['h']:
					if not ui.getFocused(1):						
						transport.globalTransport(midi.FPT_F6, 65)
					else:
						transport.globalTransport(midi.FPT_F9, 68)
					event.handled = True 				

	def note_gen(self):
		"""generates random notes. 0-65535 is the range of 16 bit numbers. note variable calls num_gen for random number which is mapped to index of note in chosen scale"""
		for i in range(patterns.getPatternLength(patterns.patternNumber())):
			note = data.scales[Buttons.scale][Buttons.root_note][int(mapvalues(num_gen(), 0 + Buttons.lower_limit, 
					len(data.scales[Buttons.scale][Buttons.root_note]) - Buttons.upper_limit, 0, 65535))]
			print(note)
			channels.setStepParameterByIndex(channels.selectedChannel(), patterns.patternNumber(), i, 0, note, 1)
			self.push.mode_init()

def num_gen():
	"""seeds and returns 16 bit random number"""
	rand_obj = _random.Random()
	rand_obj.seed()
	rand_int = rand_obj.getrandbits(16) 
	return rand_int 

def mapvalues(value, tomin, tomax, frommin, frommax):
	"""takes in value and range and returns value within another range"""
	input_value = value
	solution = tomin + (tomax-(tomin))*((input_value - frommin) / (frommax - (frommin)))
	if  -0.01 < solution < 0.01:
		solution = 0
	return solution

class PlusMinus:

	zero_status = True

	def __init__(self, event):
		self.mode = Modes(event)
		self.event = event
		self.plus_status = False
		self.minus_status = False
		self.status_maker()

	def status_maker(self):
		"""reads plus minus button midi data and calls act_out when button is pushed and midi cc is no longer 0 but ignores continued cc 
		data as to not retrigger until it button is released and cc is reset to 0"""
		if self.event.data2 > 64:
			if self.plus_status != True and PlusMinus.zero_status == True:
				self.plus_status = True
				PlusMinus.zero_status = False
				self.alter_something(1)
			elif self.plus_status == True:
				self.plus_status = False


		elif self.event.data2 < 64:
			if self.minus_status != True and PlusMinus.zero_status == True:
				self.minus_status = True
				PlusMinus.zero_status = False
				self.alter_something(-1)
			elif self.minus_status == True:
				self.minus_status = False

		elif self.event.data1 == 0 and self.event.data2 == 64:
			PlusMinus.zero_status = True
			self.plus_status = False
			self.minus_status = False		

	def alter_something(self, increment):
		self.mode.sub_sub_mode(increment)

