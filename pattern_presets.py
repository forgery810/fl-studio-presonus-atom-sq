import patterns
import channels
import transport
import mixer
import midi 
import state

active = True

pattern_data = {
	0:	{
		'name': 'live_set_3',
		'bpm': {
			'default': 127,
			1: 123.0,
			2: 135.1,
			}
		},
}	

def set_pattern(state):
	pattern_to_set = patterns.patternNumber()
	preset = state.pattern_data_index

	if pattern_to_set in pattern_data[preset]['bpm']:
		set_pattern_tempo(pattern_data[preset]['bpm'][pattern_to_set])
	elif pattern_data[preset]['bpm']['default']:
		set_pattern_tempo(pattern_data[preset]['bpm']['default'])

def set_pattern_tempo(new_tempo):
	current_bpm = mixer.getCurrentTempo()
	target_bpm = new_tempo * 1000
	bpm_difference = target_bpm - current_bpm
	bpm_to_add_scaled = bpm_difference / 100
	bpm_to_add_int = int(round(bpm_to_add_scaled))
	transport.globalTransport(midi.FPT_TempoJog, bpm_to_add_int)
