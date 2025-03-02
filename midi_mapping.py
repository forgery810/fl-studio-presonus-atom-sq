# Initial Key is MIDI Channel
# The next is MIDI ID. Value corresponds with user function assigned in config.py 
# Used in MidiHandler Class in handler.py
controller = {

    "name": "Presonus Atom SQ",
    "knob_count": 8,
    "pad_notes_top": range(52, 68),
    "pad_notes_bottom": range(36, 52),



    "buttons": 
            {
            0: {    24: "a",
                    25: "b",
                    26: "c",
                    27: "d",
                    28: "e",
                    29: "f",
                    30: "g",
                    31: "h",
                    93: "stop",
                    81: "shift_stop",
                    94: "start",
                    86: "shift_start",
                    95: "record",
                    80: "shift_record",
                    89: "metronome",
                    9: "solo", 
                    8: "solo", 
                    10: "solo", 
                    11: "solo", 
                    12: "solo", 
                    13: "solo", 
                    14: "solo",
                    15: "solo",
                    16: "mute", 
                    17: "mute", 
                    18: "mute", 
                    19: "mute", 
                    20: "mute", 
                    21: "mute", 
                    22: "mute",
                    23: "mute",
                    0: "arm", 
                    1: "arm", 
                    2: "arm", 
                    3: "arm", 
                    4: "arm", 
                    5: "arm", 
                    6: "arm",
                    7: "arm",
                     98: "left_arrow",
                    99: "right_arrow",
                },
                
            1: {    24: "a2",
                    25: "b2",
                    26: "c2",
                    27: "d2",
                    28: "e2",
                    29: "f2",
                    30: "g2",
                    31: "h2", 
            },
            
            2: {
                    24: "button_1",
                    25: "button_2",
                    26: "button_3",
                    27: "button_4",
                    28: "button_5",
                    29: "button_6",
                },
    },  

    "encoders": 
            {
                0: {
                    60: "jog_wheel",
                    14: "knob_1",
                    15: "knob_2",
                    16: "knob_3",
                    17: "knob_4",
                    18: "knob_5",
                    19: "knob_6",
                    20: "knob_7",
                    21: "knob_8",
                    1: "touch_mod",
                    9: "touch_cc"
                },

                1: {
                    14: "knob_9",
                    15: "knob_10",
                    16: "knob_11",
                    17: "knob_12",
                    18: "knob_13",
                    19: "knob_14",
                    20: "knob_15",
                    21: "knob_16",
                },

                2: {
                    14: "knob_17",
                    15: "knob_18",
                    16: "knob_19",
                    17: "knob_20",
                    18: "knob_21",
                    19: "knob_22",
                    20: "knob_23",
                    21: "knob_24",
                },

                3: {
                    14: "knob_25",
                    15: "knob_26",
                    16: "knob_27",
                    17: "knob_28",
                    18: "knob_29",
                    19: "knob_30",
                    20: "knob_31",
                    21: "knob_32",
                },
            },
    "jog": {
        "midi_id": 176, 
        "data1": 60,
    },



    "default_mode": "NOTES",
}
