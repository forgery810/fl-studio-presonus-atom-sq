import channels

preset_patterns = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0], [0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0],  [0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0], [1,0,1,1,1,0,1,0,1,1,1,0,1,0,1,1], [1,1,0,1,0,0,1,0,0,0,1,1,1,0,1,1], [1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0] ]



parameters = {
	
	0: "Pitch",
	1: "Velocity",
	2: "Release",
	3: "Fine Pitch",
	4: "Panning",
	5: "Mod x",
	6: "Mod y",
}

buttons = {
			"solo": [8, 9, 10, 11, 12, 13, 14, 15],			
			"mute": [16, 17, 18, 19, 20, 21, 22, 23],
			"arm": [0, 1, 2, 3, 4, 5, 6, 7],			
			"zoom": 100,
			# "select_mixer": 31,
			# "select_channels": 30,
			"button_1": 24,
			"button_2": 25,
			"button_3": 26,
			"button_4": 27,
			"button_5": 28,
			"button_6": 29,

		}

jog_number = 0

knobs = {


	"knob_one": 14,
	"knob_two": 15,
	"knob_three": 16,
	"knob_four": 17,
	"knob_five": 18,
	"knob_six": 19,
	"knob_seven": 20,
	"knob_eight": 21,
	"jog_wheel": 60,

	}

pads = {
	"touch": 1,
	"a": 24,
	"b": 25,
	"c": 26,
	"d": 27,
	"e": 28,
	"f": 29,
	"g": 30,
	"h": 31,
	"left_arrow": 98,
	"right_arrow": 99,
	"up_arrow": 24,
	"down_arrow": 25,

	"top_left": 9,
	"top_middle": 17,
	"top_right": 1,
	"bottom_left": 100,
}

tsport = {
	
	"stop": 93,
	"play": 94,
	"record": 95,
	"metronome": 89,
	"shift_stop": 81,
	"shift_play": 86,
	"shift_record": 80,
}


notes_list = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
midi_numbers = [x for x in range(21, 128)]
midi_notes = []

for y in range(0, 11):
	note_num = 0
	for note in notes_list:
		midi_notes.append(note+str(y))

colors = [-10721942, -5808209, -10849336, -13462158, -13030268, -13462136, -10900811, -7293607, -4879527, -5545351, -12619400]

ud_arrow = (24, 25, 26, 27, 28, 29, 30, 31, 46, 47)
channel_selected = channels.channelNumber()

cs = [0, 12, 24, 36, 48, 60, 72, 84, 96, 108, 120] # c note midi values


