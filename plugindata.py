# plugin data is stored here
# If you want to set knobs to control a plugin get the paramter data by assigning a 
knobs = [x for x in range(14, 47)]
touchpad = 1
knob_numbers = [touchpad] + knobs

plugin_names = ('Transistor Bass', 'Drumpad', 'Fruity DX10')
drum_plugs = ('FPC', ) # 'Slicex',
atom_sq_pads = [x for x in range(36, 68)]
FPC_pads = (37, 36, 42, 54, 40, 38, 46, 44, 48, 47, 45, 43, 49, 55, 51, 53, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75)

plugin_dict = {
	'Fruity Dance': [0, 5, 6, 4, 1, 2, 3],
	'Transistor Bass': [0, 1, 2, 4, 5, 6, 7, 8, 9, 10, 3, 13, 12, 11, 40, 34, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 6, 27, 28, 29, 30, 31, 32, 33, 0, 0, 0, ],
	'Drumpad': [7, 2, 3, 4, 5, 0, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 1, 24, 25, 26, 28, 27, 29, 34, 35, 36],
	'Fruity DX10': [0, 1, 2, 11, 21, 13, 10, 3, 4, 9, 12, 5, 6, 7, 8, 14, 14, 15, 20, 16, 17, 18, 19, 0, 0, 0, 0, 0],
	'Ogun': [17, 18, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
	'3x Osc': [1, 2, 3, 4, 5, 0, 8, 9, 10, 11, 12, 7, 6, 15, 16, 17, 18, 19, 14, 13, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	'GMS': [i for i in range(32, 70)],
	'Fruity granulizer': [0, 1, 2, 3, 7, 4, 5, 6, 8, 9 , 10 , 11, 12, 13, 14, 15],
	'Harmless': [54, 3, 59, 52, 56, 26, 27, 28, 31, ],
	'Toxic Biohazard': [15, 16, 0, 1, 2, 3, 4, 5, 6],
	'FLEX': [21, 22, 10, 11, 12, 13, 14, 15],
	'Poizone': [18, 29, 33, 22, 23, 24, 25, 18, 19, 20, 66, 0, 1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42]
	
			 }
# poizone ={
# 	{'Osc A shape': 0, 'Osc A PW': 1, 'Osc A sync': 2, 'Osc A ring': 3, 'Osc B shape': 4, 'Osc B PW': 5, 'Osc B pitch': 6, 
# 	'Osc B detune': 7, 'Osc balance': 8, 'Noise balance': 9, 'EG amount': 10, 'EG attack': 11, 'EG decay': 12, 
# 	'EG sustain': 13, 'EG release': 14, 'Gain': 15, 'Fine tune': 16, 'Transpose': 17, 'Filter cutoff': 18, 
# 	'Filter resolution': 19, 'Filter keytrack': 20, 'Filter veltrk': 21, 'Amplifier attack': 22, 'Amplifier decay': 23, 
# 	'Amplifier sustain': 24, 'Amplifier release': 25, 'LFO amount': 26, 'LFO retrig': 27, 'LFO rate': 28, 
# 	'Unison detune': 29, 'Unison pan': 30, 'Delay on': 31, 'Delay time left': 32, 'Delay time right': 33, 
# 	'Delay feedback': 34, 'Delay mod. depth': 35, 'Delay lo-cut': 36, 'Delay hi-cut': 37, 'Delay wet': 38, 
# 	'Chorus on': 39, 'Chorus rate': 40, 'Chorus depth': 41, 'Chorus wet': 42, 'MW amount': 43, 'Monophonic': 44, 
# 	'Octaver': 45, 'Glide time': 46, 'Gate mix': 47, 'Gate smooth': 48, 'Gate step 1': 49, 'Gate step 2': 50, 
# 	'Gate step 3': 51, 'Gate step 4': 52, 'Gate step 5': 53, 'Gate step 6': 54, 'Gate step 7': 55, 'Gate step 8': 56, 
# 	'Gate step 9': 57, 'Gate step 10': 58, 'Gate step 11': 59, 'Gate step 12': 60, 'Gate step 13': 61, 'Gate step 14': 62, 
# 	'Gate step 15': 63, 'Gate step 16': 64, 'Envelope destination': 65, 'Filter mode': 66, 'LFO destination': 67, 
# 	'LFO shape': 68, 'Arpegiator mode': 69, 'Arpegiator range': 70, 'ModWheel destination': 71, 'Glide held': 72, 
# 	'Glide static': 73,}

# ogun = {'Master level': 0, 'Master coarse pitch': 1, 'Master fine pitch': 2, 'Modulation X': 3, 'Modulation Y': 4, 'Timbre pre-decay': 5, 
# 			'Timbre decay time': 6, 'Timbre release time': 7, 'Timbre fullness': 8, 'Timbre morphing / randomness': 9, 'Timbre seed 1': 10, 
# 			'Timbre seed 2': 11, 'Unison order': 12, 'Unison panning': 13, 'Unison volume': 14, 'Unison pitch': 15, 'Unison phase': 16, 'Filter frequency': 17, 'Filter resonance': 18, 
# 			'Chorus order': 19, 'Chorus depth': 20, 'Chorus speed': 21, 'Chorus delay': 22, 'Chorus spread': 23, 'Chorus cross': 24, 'Chorus mix': 25, 'Delay feedback level': 26, 
# 			'Delay time': 27, 'Delay time stereo offset': 28, 'Delay volume': 29, 'Delay feedback mode': 30, 'Reverb lowcut': 31, 'Reverb highcut': 32, 'Reverb predelay': 33, 'Reverb room size': 34, 
# 			'Reverb diffusion': 35, 'Reverb decay': 36, 'Reverb high damping': 37, 'Reverb color': 38, 'Reverb wet volume': 39, 'EQ band 1 level': 40, 'EQ band 2 level': 41, 'EQ band 3 level': 42, 'EQ band 1 freq': 43, 'EQ band 2 freq': 44, 
# 			'EQ band 3 freq': 45, 'EQ band 1 width': 46, 'EQ band 2 width': 47, 'EQ band 3 width': 48, 'Volume - Attack time scale': 49, 'Volume - Decay time scale': 50, 'Volume - Sustain level offset': 51, 
# 			'Volume - Release time scale': 52, 'Volume - LFO speed (phase)': 53, 'Volume - LFO tension': 54, 'Volume - LFO skew': 55, 'Volume - LFO pulse width': 56, 'Filter frequency - Attack time scale': 57, 
# 			'Filter frequency - Decay time scale': 58, 'Filter frequency - Sustain level offset': 59, 'Filter frequency - Release time scale': 60, 'Filter frequency - LFO speed (phase)': 61, 'Filter frequency - LFO tension': 62, 
# 			'Filter frequency - LFO skew': 63, 'Filter frequency - LFO pulse width': 64, 'Filter resonance - Attack time scale': 65, 'Filter resonance - Decay time scale': 66, 'Filter resonance - Sustain level offset': 67, 
# 			'Filter resonance - Release time scale': 68, 'Filter resonance - LFO speed (phase)': 69, 'Filter resonance - LFO tension': 70, 'Filter resonance - LFO skew': 71, 'Filter resonance - LFO pulse width': 72, 
# 			'Pitch - Attack time scale': 73, 'Pitch - Decay time scale': 74, 'Pitch - Sustain level offset': 75, 'Pitch - Release time scale': 76, 'Pitch - LFO speed (phase)': 77, 'Pitch - LFO tension': 78, 'Pitch - LFO skew': 79, 
# 			'Pitch - LFO pulse width': 80, 'Unison pitch - Attack time scale': 81, 'Unison pitch - Decay time scale': 82, 'Unison pitch - Sustain level offset': 83, 'Unison pitch - Release time scale': 84, 'Unison pitch - LFO speed (phase)': 85, 
# 			'Unison pitch - LFO tension': 86, 'Unison pitch - LFO skew': 87, 'Unison pitch - LFO pulse width': 88}
# toxic_biohazard = {'Gain': 0, 'Distortion': 1, 'Transpose': 2, 'Master Atk': 3, 'Master Dec': 4, 'Master Sus': 5, 'Master Rel': 6, 
# 					'Vel. Curve': 7, 'Unison Dtn': 8, 'Unison Pan': 9, 'Glide Time': 10, 'EGF to Pitch': 11, 'Lfo2 to Pitch': 12, 'Lfo1 Speed': 13, 
# 					'Lfo2 Speed': 14, 'Flt Cutoff': 15, 'Flt Res': 16, 'Flt KeyTrk': 17, 'Flt VelTrk': 18, 'Flt EG Atk': 19, 'Flt EG Dec': 20, 
# 					'Flt EG Sus': 21, 'Flt EG Rel': 22, 'Flt Eg Amnt': 23, 'Flt Lfo1 Amnt': 24, 'O1 Enable': 25, 'O2 Enable': 26, 'O3 Enable': 27, 
# 					'O4 Enable': 28, 'O5 Enable': 29, 'O6 Enable': 30, 'O1 Coarse': 31, 'O2 Coarse': 32, 'O3 Coarse': 33, 'O4 Coarse': 34, 'O5 Coarse': 35, 
# 					'O6 Coarse': 36, 'O1 Fine': 37, 'O2 Fine': 38, 'O3 Fine': 39, 'O4 Fine': 40, 'O5 Fine': 41, 'O6 Fine': 42, 'O1 Frq Shift': 43, 'O2 Frq Shift': 44, 
# 					'O3 Frq Shift': 45, 'O4 Frq Shift': 46, 'O5 Frq Shift': 47, 'O6 Frq Shift': 48, 'O1 Free Run': 49, 'O2 Free Run': 50, 'O3 Free Run': 51, 'O4 Free Run': 52, 
# 					'O5 Free Run': 53, 'O6 Free Run': 54, 'O1 Phase': 55, 'O2 Phase': 56, 'O3 Phase': 57, 'O4 Phase': 58, 'O5 Phase': 59, 'O6 Phase': 60, 'O1 VelSens': 61, 'O2 VelSens': 62, 
# 					'O3 VelSens': 63, 'O4 VelSens': 64, 'O5 VelSens': 65, 'O6 VelSens': 66, 'O1 Init': 67, 'O2 Init': 68, 'O3 Init': 69, 'O4 Init': 70, 'O5 Init': 71, 'O6 Init': 72, 
# 					'O1 Atk': 73, 'O2 Atk': 74, 'O3 Atk': 75, 'O4 Atk': 76, 'O5 Atk': 77, 'O6 Atk': 78, 'O1 Dec': 79, 'O2 Dec': 80, 'O3 Dec': 81, 'O4 Dec': 82, 'O5 Dec': 83, 'O6 Dec': 84, 
# 					'O1 Sus': 85, 'O2 Sus': 86, 'O3 Sus': 87, 'O4 Sus': 88, 'O5 Sus': 89, 'O6 Sus': 90, 'O1 Rel': 91, 'O2 Rel': 92, 'O3 Rel': 93, 'O4 Rel': 94, 'O5 Rel': 95, 'O6 Rel': 96, 
# 					'O1 Pan': 97, 'O2 Pan': 98, 'O3 Pan': 99, 'O4 Pan': 100, 'O5 Pan': 101, 'O6 Pan': 102, 'O1 Mix': 103, 'O2 Mix': 104, 'O3 Mix': 105, 'O4 Mix': 106, 'O5 Mix': 107, 'O6 Mix': 108, 
# 					'O1 Fm 1': 109, 'O2 Fm 1': 110, 'O3 Fm 1': 111, 'O4 Fm 1': 112, 'O5 Fm 1': 113, 'O6 Fm 1': 114, 'O1 Fm 2': 115, 'O2 Fm 2': 116, 'O3 Fm 2': 117, 'O4 Fm 2': 118, 'O5 Fm 2': 119, 
# 					'O6 Fm 2': 120, 'O1 Fm 3': 121, 'O2 Fm 3': 122, 'O3 Fm 3': 123, 'O4 Fm 3': 124, 'O5 Fm 3': 125, 'O6 Fm 3': 126, 'O1 Fm 4': 127, 'O2 Fm 4': 128, 'O3 Fm 4': 129, 'O4 Fm 4': 130, 'O5 Fm 4': 131, 'O6 Fm 4': 132, 'O1 Fm 5': 133, 'O2 Fm 5': 134, 'O3 Fm 5': 135, 'O4 Fm 5': 136, 'O5 Fm 5': 137, 'O6 Fm 5': 138, 'O1 Fm 6': 139, 'O2 Fm 6': 140, 'O3 Fm 6': 141, 'O4 Fm 6': 142, 'O5 Fm 6': 143, 'O6 Fm 6': 144, 'LFO1 Osc1': 145, 'LFO1 Osc2': 146, 'LFO1 Osc3': 147, 'LFO1 Osc4': 148, 'LFO1 Osc5': 149, 'LFO1 Osc6': 150, 'LFO2 Osc1': 151, 'LFO2 Osc2': 152, 'LFO2 Osc3': 153, 'LFO2 Osc4': 154, 'LFO2 Osc5': 155, 'LFO2 Osc6': 156, 'Seq Play': 157, 'Seq Swing': 158, 'Seq P-P': 159, 'Seq Rnd': 160, 'Seq Dual': 161, 'Seq Steps': 162, 'Seq Ptrn 0': 163, 'Seq Ptrn 1': 164, 'Seq Ptrn 2': 165, 'Seq Ptrn 3': 166, 'Seq Ptrn 4': 167, 'Seq Ptrn 5': 168, 'Seq Ptrn 6': 169, 'Seq Ptrn 7': 170, 'Seq Ptrn 8': 171, 'Seq Ptrn 9': 172, 'Seq Ptrn 10': 173, 'Seq Ptrn 11': 174, 'Seq Ptrn 12': 175, 'Seq Ptrn 13': 176, 'Seq Ptrn 14': 177, 'Seq Ptrn 15': 178, 'Seq Ptrn 16': 179, 'Seq Ptrn 17': 180, 'Seq Ptrn 18': 181, 'Seq Ptrn 19': 182, 'Seq Ptrn 20': 183, 'Seq Ptrn 21': 184, 'Seq Ptrn 22': 185, 'Seq Ptrn 23': 186, 'Seq Ptrn 24': 187, 'Seq Ptrn 25': 188, 'Seq Ptrn 26': 189, 'Seq Ptrn 27': 190, 'Seq Ptrn 28': 191, 'Seq Ptrn 29': 192, 'Seq Ptrn 30': 193, 'Seq Ptrn 31': 194, 'Seq Ptrn 32': 195, 'Seq Ptrn 33': 196, 'Seq Ptrn 34': 197, 'Seq Ptrn 35': 198, 'Seq Ptrn 36': 199, 'Seq Ptrn 37': 200, 'Seq Ptrn 38': 201, 'Seq Ptrn 39': 202, 'Seq Ptrn 40': 203, 'Seq Ptrn 41': 204, 'Seq Ptrn 42': 205, 'Seq Ptrn 43': 206, 'Seq Ptrn 44': 207, 'Seq Ptrn 45': 208, 'Seq Ptrn 46': 209, 'Seq Ptrn 47': 210, 'Seq Ptrn 48': 211, 'Seq Ptrn 49': 212, 'Seq Ptrn 50': 213, 'Seq Ptrn 51': 214, 'Seq Ptrn 52': 215, 'Seq Ptrn 53': 216, 'Seq Ptrn 54': 217, 'Seq Ptrn 55': 218, 'Seq Ptrn 56': 219, 'Seq Ptrn 57': 220, 'Seq Ptrn 58': 221, 'Seq Ptrn 59': 222, 'Seq Ptrn 60': 223, 'Seq Ptrn 61': 224, 'Seq Ptrn 62': 225, 'Seq Ptrn 63': 226, 'EQ On ': 227, 'EQ Band1': 228, 'EQ Band2': 229, 'EQ Band3': 230, 'EQ Band4': 231, 'EQ Band5': 232, 'EQ Band6': 233, 'EQ Band7': 234, 'EQ Band8': 235, 'Fx1 Enable': 236, 'Fx2 Enable': 237, 'Flang1 Delay': 238, 'Flang2 Delay': 239, 'Flang1 Fdbk': 240, 'Flang2 Fdbk': 241, 'Flang1 Depth': 242, 'Flang2 Depth': 243, 'Flang1 Rate': 244, 'Flang2 Rate': 245, 'Flang1 Mix': 246, 'Flang2 Mix': 247, 'Flang1 -Fdbk': 248, 'Flang2 Inv. Fdbk': 249, 'Flang1 -Mix': 250, 'Flang2 Inv. Mix': 251, 'Chor1 Depth': 252, 'Chor2 Depth': 253, 'Chor1 Rate': 254, 'Chor2 Rate': 255, 'Chor1 Mix': 256, 'Chor2 Mix': 257, 'Rev1 Mix': 258, 'Rev2 Mix': 259, 'Rev1 Decay': 260, 'Rev2 Decay': 261, 'Rev1 Damp': 262, 'Rev2 Damp': 263, 'Rev1 Hi-Cut': 264, 'Rev2 Hi-Cut': 265, 'Delay1 Time': 266, 'Delay2 Time': 267, 'Delay1 Fdbk': 268, 'Delay2 Fdbk': 269, 'Delay1 Rate': 270, 'Delay2 Rate': 271, 'Delay1 Depth': 272, 'Delay2 Depth': 273, 'Delay1 Blur': 274, 'Delay2 Blur': 275, 'Delay1 Mix': 276, 'Delay2 Mix': 277, 'LoFi1 Bits': 278, 'LoFi2 Bits': 279, 'LoFi1 Smp': 280, 'LoFi2 Smp': 281, 'LoFi1 Flt': 282, 'LoFi2 Flt': 283, 'Phas1 Frq': 284, 'Phas2 Frq': 285, 'Phas1 Rate': 286, 'Phas2 Rate': 287, 'Phas1 Dpth': 288, 'Phas2 Dpth': 289, 'Phas1 Fdbk': 290, 'Phas2 Fdbk': 291, 'Phas1 Mix': 292, 'Phas2 Mix': 293,  'Chn. Aftertouch': 422}
# sawer = {			'Master Level': 0, 
# 					'Master Pan': 1, 
# 					'Master Attack': 2, 
# 					'Master Decay': 3, 
# 					'Master Sustain': 4, 
# 					'Master Release': 5, 

# 					'Transpose': 6, 
# 					'Fine Tune': 7, 
# 					'Mono Mode': 8, 
# 					'Glide TimeMode': 9, 
# 					'Glide KeyMode': 10, 
# 					'Glide Time': 11, 
# 					'Octaver': 12, 

# 					'Unison Rtrg': 13, 
# 					'Unison': 14, 
# 					'Unison Detune': 15, 
# 					'Unison Pan': 16, 
# 					'Sub-Saw Phs': 17, 
# 					'Sub-Saw Hrm': 18, 

# 					'Sub-Saw Level': 19, 
# 					'Sub-Saw Detune': 20, 
# 					'Sub-Saw Retrig': 21, 
# 					'Sub-Saw Invert': 22, 
# 					'Sub-Saw Square': 23, 
# 					'Osc Sync Frq': 24, 


# 					'Osc Sync': 25, 
# 					'Noise Level': 26, 
# 					'Filter Cutoff': 27, 
# 					'Filter Reso': 28, 
# 					'Filter KeyTrk': 29, 
# 					'Filter VelTrk': 30, 
# 					'Filter Mode': 31, 

# 					'EGF Attack': 32, 
# 					'EGF Decay': 33, 
# 					'EGF Sustain': 34, 
# 					'EGF Release': 35, 
# 					'EGF Amount': 36, 
# 					'EGF Dest': 37, 
# 					'LFO Shape': 38, 
# 					'LFO Speed': 39, 
# 					'LFO Tmp Sync': 40, 
# 					'LFO Attack': 41, 
# 					'LFO Release': 42, 
# 					'LFO Retrig': 43, 
# 					'LFO Invert': 44, 
# 					'LFO Amount': 45, 
# 					'LFO Dest': 46, 
# 					'Chorus On': 47, 
# 					'Chorus Depth': 48, 
# 					'Chorus Rate': 49, 
# 					'Chorus Mix': 50, 
# 					'Phaser On': 51, 
# 					'Phaser Center': 52, 
# 					'Phaser Rate': 53, 
# 					'Phaser Depth': 54, 
# 					'Phaser Fdbk': 55, 
# 					'Phaser Mix': 56, 
# 					'Delay On': 57, 
# 					'Delay Left': 58, 
# 					'Delay Right': 59, 
# 					'Delay Fdbk': 60, 
# 					'Delay Depth': 61, 
# 					'Delay LoCut': 62, 
# 					'Delay HiCut': 63, 
# 					'Delay Mix': 64, 
# 					'Reverb On': 65, 
# 					'Reverb Decay': 66, 
# 					'Reverb HiCut': 67, 
# 					'Reverb Damp': 68, 
# 					'Reverb Mix': 69, 
# 					'Arp Play': 70, 
# 					'Arp Mode': 71, 
# 					'Arp Range': 72, 
# 					 'Chn. Aftertouch': 201}


# flex = {			'Volume envelope attack': 0, 
# 					'Volume envelope hold': 1, 
# 					'Volume envelope decay': 2, 
# 					'Volume envelope sustain': 3, 

# 					'Volume envelope release': 4, 
# 					'Filter envelope attack': 5, 
# 					'Filter envelope hold': 6, 
# 					'Filter envelope decay': 7, 

# 					'Filter envelope sustain': 8, 
# 					'Filter envelope release': 9, 
# 					'Filter': 10, 
# 					'Vibrato': 11, 
# 					'Unison': 12, 
# 					'Character': 13, 

# 					'Reverb': 38, 
# 					'Delay': 37, 
# 					'Not Used': 17, 
# 					'Filter cutoff': 18, 
# 					'Filter env amt': 19, 
# 					'Filter resonance': 20, 

# 					'Master filter cutoff': 21, 
# 					'Master filter resonance': 22, 
# 					'': 43, 
# 					'Delay mix': 25, 
# 					'Delay time': 26, 
# 					'Delay feedback': 27, 

# 					'Delay mod': 28, 
# 					'Delay color': 29, 
# 					'Reverb mix': 30, 
# 					'Reverb decay': 31, 
# 					'Reverb size': 32, 
# 					'Reverb mod': 33, 
# 					'Reverb color': 34, 

# 					'Limiter pre volume': 35, 
# 					'Output volume': 36, 
# 					'Pitch': 39, 
# 					'Master filter': 40, 
# 					'Limiter': 41, 
# 					'LMH Mix': 42, 
# 					'Reverb Mod speed': 44
# 					}

# dx10 = {			'Attack': 0, 
# 					'Decay': 1, 
# 					'Release': 2, 
# 					'Mod 1 Coarse': 3, 
# 					'Mod 1 Fine': 4, 
# 					'Mod 1 Init': 5, 
# 					'Mod 1 Decay': 6, 
# 					'Mod 1 Sustain': 7, 
# 					'Mod 1 Release': 8, 
# 					'Mod 1 Velocity': 9, 
# 					'Vibrato': 10, 
# 					'Waveform': 11, 
# 					'Mod Thru': 12, 
# 					'LFO Rate': 13, 

# 					'Mod 2 Coarse': 14, 
# 					'Mod 2 Fine': 15, 
# 					'Mod 2 Init': 16, 
# 					'Mod 2 Decay': 17, 
# 					'Mod 2 Sustain': 18, 
# 					'Mod 2 Release': 19, 

# 					'Mod 2 Velocity': 20, 
# 					'Coarse': 21}

# gms = {				'FX 1': 0, 
# 					'FX 2': 1, 
# 					'FX 3': 2, 
# 					'FX 4': 3, 
# 					'FX 5': 4, 
# 					'FX 6': 5, 
# 					'FX 7': 6, 
# 					'FX 8': 7, 
# 					'FX 9': 8, 
# 					'FX 10': 9, 
# 					'FX Activate': 10, 
# 					'FX Glue': 11, 
# 					'FX LFO Rate': 12, 
# 					'FX LFO Amount': 13, 
# 					'FX LFO Shape Switch': 14, 
# 					'FX LFO Shape': 15, 
# 					'FX LFO Sync Switch': 16, 
# 					'FX LFO Sync': 17, 
# 					'FX Param X': 18, 
# 					'FX Param Y': 19, 
# 					'CHN: Mix Level': 20, 
# 					'CHN: Panning': 21, 

# 					'CHN: Pitch': 22, 
# 					'CHN: Note Length': 23, 
# 					'CHN: Amp Attack': 24, 
# 					'CHN: Amp Decay': 25, 
# 					'CHN: Amp Sustain': 26, 
# 					'CHN: Amp Release': 27,
# 					'CHN: Amp Level': 28, 
# 					'CHN: Shuffle Enable': 29, 
# 					'CHN: Slide Time': 30, 
# 					'CHN: Slide Enable': 31, 
# 					'Filter Cutoff': 32, 
# 					'Filter Resonance': 33, 
# 					'Filter KBD Tracking': 34, 
# 					'Filter Type Switch': 35, 
# 					'Filter Type': 36, 
# 					'Envelope Number': 37, 
# 					'Envelope Destination Switch': 38, 
# 					'Envelope Destination': 39, 
# 					'Envelope Attack': 40, 
# 					'Envelope Decay': 41, 
# 					'Envelope Amount': 42, 
# 					'Envelope Invert': 43, 
# 					'LFO Number': 44, 
# 					'LFO Rate': 45, 
# 					'LFO Amount': 46, 
# 					'LFO Retrig': 47, 
# 					'LFO Invert': 48, 
# 					'LFO Sync Switch': 49, 
# 					'LFO Sync': 50, 
# 					'LFO Destination Switch': 51, 
# 					'LFO Destination': 52, 
# 					'LFO Shape Switch': 53, 
# 					'LFO Shape': 54, 
# 					'SYNTH: Mono Voice': 55, 
# 					'SYNTH: Unison Voices': 56, 
# 					'SYNTH: Unison Detune': 57, 
# 					'SYNTH: Unison Stereo': 58, 
# 					'SYNTH: Octave': 59, 
# 					'SYNTH: Noise Mix': 60, 
# 					'SYNTH: Unison Phase': 61, 
# 					'SYNTH: Unison Phase Retrig': 62, 
# 					'SYNTH: Mix Oscllator 2': 63, 
# 					'SYNTH: Mix Oscillator 3': 64, 
# 					'SYNTH: Modulation': 65, 
# 					'SYNTH: Mod Kind': 66, 
# 					'SYNTH: Phase Offset Osc 2': 67, 
# 					'SYNTH: Phase Retrig Osc 2': 68, 
# 					'SYNTH: Osc 2 Invert': 69, 
# 					'SYNTH: Osc 1 Pitch': 70, 
# 					'SYNTH: Osc 1 Detune': 71, 
# 					'SYNTH: Osc 2 Pitch': 72, 
# 					'SYNTH: Osc 2 Detune': 73, 
# 					'SYNTH: Osc 3 Pitch': 74, 
# 					'SYNTH: Osc 3 Detune': 75, 
# 					'Chn. Aftertouch': 204}

####### DRUMPAD
# dp = {'Mallet retrig': 0, 'Retrig': 1, 'Mallet amplitude': 2, 'Mallet decay': 3, 'Mallet noise': 4, 
		# 'Mallet noise RP': 5, 'Membrane decay': 6, 'Membrane cutoff': 7, 'Membrane tension': 8, 'Membrane phase': 9, 
		# 'Membrane material': 10, 'Membrane size': 11, 'Membrane shape': 12, 'LOW frequency': 13, 'LOW reso': 14, 
		# 'SOF frequency': 15, 'SOF decay': 16, 'SOF level': 17, 'MID frequency': 18, 'MID level': 19, 'MID res': 20, 
		# 'MID frequency mod': 21, 'MID level mod': 22, 'MID attack': 23, 'HIGH frequency': 24, 'HIGH level': 25, 
		# 'HIGH res': 26, 'Lo-Fi': 27, 'Hold': 28, 'Pitch': 33, 'Velocity mod 1 value': 34, 'Velocity mod 2 value': 35, 
		# 'Velocity mod 3 value': 36, 'Velocity mod 4 value': 37}

# tb = {'Tuning': 0, 'Waveform': 1, 'Cutoff': 2, 'Cutoff key follow': 3, 'Resonance': 4, 'Envelope mod': 5, 'Decay': 6, 
# 		'Accent': 7, 'Volume': 8, 'HP': 9, 'Minimum decay': 10, 'Pulse width': 11, 'LFO -> Pulse width rate': 12, 
# 		'LFO -> Pulse width amount': 13, 'Reverb': 14, 'Reverb low cut': 15, 'Reverb high cut': 16, 'Reverb predelay': 17, 
# 		'Reverb predelay feedback': 18, 'Reverb room size': 19, 'Reverb diffusion': 20, 'Reverb decay': 21, 
# 		'Reverb high damp': 22, 'Reverb width': 23, 'Reverb dry amount': 24, 'Reverb early reflection amount': 25, 
# 		'Reverb wet amount': 26, 'Distortion': 27, 'Distortion HP': 28, 'Distortion drive': 29, 'Distortion tone': 30, 
# 		'Distortion volume': 31, 'Delay': 32, 'Delay BPM sync': 33, 'Delay amount': 34, 'Delay time': 35, 
# 		'Delay right tap point': 36, 'Delay feedback': 37, 'Delay tone': 38, 'Delay stereo': 39, 'Clicks': 40, '303 Pulse': 41
	
# 		}

# osc = {'Osc 1 panning': 0, 'Osc 1 shape': 1, 'Osc 1 coarse pitch': 2, 'Osc 1 fine pitch': 3, 'Osc 1 stereo phase offset': 4, 'Osc 1 stereo detune': 5, 
# 		'Osc 2 mix level': 6, 'Osc 2 panning': 7, 'Osc 2 shape': 8, 'Osc 2 coarse pitch': 9, 'Osc 2 fine pitch': 10, 
# 		'Osc 2 stereo phase offset': 11, 'Osc 2 stereo detune': 12, 'Osc 3 mix level': 13, 'Osc 3 panning': 14, 
# 		'Osc 3 shape': 15, 'Osc 3 coarse pitch': 16, 'Osc 3 fine pitch': 17, 'Osc 3 stereo phase offset': 18, 
# 		'Osc 3 stereo detune': 19, 'Stereo phase randomness': 20
	
# 		}
# harmless = {'Phase randomness': 0, 'Low harmonics protection': 1, 'Sub harmonic 1': 2, 'Sub harmonic 3': 3, 'Sub harmonic 4': 4, 
# 	'Timbre EQ band 1': 5, 'Timbre EQ band 2': 6, 'Timbre EQ band 3': 7, 'Timbre EQ band 4': 8, 'Timbre EQ band 5': 9, 
# 	'Timbre EQ band 6': 10, 'Harmonic mask 1/12': 11, 'Harmonic mask 2/12': 12, 'Harmonic mask 3/12': 13, 
# 	'Harmonic mask 4/12': 14, 'Harmonic mask 5/12': 15, 'Harmonic mask 6/12': 16, 'Harmonic mask 7/12': 17, 
# 	'Harmonic mask 8/12': 18, 'Harmonic mask 9/12': 19, 'Harmonic mask 10/12': 20, 'Harmonic mask 11/12': 21, 
# 	'Harmonic mask 12/12': 22, 'Harmonic mask mix': 23, 'Harmonic mask mix LFO amount': 24, 'Stereo tremolo depth': 25, 
# 	'Volume env attack length': 26, 'Volume env decay length': 27, 'Volume env release length': 28, 'Velocity to attack': 29, 
# 	'Release velocity to release': 30, 'Pluck decay length': 31, 'Velocity to pluck decay': 32, 'Alternate pluck mode': 33, 
# 	'Pluck uses harmonic mask': 34, 'Pluck only on release': 35, 'Master volume': 36, 'Velocity to volume': 37, 'Master pitch': 38, 
# 	'Detuning': 39, 'Grittiness': 40, 'Pitch vibrato depth': 41, 'Pitch LFO amount': 42, 'Portamento mode': 43, 'Monophonic mode': 44, 
# 	'Portamento / legato time': 45, 'Velocity / release to portamento / legato time': 46, 'Adaptive filter envelope mode': 47, 
# 	'Filter env attack length': 48, 'Filter env decay length': 49, 'Filter env attack slope': 50, 
# 	'Filter env decay slope': 51, 'Filter env amount': 52, 'Velocity to filter env amount': 53, 
# 	'Filter frequency': 54, 'Filter scale': 55, 'Filter width': 56, 'Key to filter frequency': 57, 
# 	'Filter LFO amount': 58, 'Resonance amount': 59, 'Resonance scale': 60, 'Resonance offset / noise length': 61, 
# 	'Resonance self-oscillation': 62, 'Adaptive width': 63, 'Track filter frequency motion': 64, 'Unison order': 65, 
# 	'Unison panning': 66, 'Unison pitch thickness': 67, 'Unison phase': 68, 'Unison variation': 69, 'Unison type': 70, 
# 	'Phaser mix': 71, 'Phaser scale': 72, 'Phaser width': 73, 'Phaser width LFO amount': 74, 'Phaser offset': 75, 
# 	'Phaser offset LFO amount': 76, 'Phaser offset motion speed': 77, 'Key to phaser offset': 78, 'Harmonizer mix': 79, 
# 	'Harmonizer width': 80, 'Harmonizer width LFO amount': 81, 'Velocity to harmonizer width': 82, 'Harmonizer strength': 83, 
# 	'Harmonizer type': 84, 'Harmonizer position': 85, 'LFO shape / source': 86, 'Global / retriggered LFO': 87, 'LFO attack': 88, 
# 	'LFO speed': 89, 'Chorus type': 90, 'Chorus mix': 91, 'Delay type': 92, 'Delay input level': 93, 'Delay feedback level': 94, 
# 	'Delay time': 95, 'Reverb type': 96, 'Reverb wet level': 97, 'Compression level': 98, 'Velocity to unison pitch thickness': 99}
