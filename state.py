import config
import channels
import lights
import device

class State:
    def __init__(self):
        # From Notes
        self.octave_index = 3
        self.root_note = 0  
        self.scale_choice = 0

        # From Action
        self.random_max_octave = 3
        self.random_min_octave = 6
        self.random_offset = 63
        self.selected_step = 0
        self.selected_steps = []
        self.track_number = -1
        self.track_original = -1

        # Other variables that were in Action:
        self.active_track = 0
        self.parameter_index = 0
        self.mixer_num = 0
        self.mixer_send = 2
        self.rotate_set_count = 0
        self.shift_status = 0
        self.performance_row = -1
        self.change_pattern = False
        self.selected_playlist_track = 1
        self.current_pattern = 0
        self.next_pattern = 0
        self.pattern_change_immediate = config.PATTERN_CHANGE_IMMEDIATE
        self.pattern_select_range = 0
        self.channel_index = 0

    def set_plus_minus_leds(self):
        plus = lights.octave_colors["plus_white"]
        minus = lights.octave_colors["minus_white"]
        if self.shift_status:
            plus = lights.octave_colors["plus_off"]
        device.midiOutMsg(plus["midi_id"], plus["channel"], plus["data_1"], plus["data_2"])
        device.midiOutMsg(minus["midi_id"], minus["channel"], minus["data_1"], minus["data_2"])