chromatic_scales = [[d for d in range(0, 152)] for n in notes_list]
major_scales = [[0, 2, 4, 5, 7, 9, 11, 12, 14, 16, 17, 19, 21, 23, 24, 26, 28, 29, 31, 33, 35, 36, 38, 40, 41, 43, 45, 47, 48, 50, 52, 53, 55, 57, 59, 60, 62, 64, 65, 67, 69, 71, 72, 74, 76, 77, 79, 81, 83, 84, 86, 88, 89, 91, 93, 95, 96, 98, 100, 101, 103, 105, 107, 108, 110, 112, 113, 115, 117, 119, 120, 122, 124, 125, 127, 129, 131, 132, 134, 136, 137, 139, 141, 143, 144], [1, 3, 5, 6, 8, 10, 12, 13, 15, 17, 18, 20, 22, 24, 25, 27, 29, 30, 32, 34, 36, 37, 39, 41, 42, 44, 46, 48, 49, 51, 53, 54, 56, 58, 60, 61, 63, 65, 66, 68, 70, 72, 73, 75, 77, 78, 80, 82, 84, 85, 87, 89, 90, 92, 94, 96, 97, 99, 101, 102, 104, 106, 108, 109, 111, 113, 114, 116, 118, 120, 121, 123, 125, 126, 128, 130, 132, 133, 135, 137, 138, 140, 142, 144, 145], [2, 4, 6, 7, 9, 11, 13, 14, 16, 18, 19, 21, 23, 25, 26, 28, 30, 31, 33, 35, 37, 38, 40, 42, 43, 45, 47, 49, 50, 52, 54, 55, 57, 59, 61, 62, 64, 66, 67, 69, 71, 73, 74, 76, 78, 79, 81, 83, 85, 86, 88, 90, 91, 93, 95, 97, 98, 100, 102, 103, 105, 107, 109, 110, 112, 114, 115, 117, 119, 121, 122, 124, 126, 127, 129, 131, 133, 134, 136, 138, 139, 141, 143, 145, 146], [3, 5, 7, 8, 10, 12, 14, 15, 17, 19, 20, 22, 24, 26, 27, 29, 31, 32, 34, 36, 38, 39, 41, 43, 44, 46, 48, 50, 51, 53, 55, 56, 58, 60, 62, 63, 65, 67, 68, 70, 72, 74, 75, 77, 79, 80, 82, 84, 86, 87, 89, 91, 92, 94, 96, 98, 99, 101, 103, 104, 106, 108, 110, 111, 113, 115, 116, 118, 120, 122, 123, 125, 127, 128, 130, 132, 134, 135, 137, 139, 140, 142, 144, 146, 147], [4, 6, 8, 9, 11, 13, 15, 16, 18, 20, 21, 23, 25, 27, 28, 30, 32, 33, 35, 37, 39, 40, 42, 44, 45, 47, 49, 51, 52, 54, 56, 57, 59, 61, 63, 64, 66, 68, 69, 71, 73, 75, 76, 78, 80, 81, 83, 85, 87, 88, 90, 92, 93, 95, 97, 99, 100, 102, 104, 105, 107, 109, 111, 112, 114, 116, 117, 119, 121, 123, 124, 126, 128, 129, 131, 133, 135, 136, 138, 140, 141, 143, 145, 147, 148], [5, 7, 9, 10, 12, 14, 16, 17, 19, 21, 22, 24, 26, 28, 29, 31, 33, 34, 36, 38, 40, 41, 43, 45, 46, 48, 50, 52, 53, 55, 57, 58, 60, 62, 64, 65, 67, 69, 70, 72, 74, 76, 77, 79, 81, 82, 84, 86, 88, 89, 91, 93, 94, 96, 98, 100, 101, 103, 105, 106, 108, 110, 112, 113, 115, 117, 118, 120, 122, 124, 125, 127, 129, 130, 132, 134, 136, 137, 139, 141, 142, 144, 146, 148, 149], [6, 8, 10, 11, 13, 15, 17, 18, 20, 22, 23, 25, 27, 29, 30, 32, 34, 35, 37, 39, 41, 42, 44, 46, 47, 49, 51, 53, 54, 56, 58, 59, 61, 63, 65, 66, 68, 70, 71, 73, 75, 77, 78, 80, 82, 83, 85, 87, 89, 90, 92, 94, 95, 97, 99, 101, 102, 104, 106, 107, 109, 111, 113, 114, 116, 118, 119, 121, 123, 125, 126, 128, 130, 131, 133, 135, 137, 138, 140, 142, 143, 145, 147, 149, 150], [7, 9, 11, 12, 14, 16, 18, 19, 21, 23, 24, 26, 28, 30, 31, 33, 35, 36, 38, 40, 42, 43, 45, 47, 48, 50, 52, 54, 55, 57, 59, 60, 62, 64, 66, 67, 69, 71, 72, 74, 76, 78, 79, 81, 83, 84, 86, 88, 90, 91, 93, 95, 96, 98, 100, 102, 103, 105, 107, 108, 110, 112, 114, 115, 117, 119, 120, 122, 124, 126, 127, 129, 131, 132, 134, 136, 138, 139, 141, 143, 144, 146, 148, 150, 151], [8, 10, 12, 13, 15, 17, 19, 20, 22, 24, 25, 27, 29, 31, 32, 34, 36, 37, 39, 41, 43, 44, 46, 48, 49, 51, 53, 55, 56, 58, 60, 61, 63, 65, 67, 68, 70, 72, 73, 75, 77, 79, 80, 82, 84, 85, 87, 89, 91, 92, 94, 96, 97, 99, 101, 103, 104, 106, 108, 109, 111, 113, 115, 116, 118, 120, 121, 123, 125, 127, 128, 130, 132, 133, 135, 137, 139, 140, 142, 144, 145, 147, 149, 151, 152], [9, 11, 13, 14, 16, 18, 20, 21, 23, 25, 26, 28, 30, 32, 33, 35, 37, 38, 40, 42, 44, 45, 47, 49, 50, 52, 54, 56, 57, 59, 61, 62, 64, 66, 68, 69, 71, 73, 74, 76, 78, 80, 81, 83, 85, 86, 88, 90, 92, 93, 95, 97, 98, 100, 102, 104, 105, 107, 109, 110, 112, 114, 116, 117, 119, 121, 122, 124, 126, 128, 129, 131, 133, 134, 136, 138, 140, 141, 143, 145, 146, 148, 150, 152, 153], [10, 12, 14, 15, 17, 19, 21, 22, 24, 26, 27, 29, 31, 33, 34, 36, 38, 39, 41, 43, 45, 46, 48, 50, 51, 53, 55, 57, 58, 60, 62, 63, 65, 67, 69, 70, 72, 74, 75, 77, 79, 81, 82, 84, 86, 87, 89, 91, 93, 94, 96, 98, 99, 101, 103, 105, 106, 108, 110, 111, 113, 115, 117, 118, 120, 122, 123, 125, 127, 129, 130, 132, 134, 135, 137, 139, 141, 142, 144, 146, 147, 149, 151, 153, 154], [11, 13, 15, 16, 18, 20, 22, 23, 25, 27, 28, 30, 32, 34, 35, 37, 39, 40, 42, 44, 46, 47, 49, 51, 52, 54, 56, 58, 59, 61, 63, 64, 66, 68, 70, 71, 73, 75, 76, 78, 80, 82, 83, 85, 87, 88, 90, 92, 94, 95, 97, 99, 100, 102, 104, 106, 107, 109, 111, 112, 114, 116, 118, 119, 121, 123, 124, 126, 128, 130, 131, 133, 135, 136, 138, 140, 142, 143, 145, 147, 148, 150, 152, 154, 155]]
natural_scales = [[0, 2, 3, 5, 7, 8, 10, 12, 14, 15, 17, 19, 20, 22, 24, 26, 27, 29, 31, 32, 34, 36, 38, 39, 41, 43, 44, 46, 48, 50, 51, 53, 55, 56, 58, 60, 62, 63, 65, 67, 68, 70, 72, 74, 75, 77, 79, 80, 82, 84, 86, 87, 89, 91, 92, 94, 96, 98, 99, 101, 103, 104, 106, 108, 110, 111, 113, 115, 116, 118, 120, 122, 123, 125, 127, 128, 130, 132, 134, 135, 137, 139, 140, 142, 144], [1, 3, 4, 6, 8, 9, 11, 13, 15, 16, 18, 20, 21, 23, 25, 27, 28, 30, 32, 33, 35, 37, 39, 40, 42, 44, 45, 47, 49, 51, 52, 54, 56, 57, 59, 61, 63, 64, 66, 68, 69, 71, 73, 75, 76, 78, 80, 81, 83, 85, 87, 88, 90, 92, 93, 95, 97, 99, 100, 102, 104, 105, 107, 109, 111, 112, 114, 116, 117, 119, 121, 123, 124, 126, 128, 129, 131, 133, 135, 136, 138, 140, 141, 143, 145], [2, 4, 5, 7, 9, 10, 12, 14, 16, 17, 19, 21, 22, 24, 26, 28, 29, 31, 33, 34, 36, 38, 40, 41, 43, 45, 46, 48, 50, 52, 53, 55, 57, 58, 60, 62, 64, 65, 67, 69, 70, 72, 74, 76, 77, 79, 81, 82, 84, 86, 88, 89, 91, 93, 94, 96, 98, 100, 101, 103, 105, 106, 108, 110, 112, 113, 115, 117, 118, 120, 122, 124, 125, 127, 129, 130, 132, 134, 136, 137, 139, 141, 142, 144, 146], [3, 5, 6, 8, 10, 11, 13, 15, 17, 18, 20, 22, 23, 25, 27, 29, 30, 32, 34, 35, 37, 39, 41, 42, 44, 46, 47, 49, 51, 53, 54, 56, 58, 59, 61, 63, 65, 66, 68, 70, 71, 73, 75, 77, 78, 80, 82, 83, 85, 87, 89, 90, 92, 94, 95, 97, 99, 101, 102, 104, 106, 107, 109, 111, 113, 114, 116, 118, 119, 121, 123, 125, 126, 128, 130, 131, 133, 135, 137, 138, 140, 142, 143, 145, 147], [4, 6, 7, 9, 11, 12, 14, 16, 18, 19, 21, 23, 24, 26, 28, 30, 31, 33, 35, 36, 38, 40, 42, 43, 45, 47, 48, 50, 52, 54, 55, 57, 59, 60, 62, 64, 66, 67, 69, 71, 72, 74, 76, 78, 79, 81, 83, 84, 86, 88, 90, 91, 93, 95, 96, 98, 100, 102, 103, 105, 107, 108, 110, 112, 114, 115, 117, 119, 120, 122, 124, 126, 127, 129, 131, 132, 134, 136, 138, 139, 141, 143, 144, 146, 148], [5, 7, 8, 10, 12, 13, 15, 17, 19, 20, 22, 24, 25, 27, 29, 31, 32, 34, 36, 37, 39, 41, 43, 44, 46, 48, 49, 51, 53, 55, 56, 58, 60, 61, 63, 65, 67, 68, 70, 72, 73, 75, 77, 79, 80, 82, 84, 85, 87, 89, 91, 92, 94, 96, 97, 99, 101, 103, 104, 106, 108, 109, 111, 113, 115, 116, 118, 120, 121, 123, 125, 127, 128, 130, 132, 133, 135, 137, 139, 140, 142, 144, 145, 147, 149], [6, 8, 9, 11, 13, 14, 16, 18, 20, 21, 23, 25, 26, 28, 30, 32, 33, 35, 37, 38, 40, 42, 44, 45, 47, 49, 50, 52, 54, 56, 57, 59, 61, 62, 64, 66, 68, 69, 71, 73, 74, 76, 78, 80, 81, 83, 85, 86, 88, 90, 92, 93, 95, 97, 98, 100, 102, 104, 105, 107, 109, 110, 112, 114, 116, 117, 119, 121, 122, 124, 126, 128, 129, 131, 133, 134, 136, 138, 140, 141, 143, 145, 146, 148, 150], [7, 9, 10, 12, 14, 15, 17, 19, 21, 22, 24, 26, 27, 29, 31, 33, 34, 36, 38, 39, 41, 43, 45, 46, 48, 50, 51, 53, 55, 57, 58, 60, 62, 63, 65, 67, 69, 70, 72, 74, 75, 77, 79, 81, 82, 84, 86, 87, 89, 91, 93, 94, 96, 98, 99, 101, 103, 105, 106, 108, 110, 111, 113, 115, 117, 118, 120, 122, 123, 125, 127, 129, 130, 132, 134, 135, 137, 139, 141, 142, 144, 146, 147, 149, 151], [8, 10, 11, 13, 15, 16, 18, 20, 22, 23, 25, 27, 28, 30, 32, 34, 35, 37, 39, 40, 42, 44, 46, 47, 49, 51, 52, 54, 56, 58, 59, 61, 63, 64, 66, 68, 70, 71, 73, 75, 76, 78, 80, 82, 83, 85, 87, 88, 90, 92, 94, 95, 97, 99, 100, 102, 104, 106, 107, 109, 111, 112, 114, 116, 118, 119, 121, 123, 124, 126, 128, 130, 131, 133, 135, 136, 138, 140, 142, 143, 145, 147, 148, 150, 152], [9, 11, 12, 14, 16, 17, 19, 21, 23, 24, 26, 28, 29, 31, 33, 35, 36, 38, 40, 41, 43, 45, 47, 48, 50, 52, 53, 55, 57, 59, 60, 62, 64, 65, 67, 69, 71, 72, 74, 76, 77, 79, 81, 83, 84, 86, 88, 89, 91, 93, 95, 96, 98, 100, 101, 103, 105, 107, 108, 110, 112, 113, 115, 117, 119, 120, 122, 124, 125, 127, 129, 131, 132, 134, 136, 137, 139, 141, 143, 144, 146, 148, 149, 151, 153], [10, 12, 13, 15, 17, 18, 20, 22, 24, 25, 27, 29, 30, 32, 34, 36, 37, 39, 41, 42, 44, 46, 48, 49, 51, 53, 54, 56, 58, 60, 61, 63, 65, 66, 68, 70, 72, 73, 75, 77, 78, 80, 82, 84, 85, 87, 89, 90, 92, 94, 96, 97, 99, 101, 102, 104, 106, 108, 109, 111, 113, 114, 116, 118, 120, 121, 123, 125, 126, 128, 130, 132, 133, 135, 137, 138, 140, 142, 144, 145, 147, 149, 150, 152, 154], [11, 13, 14, 16, 18, 19, 21, 23, 25, 26, 28, 30, 31, 33, 35, 37, 38, 40, 42, 43, 45, 47, 49, 50, 52, 54, 55, 57, 59, 61, 62, 64, 66, 67, 69, 71, 73, 74, 76, 78, 79, 81, 83, 85, 86, 88, 90, 91, 93, 95, 97, 98, 100, 102, 103, 105, 107, 109, 110, 112, 114, 115, 117, 119, 121, 122, 124, 126, 127, 129, 131, 133, 134, 136, 138, 139, 141, 143, 145, 146, 148, 150, 151, 153, 155]]
harmonic_scales = [[0, 2, 3, 5, 7, 8, 11, 12, 14, 15, 17, 19, 20, 23, 24, 26, 27, 29, 31, 32, 35, 36, 38, 39, 41, 43, 44, 47, 48, 50, 51, 53, 55, 56, 59, 60, 62, 63, 65, 67, 68, 71, 72, 74, 75, 77, 79, 80, 83, 84, 86, 87, 89, 91, 92, 95, 96, 98, 99, 101, 103, 104, 107, 108, 110, 111, 113, 115, 116, 119, 120, 122, 123, 125, 127, 128, 131, 132, 134, 135, 137, 139, 140, 143, 144], [1, 3, 4, 6, 8, 9, 12, 13, 15, 16, 18, 20, 21, 24, 25, 27, 28, 30, 32, 33, 36, 37, 39, 40, 42, 44, 45, 48, 49, 51, 52, 54, 56, 57, 60, 61, 63, 64, 66, 68, 69, 72, 73, 75, 76, 78, 80, 81, 84, 85, 87, 88, 90, 92, 93, 96, 97, 99, 100, 102, 104, 105, 108, 109, 111, 112, 114, 116, 117, 120, 121, 123, 124, 126, 128, 129, 132, 133, 135, 136, 138, 140, 141, 144, 145], [2, 4, 5, 7, 9, 10, 13, 14, 16, 17, 19, 21, 22, 25, 26, 28, 29, 31, 33, 34, 37, 38, 40, 41, 43, 45, 46, 49, 50, 52, 53, 55, 57, 58, 61, 62, 64, 65, 67, 69, 70, 73, 74, 76, 77, 79, 81, 82, 85, 86, 88, 89, 91, 93, 94, 97, 98, 100, 101, 103, 105, 106, 109, 110, 112, 113, 115, 117, 118, 121, 122, 124, 125, 127, 129, 130, 133, 134, 136, 137, 139, 141, 142, 145, 146], [3, 5, 6, 8, 10, 11, 14, 15, 17, 18, 20, 22, 23, 26, 27, 29, 30, 32, 34, 35, 38, 39, 41, 42, 44, 46, 47, 50, 51, 53, 54, 56, 58, 59, 62, 63, 65, 66, 68, 70, 71, 74, 75, 77, 78, 80, 82, 83, 86, 87, 89, 90, 92, 94, 95, 98, 99, 101, 102, 104, 106, 107, 110, 111, 113, 114, 116, 118, 119, 122, 123, 125, 126, 128, 130, 131, 134, 135, 137, 138, 140, 142, 143, 146, 147], [4, 6, 7, 9, 11, 12, 15, 16, 18, 19, 21, 23, 24, 27, 28, 30, 31, 33, 35, 36, 39, 40, 42, 43, 45, 47, 48, 51, 52, 54, 55, 57, 59, 60, 63, 64, 66, 67, 69, 71, 72, 75, 76, 78, 79, 81, 83, 84, 87, 88, 90, 91, 93, 95, 96, 99, 100, 102, 103, 105, 107, 108, 111, 112, 114, 115, 117, 119, 120, 123, 124, 126, 127, 129, 131, 132, 135, 136, 138, 139, 141, 143, 144, 147, 148], [5, 7, 8, 10, 12, 13, 16, 17, 19, 20, 22, 24, 25, 28, 29, 31, 32, 34, 36, 37, 40, 41, 43, 44, 46, 48, 49, 52, 53, 55, 56, 58, 60, 61, 64, 65, 67, 68, 70, 72, 73, 76, 77, 79, 80, 82, 84, 85, 88, 89, 91, 92, 94, 96, 97, 100, 101, 103, 104, 106, 108, 109, 112, 113, 115, 116, 118, 120, 121, 124, 125, 127, 128, 130, 132, 133, 136, 137, 139, 140, 142, 144, 145, 148, 149], [6, 8, 9, 11, 13, 14, 17, 18, 20, 21, 23, 25, 26, 29, 30, 32, 33, 35, 37, 38, 41, 42, 44, 45, 47, 49, 50, 53, 54, 56, 57, 59, 61, 62, 65, 66, 68, 69, 71, 73, 74, 77, 78, 80, 81, 83, 85, 86, 89, 90, 92, 93, 95, 97, 98, 101, 102, 104, 105, 107, 109, 110, 113, 114, 116, 117, 119, 121, 122, 125, 126, 128, 129, 131, 133, 134, 137, 138, 140, 141, 143, 145, 146, 149, 150], [7, 9, 10, 12, 14, 15, 18, 19, 21, 22, 24, 26, 27, 30, 31, 33, 34, 36, 38, 39, 42, 43, 45, 46, 48, 50, 51, 54, 55, 57, 58, 60, 62, 63, 66, 67, 69, 70, 72, 74, 75, 78, 79, 81, 82, 84, 86, 87, 90, 91, 93, 94, 96, 98, 99, 102, 103, 105, 106, 108, 110, 111, 114, 115, 117, 118, 120, 122, 123, 126, 127, 129, 130, 132, 134, 135, 138, 139, 141, 142, 144, 146, 147, 150, 151], [8, 10, 11, 13, 15, 16, 19, 20, 22, 23, 25, 27, 28, 31, 32, 34, 35, 37, 39, 40, 43, 44, 46, 47, 49, 51, 52, 55, 56, 58, 59, 61, 63, 64, 67, 68, 70, 71, 73, 75, 76, 79, 80, 82, 83, 85, 87, 88, 91, 92, 94, 95, 97, 99, 100, 103, 104, 106, 107, 109, 111, 112, 115, 116, 118, 119, 121, 123, 124, 127, 128, 130, 131, 133, 135, 136, 139, 140, 142, 143, 145, 147, 148, 151, 152], [9, 11, 12, 14, 16, 17, 20, 21, 23, 24, 26, 28, 29, 32, 33, 35, 36, 38, 40, 41, 44, 45, 47, 48, 50, 52, 53, 56, 57, 59, 60, 62, 64, 65, 68, 69, 71, 72, 74, 76, 77, 80, 81, 83, 84, 86, 88, 89, 92, 93, 95, 96, 98, 100, 101, 104, 105, 107, 108, 110, 112, 113, 116, 117, 119, 120, 122, 124, 125, 128, 129, 131, 132, 134, 136, 137, 140, 141, 143, 144, 146, 148, 149, 152, 153], [10, 12, 13, 15, 17, 18, 21, 22, 24, 25, 27, 29, 30, 33, 34, 36, 37, 39, 41, 42, 45, 46, 48, 49, 51, 53, 54, 57, 58, 60, 61, 63, 65, 66, 69, 70, 72, 73, 75, 77, 78, 81, 82, 84, 85, 87, 89, 90, 93, 94, 96, 97, 99, 101, 102, 105, 106, 108, 109, 111, 113, 114, 117, 118, 120, 121, 123, 125, 126, 129, 130, 132, 133, 135, 137, 138, 141, 142, 144, 145, 147, 149, 150, 153, 154], [11, 13, 14, 16, 18, 19, 22, 23, 25, 26, 28, 30, 31, 34, 35, 37, 38, 40, 42, 43, 46, 47, 49, 50, 52, 54, 55, 58, 59, 61, 62, 64, 66, 67, 70, 71, 73, 74, 76, 78, 79, 82, 83, 85, 86, 88, 90, 91, 94, 95, 97, 98, 100, 102, 103, 106, 107, 109, 110, 112, 114, 115, 118, 119, 121, 122, 124, 126, 127, 130, 131, 133, 134, 136, 138, 139, 142, 143, 145, 146, 148, 150, 151, 154, 155]]
dorian_scales = [[0, 2, 3, 5, 7, 9, 10, 12, 14, 15, 17, 19, 21, 22, 24, 26, 27, 29, 31, 33, 34, 36, 38, 39, 41, 43, 45, 46, 48, 50, 51, 53, 55, 57, 58, 60, 62, 63, 65, 67, 69, 70, 72, 74, 75, 77, 79, 81, 82, 84, 86, 87, 89, 91, 93, 94, 96, 98, 99, 101, 103, 105, 106, 108, 110, 111, 113, 115, 117, 118, 120, 122, 123, 125, 127, 129, 130, 132, 134, 135, 137, 139, 141, 142, 144], [1, 3, 4, 6, 8, 10, 11, 13, 15, 16, 18, 20, 22, 23, 25, 27, 28, 30, 32, 34, 35, 37, 39, 40, 42, 44, 46, 47, 49, 51, 52, 54, 56, 58, 59, 61, 63, 64, 66, 68, 70, 71, 73, 75, 76, 78, 80, 82, 83, 85, 87, 88, 90, 92, 94, 95, 97, 99, 100, 102, 104, 106, 107, 109, 111, 112, 114, 116, 118, 119, 121, 123, 124, 126, 128, 130, 131, 133, 135, 136, 138, 140, 142, 143, 145], [2, 4, 5, 7, 9, 11, 12, 14, 16, 17, 19, 21, 23, 24, 26, 28, 29, 31, 33, 35, 36, 38, 40, 41, 43, 45, 47, 48, 50, 52, 53, 55, 57, 59, 60, 62, 64, 65, 67, 69, 71, 72, 74, 76, 77, 79, 81, 83, 84, 86, 88, 89, 91, 93, 95, 96, 98, 100, 101, 103, 105, 107, 108, 110, 112, 113, 115, 117, 119, 120, 122, 124, 125, 127, 129, 131, 132, 134, 136, 137, 139, 141, 143, 144, 146], [3, 5, 6, 8, 10, 12, 13, 15, 17, 18, 20, 22, 24, 25, 27, 29, 30, 32, 34, 36, 37, 39, 41, 42, 44, 46, 48, 49, 51, 53, 54, 56, 58, 60, 61, 63, 65, 66, 68, 70, 72, 73, 75, 77, 78, 80, 82, 84, 85, 87, 89, 90, 92, 94, 96, 97, 99, 101, 102, 104, 106, 108, 109, 111, 113, 114, 116, 118, 120, 121, 123, 125, 126, 128, 130, 132, 133, 135, 137, 138, 140, 142, 144, 145, 147], [4, 6, 7, 9, 11, 13, 14, 16, 18, 19, 21, 23, 25, 26, 28, 30, 31, 33, 35, 37, 38, 40, 42, 43, 45, 47, 49, 50, 52, 54, 55, 57, 59, 61, 62, 64, 66, 67, 69, 71, 73, 74, 76, 78, 79, 81, 83, 85, 86, 88, 90, 91, 93, 95, 97, 98, 100, 102, 103, 105, 107, 109, 110, 112, 114, 115, 117, 119, 121, 122, 124, 126, 127, 129, 131, 133, 134, 136, 138, 139, 141, 143, 145, 146, 148], [5, 7, 8, 10, 12, 14, 15, 17, 19, 20, 22, 24, 26, 27, 29, 31, 32, 34, 36, 38, 39, 41, 43, 44, 46, 48, 50, 51, 53, 55, 56, 58, 60, 62, 63, 65, 67, 68, 70, 72, 74, 75, 77, 79, 80, 82, 84, 86, 87, 89, 91, 92, 94, 96, 98, 99, 101, 103, 104, 106, 108, 110, 111, 113, 115, 116, 118, 120, 122, 123, 125, 127, 128, 130, 132, 134, 135, 137, 139, 140, 142, 144, 146, 147, 149], [6, 8, 9, 11, 13, 15, 16, 18, 20, 21, 23, 25, 27, 28, 30, 32, 33, 35, 37, 39, 40, 42, 44, 45, 47, 49, 51, 52, 54, 56, 57, 59, 61, 63, 64, 66, 68, 69, 71, 73, 75, 76, 78, 80, 81, 83, 85, 87, 88, 90, 92, 93, 95, 97, 99, 100, 102, 104, 105, 107, 109, 111, 112, 114, 116, 117, 119, 121, 123, 124, 126, 128, 129, 131, 133, 135, 136, 138, 140, 141, 143, 145, 147, 148, 150], [7, 9, 10, 12, 14, 16, 17, 19, 21, 22, 24, 26, 28, 29, 31, 33, 34, 36, 38, 40, 41, 43, 45, 46, 48, 50, 52, 53, 55, 57, 58, 60, 62, 64, 65, 67, 69, 70, 72, 74, 76, 77, 79, 81, 82, 84, 86, 88, 89, 91, 93, 94, 96, 98, 100, 101, 103, 105, 106, 108, 110, 112, 113, 115, 117, 118, 120, 122, 124, 125, 127, 129, 130, 132, 134, 136, 137, 139, 141, 142, 144, 146, 148, 149, 151], [8, 10, 11, 13, 15, 17, 18, 20, 22, 23, 25, 27, 29, 30, 32, 34, 35, 37, 39, 41, 42, 44, 46, 47, 49, 51, 53, 54, 56, 58, 59, 61, 63, 65, 66, 68, 70, 71, 73, 75, 77, 78, 80, 82, 83, 85, 87, 89, 90, 92, 94, 95, 97, 99, 101, 102, 104, 106, 107, 109, 111, 113, 114, 116, 118, 119, 121, 123, 125, 126, 128, 130, 131, 133, 135, 137, 138, 140, 142, 143, 145, 147, 149, 150, 152], [9, 11, 12, 14, 16, 18, 19, 21, 23, 24, 26, 28, 30, 31, 33, 35, 36, 38, 40, 42, 43, 45, 47, 48, 50, 52, 54, 55, 57, 59, 60, 62, 64, 66, 67, 69, 71, 72, 74, 76, 78, 79, 81, 83, 84, 86, 88, 90, 91, 93, 95, 96, 98, 100, 102, 103, 105, 107, 108, 110, 112, 114, 115, 117, 119, 120, 122, 124, 126, 127, 129, 131, 132, 134, 136, 138, 139, 141, 143, 144, 146, 148, 150, 151, 153], [10, 12, 13, 15, 17, 19, 20, 22, 24, 25, 27, 29, 31, 32, 34, 36, 37, 39, 41, 43, 44, 46, 48, 49, 51, 53, 55, 56, 58, 60, 61, 63, 65, 67, 68, 70, 72, 73, 75, 77, 79, 80, 82, 84, 85, 87, 89, 91, 92, 94, 96, 97, 99, 101, 103, 104, 106, 108, 109, 111, 113, 115, 116, 118, 120, 121, 123, 125, 127, 128, 130, 132, 133, 135, 137, 139, 140, 142, 144, 145, 147, 149, 151, 152, 154], [11, 13, 14, 16, 18, 20, 21, 23, 25, 26, 28, 30, 32, 33, 35, 37, 38, 40, 42, 44, 45, 47, 49, 50, 52, 54, 56, 57, 59, 61, 62, 64, 66, 68, 69, 71, 73, 74, 76, 78, 80, 81, 83, 85, 86, 88, 90, 92, 93, 95, 97, 98, 100, 102, 104, 105, 107, 109, 110, 112, 114, 116, 117, 119, 121, 122, 124, 126, 128, 129, 131, 133, 134, 136, 138, 140, 141, 143, 145, 146, 148, 150, 152, 153, 155]]
mixolydian_scales = [[0, 2, 4, 5, 7, 9, 10, 12, 14, 16, 17, 19, 21, 22, 24, 26, 28, 29, 31, 33, 34, 36, 38, 40, 41, 43, 45, 46, 48, 50, 52, 53, 55, 57, 58, 60, 62, 64, 65, 67, 69, 70, 72, 74, 76, 77, 79, 81, 82, 84, 86, 88, 89, 91, 93, 94, 96, 98, 100, 101, 103, 105, 106, 108, 110, 112, 113, 115, 117, 118, 120, 122, 124, 125, 127, 129, 130, 132, 134, 136, 137, 139, 141, 142, 144], [1, 3, 5, 6, 8, 10, 11, 13, 15, 17, 18, 20, 22, 23, 25, 27, 29, 30, 32, 34, 35, 37, 39, 41, 42, 44, 46, 47, 49, 51, 53, 54, 56, 58, 59, 61, 63, 65, 66, 68, 70, 71, 73, 75, 77, 78, 80, 82, 83, 85, 87, 89, 90, 92, 94, 95, 97, 99, 101, 102, 104, 106, 107, 109, 111, 113, 114, 116, 118, 119, 121, 123, 125, 126, 128, 130, 131, 133, 135, 137, 138, 140, 142, 143, 145], [2, 4, 6, 7, 9, 11, 12, 14, 16, 18, 19, 21, 23, 24, 26, 28, 30, 31, 33, 35, 36, 38, 40, 42, 43, 45, 47, 48, 50, 52, 54, 55, 57, 59, 60, 62, 64, 66, 67, 69, 71, 72, 74, 76, 78, 79, 81, 83, 84, 86, 88, 90, 91, 93, 95, 96, 98, 100, 102, 103, 105, 107, 108, 110, 112, 114, 115, 117, 119, 120, 122, 124, 126, 127, 129, 131, 132, 134, 136, 138, 139, 141, 143, 144, 146], [3, 5, 7, 8, 10, 12, 13, 15, 17, 19, 20, 22, 24, 25, 27, 29, 31, 32, 34, 36, 37, 39, 41, 43, 44, 46, 48, 49, 51, 53, 55, 56, 58, 60, 61, 63, 65, 67, 68, 70, 72, 73, 75, 77, 79, 80, 82, 84, 85, 87, 89, 91, 92, 94, 96, 97, 99, 101, 103, 104, 106, 108, 109, 111, 113, 115, 116, 118, 120, 121, 123, 125, 127, 128, 130, 132, 133, 135, 137, 139, 140, 142, 144, 145, 147], [4, 6, 8, 9, 11, 13, 14, 16, 18, 20, 21, 23, 25, 26, 28, 30, 32, 33, 35, 37, 38, 40, 42, 44, 45, 47, 49, 50, 52, 54, 56, 57, 59, 61, 62, 64, 66, 68, 69, 71, 73, 74, 76, 78, 80, 81, 83, 85, 86, 88, 90, 92, 93, 95, 97, 98, 100, 102, 104, 105, 107, 109, 110, 112, 114, 116, 117, 119, 121, 122, 124, 126, 128, 129, 131, 133, 134, 136, 138, 140, 141, 143, 145, 146, 148], [5, 7, 9, 10, 12, 14, 15, 17, 19, 21, 22, 24, 26, 27, 29, 31, 33, 34, 36, 38, 39, 41, 43, 45, 46, 48, 50, 51, 53, 55, 57, 58, 60, 62, 63, 65, 67, 69, 70, 72, 74, 75, 77, 79, 81, 82, 84, 86, 87, 89, 91, 93, 94, 96, 98, 99, 101, 103, 105, 106, 108, 110, 111, 113, 115, 117, 118, 120, 122, 123, 125, 127, 129, 130, 132, 134, 135, 137, 139, 141, 142, 144, 146, 147, 149], [6, 8, 10, 11, 13, 15, 16, 18, 20, 22, 23, 25, 27, 28, 30, 32, 34, 35, 37, 39, 40, 42, 44, 46, 47, 49, 51, 52, 54, 56, 58, 59, 61, 63, 64, 66, 68, 70, 71, 73, 75, 76, 78, 80, 82, 83, 85, 87, 88, 90, 92, 94, 95, 97, 99, 100, 102, 104, 106, 107, 109, 111, 112, 114, 116, 118, 119, 121, 123, 124, 126, 128, 130, 131, 133, 135, 136, 138, 140, 142, 143, 145, 147, 148, 150], [7, 9, 11, 12, 14, 16, 17, 19, 21, 23, 24, 26, 28, 29, 31, 33, 35, 36, 38, 40, 41, 43, 45, 47, 48, 50, 52, 53, 55, 57, 59, 60, 62, 64, 65, 67, 69, 71, 72, 74, 76, 77, 79, 81, 83, 84, 86, 88, 89, 91, 93, 95, 96, 98, 100, 101, 103, 105, 107, 108, 110, 112, 113, 115, 117, 119, 120, 122, 124, 125, 127, 129, 131, 132, 134, 136, 137, 139, 141, 143, 144, 146, 148, 149, 151], [8, 10, 12, 13, 15, 17, 18, 20, 22, 24, 25, 27, 29, 30, 32, 34, 36, 37, 39, 41, 42, 44, 46, 48, 49, 51, 53, 54, 56, 58, 60, 61, 63, 65, 66, 68, 70, 72, 73, 75, 77, 78, 80, 82, 84, 85, 87, 89, 90, 92, 94, 96, 97, 99, 101, 102, 104, 106, 108, 109, 111, 113, 114, 116, 118, 120, 121, 123, 125, 126, 128, 130, 132, 133, 135, 137, 138, 140, 142, 144, 145, 147, 149, 150, 152], [9, 11, 13, 14, 16, 18, 19, 21, 23, 25, 26, 28, 30, 31, 33, 35, 37, 38, 40, 42, 43, 45, 47, 49, 50, 52, 54, 55, 57, 59, 61, 62, 64, 66, 67, 69, 71, 73, 74, 76, 78, 79, 81, 83, 85, 86, 88, 90, 91, 93, 95, 97, 98, 100, 102, 103, 105, 107, 109, 110, 112, 114, 115, 117, 119, 121, 122, 124, 126, 127, 129, 131, 133, 134, 136, 138, 139, 141, 143, 145, 146, 148, 150, 151, 153], [10, 12, 14, 15, 17, 19, 20, 22, 24, 26, 27, 29, 31, 32, 34, 36, 38, 39, 41, 43, 44, 46, 48, 50, 51, 53, 55, 56, 58, 60, 62, 63, 65, 67, 68, 70, 72, 74, 75, 77, 79, 80, 82, 84, 86, 87, 89, 91, 92, 94, 96, 98, 99, 101, 103, 104, 106, 108, 110, 111, 113, 115, 116, 118, 120, 122, 123, 125, 127, 128, 130, 132, 134, 135, 137, 139, 140, 142, 144, 146, 147, 149, 151, 152, 154], [11, 13, 15, 16, 18, 20, 21, 23, 25, 27, 28, 30, 32, 33, 35, 37, 39, 40, 42, 44, 45, 47, 49, 51, 52, 54, 56, 57, 59, 61, 63, 64, 66, 68, 69, 71, 73, 75, 76, 78, 80, 81, 83, 85, 87, 88, 90, 92, 93, 95, 97, 99, 100, 102, 104, 105, 107, 109, 111, 112, 114, 116, 117, 119, 121, 123, 124, 126, 128, 129, 131, 133, 135, 136, 138, 140, 141, 143, 145, 147, 148, 150, 152, 153, 155]]
min_pent_scales = [[0, 3, 5, 7, 10, 12, 15, 17, 19, 22, 24, 27, 29, 31, 34, 36, 39, 41, 43, 46, 48, 51, 53, 55, 58, 60, 63, 65, 67, 70, 72, 75, 77, 79, 82, 84, 87, 89, 91, 94, 96, 99, 101, 103, 106, 108, 111, 113, 115, 118, 120, 123, 125, 127, 130, 132, 135, 137, 139, 142, 144], [1, 4, 6, 8, 11, 13, 16, 18, 20, 23, 25, 28, 30, 32, 35, 37, 40, 42, 44, 47, 49, 52, 54, 56, 59, 61, 64, 66, 68, 71, 73, 76, 78, 80, 83, 85, 88, 90, 92, 95, 97, 100, 102, 104, 107, 109, 112, 114, 116, 119, 121, 124, 126, 128, 131, 133, 136, 138, 140, 143, 145], [2, 5, 7, 9, 12, 14, 17, 19, 21, 24, 26, 29, 31, 33, 36, 38, 41, 43, 45, 48, 50, 53, 55, 57, 60, 62, 65, 67, 69, 72, 74, 77, 79, 81, 84, 86, 89, 91, 93, 96, 98, 101, 103, 105, 108, 110, 113, 115, 117, 120, 122, 125, 127, 129, 132, 134, 137, 139, 141, 144, 146], [3, 6, 8, 10, 13, 15, 18, 20, 22, 25, 27, 30, 32, 34, 37, 39, 42, 44, 46, 49, 51, 54, 56, 58, 61, 63, 66, 68, 70, 73, 75, 78, 80, 82, 85, 87, 90, 92, 94, 97, 99, 102, 104, 106, 109, 111, 114, 116, 118, 121, 123, 126, 128, 130, 133, 135, 138, 140, 142, 145, 147], [4, 7, 9, 11, 14, 16, 19, 21, 23, 26, 28, 31, 33, 35, 38, 40, 43, 45, 47, 50, 52, 55, 57, 59, 62, 64, 67, 69, 71, 74, 76, 79, 81, 83, 86, 88, 91, 93, 95, 98, 100, 103, 105, 107, 110, 112, 115, 117, 119, 122, 124, 127, 129, 131, 134, 136, 139, 141, 143, 146, 148], [5, 8, 10, 12, 15, 17, 20, 22, 24, 27, 29, 32, 34, 36, 39, 41, 44, 46, 48, 51, 53, 56, 58, 60, 63, 65, 68, 70, 72, 75, 77, 80, 82, 84, 87, 89, 92, 94, 96, 99, 101, 104, 106, 108, 111, 113, 116, 118, 120, 123, 125, 128, 130, 132, 135, 137, 140, 142, 144, 147, 149], [6, 9, 11, 13, 16, 18, 21, 23, 25, 28, 30, 33, 35, 37, 40, 42, 45, 47, 49, 52, 54, 57, 59, 61, 64, 66, 69, 71, 73, 76, 78, 81, 83, 85, 88, 90, 93, 95, 97, 100, 102, 105, 107, 109, 112, 114, 117, 119, 121, 124, 126, 129, 131, 133, 136, 138, 141, 143, 145, 148, 150], [7, 10, 12, 14, 17, 19, 22, 24, 26, 29, 31, 34, 36, 38, 41, 43, 46, 48, 50, 53, 55, 58, 60, 62, 65, 67, 70, 72, 74, 77, 79, 82, 84, 86, 89, 91, 94, 96, 98, 101, 103, 106, 108, 110, 113, 115, 118, 120, 122, 125, 127, 130, 132, 134, 137, 139, 142, 144, 146, 149, 151], [8, 11, 13, 15, 18, 20, 23, 25, 27, 30, 32, 35, 37, 39, 42, 44, 47, 49, 51, 54, 56, 59, 61, 63, 66, 68, 71, 73, 75, 78, 80, 83, 85, 87, 90, 92, 95, 97, 99, 102, 104, 107, 109, 111, 114, 116, 119, 121, 123, 126, 128, 131, 133, 135, 138, 140, 143, 145, 147, 150, 152], [9, 12, 14, 16, 19, 21, 24, 26, 28, 31, 33, 36, 38, 40, 43, 45, 48, 50, 52, 55, 57, 60, 62, 64, 67, 69, 72, 74, 76, 79, 81, 84, 86, 88, 91, 93, 96, 98, 100, 103, 105, 108, 110, 112, 115, 117, 120, 122, 124, 127, 129, 132, 134, 136, 139, 141, 144, 146, 148, 151, 153], [10, 13, 15, 17, 20, 22, 25, 27, 29, 32, 34, 37, 39, 41, 44, 46, 49, 51, 53, 56, 58, 61, 63, 65, 68, 70, 73, 75, 77, 80, 82, 85, 87, 89, 92, 94, 97, 99, 101, 104, 106, 109, 111, 113, 116, 118, 121, 123, 125, 128, 130, 133, 135, 137, 140, 142, 145, 147, 149, 152, 154], [11, 14, 16, 18, 21, 23, 26, 28, 30, 33, 35, 38, 40, 42, 45, 47, 50, 52, 54, 57, 59, 62, 64, 66, 69, 71, 74, 76, 78, 81, 83, 86, 88, 90, 93, 95, 98, 100, 102, 105, 107, 110, 112, 114, 117, 119, 122, 124, 126, 129, 131, 134, 136, 138, 141, 143, 146, 148, 150, 153, 155]]
scales = [chromatic_scales, major_scales, natural_scales, harmonic_scales, dorian_scales, mixolydian_scales, min_pent_scales]
scale_names = ["Chromatic", "Major", "Natural Minor", "Harmonic Minor", "Dorian", "Mixolydian", "Minor Pentatonic"]
knob_list = [1, 14, 15, 16, 17, 18, 19, 20, 21]


