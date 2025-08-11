import patterns
import channels
import transport
import mixer
import midi 
import state

active = True

arrangement_count = 0

song_data = {
	0:	{
		'name': 'live_set_3',
		'bpm': {
			'default': 127,
			1: 123.0,
			2: 135.1,
			},
		'arrangement': {
			1: [0],
			2: [2, 4, 4, 1],
			3: [5],
			4: [7, 23, 23],
			5: [0],
			6: [0],
			7: [0],
			8: [0],
			9: [0],
			10: [0],
			11: [0],
			12: [0],
			13: [0],
			14: [0],
			15: [0],
			16: [0],
		}
		},
}	

def set_pattern(state):
	pattern_to_set = patterns.patternNumber()
	preset = state.song_data_index

	if pattern_to_set in song_data[preset]['bpm']:
		set_pattern_tempo(song_data[preset]['bpm'][pattern_to_set])
	elif song_data[preset]['bpm']['default']:
		set_pattern_tempo(song_data[preset]['bpm']['default'])

def set_pattern_tempo(new_tempo):
	current_bpm = mixer.getCurrentTempo()
	target_bpm = new_tempo * 1000
	bpm_difference = target_bpm - current_bpm
	bpm_to_add_scaled = bpm_difference / 100
	bpm_to_add_int = int(round(bpm_to_add_scaled))
	transport.globalTransport(midi.FPT_TempoJog, bpm_to_add_int)

def set_arrangement(state):
	global arrangement_count
	active_arrangements = song_data[state.song_data_index]['arrangement']
	arrangement_count += 1
	if arrangement_count >= len(active_arrangements[state.active_arrangement]):
		arrangement_count = 0
	if active_arrangements[state.active_arrangement][arrangement_count]:
		patterns.jumpToPattern(active_arrangements[state.active_arrangement][arrangement_count])