import ui
import config
from state import State

class Notes():
	something = 2
	upper_limit = -25
	lower_limit = 25
	note_list = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
	octaves = [-36, -24, -12, 0, 12, 24, 36]
	root = note_list.index(config.ROOT_NOTE)
	octave = 3

	def adjust_octave(increment):
		Notes.octave += increment
		if Notes.octave >= len(Notes.octaves):
		    Notes.octave = 0
		elif Notes.octave < 0:
		    Notes.octave = len(Notes.octaves) - 1

	def get_root_note():
		return State.root_note

	def set_root_note(data_two):
		Notes.root = data_two

	def set_upper_limit(data_two):
		Notes.upper_limit = data_two

	def set_lower_limit(data_two):
		Notes.lower_limit = data_two
		
	def get_upper_limit():
		return Notes.upper_limit

	def get_lower_limit():
		return Notes.lower_limit

	def get_octave():
		return Notes.octaves[Notes.octave] 

	def root_name(note):
		return Notes.note_list[note]

class Scales(Notes):

	major_scale = [0, 2, 4, 5, 7, 9, 11] 
	natural_scale =[0, 2, 3, 5, 7, 8, 10,] 
	harmonic_scale = [0, 2, 3, 5, 7, 8, 11] 
	dorian_scale = [0, 2, 3, 5, 7, 9, 10, ] 
	mixolydian_scale = [0, 2, 4, 5, 7, 9, 10,] 
	min_pent_scale = [0, 3, 5, 7, 10,] 
	chromatic_scale = [i for i in range(0, 11)]

	scales = [major_scale, natural_scale, harmonic_scale, dorian_scale, mixolydian_scale, min_pent_scale, chromatic_scale]
	scale_names = ["Major", "Natural Minor", "Harmonic Minor", "Dorian", "Mixolydian", "Minor Pentatonic", "Chromatic"]
	scale_choice = scale_names.index(config.SCALE)

	def set_scale(data_two):
		Scales.scale_choice = data_two

	def set_scale_by_name(name):
		Scales.scale_choice = Scales.scale_names.index(name)

	def increment_scale():
		Scales.scale_choice += 1
		if Scales.scale_choice >= len(Scales.scales):
			Scales.scale_choice = 0

	def get_scale_choice():
		return Scales.scale_choice

	def get_scale():
		return Scales.scales[Scales.scale_choice]

	def scale_message(data_two):
		return ui.setHintMsg(Scales.scale_names[int(mapvalues(self.data_two, 0, len(Scales.scale_names)-1, 0, 127))])

	def get_scale_name(scale_choice):
		return Scales.scale_names[scale_choice]

	def display_scale():
		return Timing.begin_message(f"Root: {Notes.root_name(Notes.get_root_note())} Scale: {Scales.scale_name(Scales.get_scale_choice())}")