notes_dict = { 	

				"C": 0,
				"C#": 1,
				"D": 2,
				"D#": 3,
				"E": 4, 
				"F": 5,
				"F#": 6,
				"G": 7,
				"G#": 8,
				"A": 9,
				"A#": 10,
				"B": 11,

			}


key_dict = {

	'36': 48,
	'37': 50,
	'38': 52,
	'39': 53,
	'40': 55,
	'41': 57,
	'42': 59,
	'43': 60,
	'44': 62,
	'45': 64,
	'46': 65,
	'47': 67,
	'48': 69,
	'49': 71,
	'50': 72,
	'51': 74,
	'52': 49,
	'53': 51,
	'54': 300, # unlit keys play impossible note (to prevent error)
	'55': 54,
	'56': 56,
	'57': 58,
	'58': 300, #
	'59': 61,
	'60': 63,
	'61': 300, #
	'62': 66,
	'63': 68,
	'64': 70,
	'65': 300, #
	'66': 73, 
	'67': 75,	

}


# 1-16 - 48, 50, 52, 53, 55, 57, 59, 60, 62, 64, 65, 67, 69, 71, 72, 74, 76, 77, 79, 
# 81, 83, 84, 86, 88, 89, 91, 93, 95, 96, 98, 100, 101,  103, 105, 107, 108, 110 

#17-32 - 49, 51, 54, 56, 58, 61, 63, 66, 
# 68, 70, 73, 75, 78, 80, 82, 85, 87, 90, 92, 94, 97, 99, 102, 104, 106, 109, 111