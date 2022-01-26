# name=Presonus Atom SQ MIDIIN2 0_01
# Author: ts-forgery
# Version .001


import device_presonusatomsq001 as trial
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
from direction import Directions
from lights import Lights
# from midi import *

def OnInit():
	print("Presonus Atom SQ MIDI2")
	# device.midiOutMsg(144, 94, 127, 0)

# class Incoming:

current_arrow = 0
arrow_index = 0
# arrow_status = False
# def OnMidiMsg(event):
# 	print(event.midiId, event.data1, event.data2, event.midiChan, event.midiChanEx)

def OnMidiIn(event):
	global current_arrow
	global arrow_index
	# global arrow_status


	print(event.data1, event.data2)
	if event.data2 > 0:
		
		if event.data1 not in data.ud_arrow:
			Directions.arrow_status = False

		if event.data1 == data.tsport["play"]:
			trial.play(event)
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

		elif event.data1 == data.tsport["metronome"]:	 
			print('Toggle Metronome')
			device.midiOutMsg(144, 0, 36, 127)
			# transport.globalTransport(midi.FPT_Metronome, 110)
			event.handled = True

		elif event.data1 == data.tsport["shift_play"]:
			transport.setLoopMode()
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

		elif event.data1 in data.buttons["mute"]: 
			if ui.getFocused(0):
				mixer.muteTrack(mixer.trackNumber())
				event.handled = True

			elif ui.getFocused(1):
				channels.muteChannel(channels.channelNumber())	
				event.handled = True	
			
			else:
				event.handled = True		

		elif event.data1 in data.ud_arrow:
			direct = Directions(event)

		elif event.data1 in data.buttons["arm"]:
			print('arm track')
			if ui.getFocused(0):
				mixer.armTrack(mixer.trackNumber())
				event.handled = True
			elif ui.getFocused(1):
				mixer.linkTrackToChannel(0)
		# elif event.data1 == data.buttons["zoom"]: 

		elif event.data1 == data.pads['left_arrow']:
			ui.left()
			event.handled = True

		elif event.data1 == data.pads['right_arrow']:
			ui.right()
			event.handled = True

		elif event.data1 == data.knobs["jog_wheel"]:
			print('jogging')
			if ui.getFocused(1):
				if event.data2 == 65:
					print('channels focused')
					if channels.channelNumber() > 0:
						channels.selectOneChannel(channels.channelNumber() - 1)
						Lights.update_pattern()
						print("selectOneChannel")
						event.handled = True

			


				elif event.data2 == 1:
					if channels.channelNumber() < channels.channelCount() - 1:
						channels.selectOneChannel(channels.channelNumber() + 1)

						event.handled = True
					else:
						print('Channels Maxed')


			elif ui.getFocused(0):
				if event.data2 == 65:
					if mixer.trackNumber() > 0:
						mixer.setTrackNumber(mixer.trackNumber() - 1)
						event.handled = True

				elif event.data2 == 1:
					mixer.setTrackNumber(mixer.trackNumber() + 1)
					event.handled = True
		else:
			event.handled = True



# incoming_midi = Incoming()

# def OnMidiMsg(event):
# 	incoming_midi.OnMidiMsg(event)

