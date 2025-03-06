#File for script configuration. See www.midicontrol.cc/atom-sq for more info

browser = 4
piano = 3
playlist = 2
channels = 1
mixer = 0
""" Do not change the lines above """

ACTIVE_MODES = [
    "NOTES",      
    "STEP_SEQUENCER",
    "PAD_PER_CHANNEL",
    "MIXER_CONTROL"
]
"""Chose from the following: "NOTES", "STEP_SEQUENCER", "PAD_PER_CHANNEL", "MIXER_CONTROL" """

NOTES_SUBMODES = ["KEYBOARD", "CONTINUOUS", "DRUM"]
""" Choose from "KEYBOARD", "CONTINUOUS", "DRUM" """

STEP_SEQUENCER_LAYOUTS =  ["STEP_32", "PATTERN_ACCESS", "CHANNEL_MUTE", "CHANNEL_SELECT"]
""" Chose from "STEP_32", "PATTERN_ACCESS", "CHANNEL_MUTE", "CHANNEL_SELECT" """

COLORS = [0, 10963273, 4311177, 4293320, 14264921, 10517732]
""" Color numbers can be found at www.midicontrol.cc/fl-colors. There is no limit to how many can be added. Make sure a comma follows each number."""

SET_WINDOWS = [mixer, channels, browser] 
""" This controls what windows the rotate_set_windows will rotate through. Only choose from the options at the top of the page. """

LIGHT_CURRENT_STEP = True
""" If True, when sequencer mode is active, current step in the sequence will be lit """

FOLLOW_TRACK = True			
""" Set to True if you want your encoders to automatically adjust what mixer tracks 
	they control based on the currently highlighted track. Only relavent if you have 
	encoders set to control specific tracks. This is used in conjuction with the 
	Number of Mixer Tracks setting on the web app. For example, if you have a controller 
	set to control mixer tracks 1-8, if you highlight any track between 9-16, they will then control 
	tracks 9-16 respectively. This affects track level, arm, mute, solo and pan.""" 
	
PATTERN_CHANGE_IMMEDIATE = True
""" This only affects pattern changes when using the 'Select Pattern *' where buttons are 
	set with specific patterns to change to when pushed. If set to true, the pattern will not
	change until the end of the current bar. False will mean patterns are changed immediately."""

ROOT_NOTE = "C"
SCALE = "Natural Minor"

""" Root Note and Scale combined will set the default scale the script opens with. These can both be changed
	with a MIDI controller if you dedicate buttons to it. It may be easier, though, to change the values here
	and reload the script and dedicated the buttons to a more commonly used function.

	Valid note and scale entries are:
		["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
		["Major", "Natural Minor", "Harmonic Minor", "Dorian", "Mixolydian", "Minor Pentatonic", "Chromatic"] """

MIXER_SCROLL_MAX = 32
""" Sets the max track that the scroll funciton can access. Higher number allow access to more tracks but can make it harder to select individual tracks """

PLUGIN_KNOB_OFFSET = 14
"""This should be left alone. It is used for default plugin control to account for the difference between the data1 value knobs send
and the plugin value to be controlled"""

SELECT_PARAM_STEP = True
""" Ignore """