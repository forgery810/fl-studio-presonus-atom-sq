# plugin data is stored here

knob_num = [x for x in range(14, 47)]

plugin_names = ('Transistor Bass', 'Drumpad', 'Fruity DX10')
drum_plugs = ('Slicex', 'FPC')
atom_sq_pads = [x for x in range(36, 68)]
FPC_pads = (37, 36, 42, 54, 40, 38, 46, 44, 48, 47, 45, 43, 49, 55, 51, 53, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75)

plugin_dict = {
	'Transistor Bass': [0, 1, 2, 4, 5, 6, 7, 8, 9, 10, 3, 13, 12, 11, 40, 34, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 6, 27, 28, 29, 30, 31, 32, 33, 0, 0, 0, ],
	'Drumpad': [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0, 1, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 28, 27, 29, 34, 35, 36],
	'Fruity DX10': [0, 1, 2, 11, 21, 13, 10, 3, 4, 9, 12, 5, 6, 7, 8, 14, 14, 15, 20, 16, 17, 18, 19, 0, 0, 0, 0, 0],
	'Ogun': [17, 18, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
	'3x Osc': [1, 2, 3, 4, 5, 0, 8, 9, 10, 11, 12, 7, 6, 15, 16, 17, 18, 19, 14, 13, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	'GMS': [i for i in range(32, 70)],
			 }

dp = {'<reserved>': 37, 'Mallet Amplitude': 2, 'Mallet Decay': 3, 'Mallet Noise': 4, 'Mallet Noise RP': 5, 'Membrane Decay': 6, 
		'Membrane Cutoff': 7, 'Membrane Tension': 8, 'Membrane Phase': 9, 'Membrane Material': 10, 'Membrane Size': 11, 
		'Membrane Shape': 12, 'LOW Freq': 13, 'LOW Res': 14, 'SOF Freq': 15, 'SOF Decay': 16, 'SOF Level': 17, 'MID Freq': 18, 
		'MID Level': 19, 'MID Res': 20, 'MID Freq Mod': 21, 'MID Level Mod': 22, 'MID Attack': 23, 'HIGH Freq': 24, 'HIGH Level': 25, 
		'HIGH Res': 26, 'Lo-Fi': 27, 'Hold': 28, 'Pitch': 29, 'MIDI CC 0': 38, 'MIDI CC 1': 39, 'MIDI CC 2': 40, 'MIDI CC 3': 41, 
		'MIDI CC 4': 42, 'MIDI CC 5': 43, 'MIDI CC 6': 44, 'MIDI CC 7': 45, 'MIDI CC 8': 46, 'MIDI CC 9': 47, 'MIDI CC 10': 48, 
		}

tb = {'Tuning': 0, 'Waveform': 1, 'Cutoff': 2, 'Cutoff key follow': 3, 'Resonance': 4, 'Envelope mod': 5, 'Decay': 6, 
		'Accent': 7, 'Volume': 8, 'HP': 9, 'Minimum decay': 10, 'Pulse width': 11, 'LFO -> Pulse width rate': 12, 
		'LFO -> Pulse width amount': 13, 'Reverb': 14, 'Reverb low cut': 15, 'Reverb high cut': 16, 'Reverb predelay': 17, 
		'Reverb predelay feedback': 18, 'Reverb room size': 19, 'Reverb diffusion': 20, 'Reverb decay': 21, 
		'Reverb high damp': 22, 'Reverb width': 23, 'Reverb dry amount': 24, 'Reverb early reflection amount': 25, 
		'Reverb wet amount': 26, 'Distortion': 27, 'Distortion HP': 28, 'Distortion drive': 29, 'Distortion tone': 30, 
		'Distortion volume': 31, 'Delay': 32, 'Delay BPM sync': 33, 'Delay amount': 34, 'Delay time': 35, 
		'Delay right tap point': 36, 'Delay feedback': 37, 'Delay tone': 38, 'Delay stereo': 39, 'Clicks': 40, '303 Pulse': 41
		}

osc = {'Osc 1 panning': 0, 'Osc 1 shape': 1, 'Osc 1 coarse pitch': 2, 'Osc 1 fine pitch': 3, 'Osc 1 stereo phase offset': 4, 'Osc 1 stereo detune': 5, 
		'Osc 2 mix level': 6, 'Osc 2 panning': 7, 'Osc 2 shape': 8, 'Osc 2 coarse pitch': 9, 'Osc 2 fine pitch': 10, 
		'Osc 2 stereo phase offset': 11, 'Osc 2 stereo detune': 12, 'Osc 3 mix level': 13, 'Osc 3 panning': 14, 
		'Osc 3 shape': 15, 'Osc 3 coarse pitch': 16, 'Osc 3 fine pitch': 17, 'Osc 3 stereo phase offset': 18, 
		'Osc 3 stereo detune': 19, 'Stereo phase randomness': 20
		}
hl = {'Phase randomness': 0, 'Low harmonics protection': 1, 'Sub harmonic 1': 2, 'Sub harmonic 3': 3, 'Sub harmonic 4': 4, 'Timbre EQ band 1': 5, 'Timbre EQ band 2': 6, 'Timbre EQ band 3': 7, 'Timbre EQ band 4': 8, 'Timbre EQ band 5': 9, 'Timbre EQ band 6': 10, 'Harmonic mask 1/12': 11, 'Harmonic mask 2/12': 12, 'Harmonic mask 3/12': 13, 'Harmonic mask 4/12': 14, 'Harmonic mask 5/12': 15, 'Harmonic mask 6/12': 16, 'Harmonic mask 7/12': 17, 'Harmonic mask 8/12': 18, 'Harmonic mask 9/12': 19, 'Harmonic mask 10/12': 20, 'Harmonic mask 11/12': 21, 'Harmonic mask 12/12': 22, 'Harmonic mask mix': 23, 'Harmonic mask mix LFO amount': 24, 'Stereo tremolo depth': 25, 'Volume env attack length': 26, 'Volume env decay length': 27, 'Volume env release length': 28, 'Velocity to attack': 29, 'Release velocity to release': 30, 'Pluck decay length': 31, 'Velocity to pluck decay': 32, 'Alternate pluck mode': 33, 'Pluck uses harmonic mask': 34, 'Pluck only on release': 35, 'Master volume': 36, 'Velocity to volume': 37, 'Master pitch': 38, 'Detuning': 39, 'Grittiness': 40, 'Pitch vibrato depth': 41, 'Pitch LFO amount': 42, 'Portamento mode': 43, 'Monophonic mode': 44, 'Portamento / legato time': 45, 'Velocity / release to portamento / legato time': 46, 'Adaptive filter envelope mode': 47, 'Filter env attack length': 48, 'Filter env decay length': 49, 'Filter env attack slope': 50, 'Filter env decay slope': 51, 'Filter env amount': 52, 'Velocity to filter env amount': 53, 'Filter frequency': 54, 'Filter scale': 55, 'Filter width': 56, 'Key to filter frequency': 57, 'Filter LFO amount': 58, 'Resonance amount': 59, 'Resonance scale': 60, 'Resonance offset / noise length': 61, 'Resonance self-oscillation': 62, 'Adaptive width': 63, 'Track filter frequency motion': 64, 'Unison order': 65, 'Unison panning': 66, 'Unison pitch thickness': 67, 'Unison phase': 68, 'Unison variation': 69, 'Unison type': 70, 'Phaser mix': 71, 'Phaser scale': 72, 'Phaser width': 73, 'Phaser width LFO amount': 74, 'Phaser offset': 75, 'Phaser offset LFO amount': 76, 'Phaser offset motion speed': 77, 'Key to phaser offset': 78, 'Harmonizer mix': 79, 'Harmonizer width': 80, 'Harmonizer width LFO amount': 81, 'Velocity to harmonizer width': 82, 'Harmonizer strength': 83, 'Harmonizer type': 84, 'Harmonizer position': 85, 'LFO shape / source': 86, 'Global / retriggered LFO': 87, 'LFO attack': 88, 'LFO speed': 89, 'Chorus type': 90, 'Chorus mix': 91, 'Delay type': 92, 'Delay input level': 93, 'Delay feedback level': 94, 'Delay time': 95, 'Reverb type': 96, 'Reverb wet level': 97, 'Compression level': 98, 'Velocity to unison pitch thickness': 99}

# touchpad_params controls how parameters react to touchpad. The name of each dictionary within touchpad_params must match the name
# of the Plugin exactly. Within wach plugin dict is a list of parameters the touchpad will change. It must follow this format:
# [number of parameter, value at 0 , value at 127] Value at 0 refers to what you want the value of that parameter to be when the knob is 
# fully closed (at 0) and Value at 127 is the value when knob is fully open. 0 is the minimum and 1.0 is the max. Look at the examples below for guidance.
# The line below can be deleted or can have a # put in front to deactivate them. 

touchpad_params = {
			'Transistor Bass': [[tb['Cutoff'], 1, .5], [tb['Waveform'], 0, .5], [tb['Resonance'], .5, 1], [tb['Envelope mod'], .5, 0]],
			'Drumpad':  [[dp['Membrane Cutoff'], 0, 1], [dp['Membrane Tension'], 0, .5], [dp['Membrane Size'], .75, 1]],
			'3x Osc': [[osc['Osc 1 fine pitch'], .4, .6], [osc['Osc 2 fine pitch'], .6, .8], [osc['Osc 3 fine pitch'], .3, .8],], 
			'Harmless': [[hl['Filter frequency'], .2, .85 ], [hl['Resonance amount'], .0, .5 ], [hl['Reverb wet level'], .3, .8] ]
			}





# ogun = {'Master level': 0, 'Master coarse pitch': 1, 'Master fine pitch': 2, 'Modulation X': 3, 'Modulation Y': 4, 'Timbre pre-decay': 5, 
			# 'Timbre decay time': 6, 'Timbre release time': 7, 'Timbre fullness': 8, 'Timbre morphing / randomness': 9, 'Timbre seed 1': 10, 
			# 'Timbre seed 2': 11, 'Unison order': 12, 'Unison panning': 13, 'Unison volume': 14, 'Unison pitch': 15, 'Unison phase': 16, 'Filter frequency': 17, 'Filter resonance': 18, 
			# 'Chorus order': 19, 'Chorus depth': 20, 'Chorus speed': 21, 'Chorus delay': 22, 'Chorus spread': 23, 'Chorus cross': 24, 'Chorus mix': 25, 'Delay feedback level': 26, 
			# 'Delay time': 27, 'Delay time stereo offset': 28, 'Delay volume': 29, 'Delay feedback mode': 30, 'Reverb lowcut': 31, 'Reverb highcut': 32, 'Reverb predelay': 33, 'Reverb room size': 34, 
			# 'Reverb diffusion': 35, 'Reverb decay': 36, 'Reverb high damping': 37, 'Reverb color': 38, 'Reverb wet volume': 39, 'EQ band 1 level': 40, 'EQ band 2 level': 41, 'EQ band 3 level': 42, 'EQ band 1 freq': 43, 'EQ band 2 freq': 44, 
			# 'EQ band 3 freq': 45, 'EQ band 1 width': 46, 'EQ band 2 width': 47, 'EQ band 3 width': 48, 'Volume - Attack time scale': 49, 'Volume - Decay time scale': 50, 'Volume - Sustain level offset': 51, 
			# 'Volume - Release time scale': 52, 'Volume - LFO speed (phase)': 53, 'Volume - LFO tension': 54, 'Volume - LFO skew': 55, 'Volume - LFO pulse width': 56, 'Filter frequency - Attack time scale': 57, 
			# 'Filter frequency - Decay time scale': 58, 'Filter frequency - Sustain level offset': 59, 'Filter frequency - Release time scale': 60, 'Filter frequency - LFO speed (phase)': 61, 'Filter frequency - LFO tension': 62, 
			# 'Filter frequency - LFO skew': 63, 'Filter frequency - LFO pulse width': 64, 'Filter resonance - Attack time scale': 65, 'Filter resonance - Decay time scale': 66, 'Filter resonance - Sustain level offset': 67, 
			# 'Filter resonance - Release time scale': 68, 'Filter resonance - LFO speed (phase)': 69, 'Filter resonance - LFO tension': 70, 'Filter resonance - LFO skew': 71, 'Filter resonance - LFO pulse width': 72, 
			# 'Pitch - Attack time scale': 73, 'Pitch - Decay time scale': 74, 'Pitch - Sustain level offset': 75, 'Pitch - Release time scale': 76, 'Pitch - LFO speed (phase)': 77, 'Pitch - LFO tension': 78, 'Pitch - LFO skew': 79, 
			# 'Pitch - LFO pulse width': 80, 'Unison pitch - Attack time scale': 81, 'Unison pitch - Decay time scale': 82, 'Unison pitch - Sustain level offset': 83, 'Unison pitch - Release time scale': 84, 'Unison pitch - LFO speed (phase)': 85, 
			# 'Unison pitch - LFO tension': 86, 'Unison pitch - LFO skew': 87, 'Unison pitch - LFO pulse width': 88}
