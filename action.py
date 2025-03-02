import itertools
import midi  
import arrangement 
import channels 
import general
import device 
import mixer 
import patterns
import playlist 
import plugins  
import transport 
import ui 
import config 
from notes import Notes, Scales 
from modes import Mode
import modes
import utility
from shifter import Shifter

class Action():

    def __init__(self, mode_manager, state):
        self.mode_manager = mode_manager
        self.state = state
        self.colors = itertools.cycle(config.COLORS)

    def call_func(self, f):
        method = getattr(Action, f)
        return method(self)

    def pad_channel(self):
        channels.selectOneChannel(self.state.track_number) 
        channels.midiNoteOn(channels.selectedChannel(), 60, 127)        

    def shift_pattern_right(self):
        shift = Shifter()
        return shift.forward()  

    def shift_pattern_left(self):
        shift = Shifter()
        return shift.back()

    def change_mode(self):
         self.mode_manager.set_mode()

    def change_sub_mode(self):
        self.mode_manager.current_mode.cycle_submode(1)

    def channel_mixer(self):
        if ui.getFocused(midi.widMixer):
            self.focus_channels()
        elif ui.getFocused(midi.widChannelRack):
            self.focus_mixer()
        else:
            self.focus_channels()

    def octave_up(self):
        self.state.octave_index += 1
        if (self.state.octave_index < 0):
            self.state.octave_index = len(Notes.octaves) - 1
        ui.setHintMsg(f"Octave: {self.state.octave_index}")

    def octave_down(self):
        self.state.octave_index -= 1
        if (self.state.octave_index < 0):
            self.state.octave_index = len(Notes.octaves) - 1
        ui.setHintMsg(f"Octave: {self.state.octave_index}")

    def get_octave(self):
        return Notes.octaves[self.state.octave_index]

    def set_random_max_octave(self, data2):
        self.state.random_max_octave = int(utility.mapvalues(data2, 0, 10, 1, 127))
        ui.setHintMsg(f"Max Octave: {self.state.random_max_octave}")
        return 

    def set_random_min_octave(self, data2):
        self.state.random_min_octave = int(utility.mapvalues(data2, 0, 10, 1, 127))
        ui.setHintMsg(f"Min Octave: {Action.random_min_octave}")
        return 

    def get_mixer_route(self):
        return self.state.mixer_send

    def mixer_route(self):
        return mixer.setRouteTo(mixer.trackNumber(), self.get_mixer_route(), 1)

    def start(self): 
        return transport.start()    

    def start_reset(self):
        if (transport.isPlaying()):
            transport.stop()
            transport.start()
        else:
            transport.start()

    def stop(self):
        return transport.stop()

    def record(self):
        return transport.record()

    def song_pat(self):
        return transport.setLoopMode()

    def step_rec(self):
        return transport.globalTransport(midi.FPT_StepEdit, 114)        

    def overdub(self):
        return transport.globalTransport(midi.FPT_Overdub, 112)

    def metronome(self):
        return transport.globalTransport(midi.FPT_Metronome, 110)

    def loop_record(self):
        return transport.globalTransport(midi.FPT_LoopRecord, 113)

    def pattern_down(self):
        return transport.globalTransport(midi.FPT_PatternJog, -1)

    def pattern_up(self):
        return transport.globalTransport(midi.FPT_PatternJog, 1)

    def jog_wheel_up(self):
        return ui.jog(1)

    def jog_wheel_down(self):
        return ui.jog(-1)

    def bpm_plus(self):
        for i in range(10):
            transport.globalTransport(midi.FPT_TempoJog, 1)

    def bpm_minus(self):
        for i in range(10):
            transport.globalTransport(midi.FPT_TempoJog, -1)


    def jog_tempo_up(self):
        return transport.globalTransport(midi.FPT_TempoJog, 1)

    def jog_tempo_down(self):
        return transport.globalTransport(midi.FPT_TempoJog, -1)

    def open_editor(self):
        channels.showEditor();

    def mute(self):
        if ui.getFocused(0):
            return mixer.muteTrack(mixer.trackNumber())
        elif ui.getFocused(1):
            return channels.muteChannel(channels.selectedChannel())
        elif ui.getFocused(2):
            playlist.muteTrack(self.state.selected_playlist_track)

    def open_channel(self):
        return channels.showCSForm(channels.selectedChannel(), -1)

    def up(self):
        return ui.up()

    def down(self):
        return ui.down()

    def left(self):
        if ui.getFocused(5) and channels.getChannelType(channels.selectedChannel()) != CT_Sampler:
            return ui.previous()
        elif ui.getFocused(midi.widChannelRack):
            self.pattern_down()
        elif ui.getFocused(midi.widPlaylist):
            return arrangement.jumpToMarker(0, 1)
        else:
            return ui.left()

    def right(self):
        if ui.getFocused(5) and channels.getChannelType(channels.selectedChannel()) != CT_Sampler:
            return ui.next()
        elif ui.getFocused(midi.widChannelRack):
            self.pattern_up()
        elif ui.getFocused(midi.widPlaylist):
            arrangement.jumpToMarker(1, 1)
        else:
            return ui.right()

    def enter(self):
        if ui.getFocused(midi.widChannelRack):
            self.open_channel()
        elif ui.getFocused(midi.widBrowser):
            ui.selectBrowserMenuItem()
            self.focus_browser()
        elif ui.getFocused(midi.widPlaylist):
            arrangement.addAutoTimeMarker(arrangement.currentTime(1), str(arrangement.currentTime(1)))
        else:
            return ui.enter()

    def prev_pre_pat(self):
        if ui.getFocused(midi.widPlugin) and channels.getChannelType(channels.selectedChannel()) != midi.CT_Sampler:
            return ui.previous()
        else:
            self.pattern_down()

    def next_pre_pat(self):
        if ui.getFocused(midi.widPlugin) and channels.getChannelType(channels.selectedChannel()) != midi.CT_Sampler:
            return ui.next()
        else:
            self.pattern_up()     

    def b_down(self):
        ui.navigateBrowser(midi.FPT_Down, 0)

    def b_right(self):
        ui.navigateBrowser(midi.FPT_Right, 1)

    def b_left(self):
        ui.navigateBrowser(midi.FPT_Left, 0)

    def b_select(self):
        ui.selectBrowserMenuItem()

    def undo(self):
        transport.globalTransport(midi.FPT_Undo, 20)

    def focus_mixer(self):
        ui.showWindow(midi.widMixer)

    def focus_channels(self):
        ui.showWindow(midi.widChannelRack)

    def focus_playlist(self):
        ui.showWindow(midi.widPlaylist)

    def focus_piano(self):
        ui.showWindow(midi.widPianoRoll)

    def focus_browser(self):
        ui.showWindow(midi.widBrowser)

    def set_root_note(self):
        self.state.root_note += 1
        if self.state.root_note >= len(Notes.note_list):
            self.state.root_note = 0
        ui.setHintMsg(Notes.root_name(self.state.root_note))

    def increment_scale(self):
        self.state.scale_choice += 1
        if self.state.scale_choice >= len(Scales.scales):
            self.state.scale_choice = 0
        ui.setHintMsg(Scales.get_scale_name(self.state.scale_choice))

    def open_plugins(self):
        transport.globalTransport(midi.FPT_F8, 67)

    def cut(self):
        ui.cut()

    def copy(self):
        ui.copy()

    def copy_all(self):
        channels.selectAll()
        ui.copy()

    def paste(self):
        ui.paste()

    def insert(self):
        ui.insert()

    def delete(self):
        ui.delete()

    def next(self):
        ui.next()

    def previous(self):
        ui.previous()

    def escape(self):
        if ui.isInPopupMenu():
            print('in pop up menu')
        ui.escape()

    def next_preset(self):
        if plugins.isValid(channels.selectedChannel()):
            plugins.nextPreset(channels.selectedChannel())  

    def prev_preset(self):
        if plugins.isValid(channels.selectedChannel()):
            plugins.prevPreset(channels.selectedChannel())

    def arm(self):
        mixer.armTrack(mixer.trackNumber())

    def quantize(self):
        channels.quickQuantize(channels.selectedChannel())

    def rotate_set_windows(self):
        self.state.rotate_set_count += 1
        if self.state.rotate_set_count >= len(config.SET_WINDOWS):
            self.state.rotate_set_count = 0
        ui.showWindow(config.SET_WINDOWS[self.state.rotate_set_count])

    def rotate_all(self):
        ui.nextWindow()

    def tap_tempo(self):
        transport.globalTransport(midi.FPT_TapTempo, 100)

    def wait_for_input():
        transport.globalTransport(midi.FPT_WaitForInput, 111)

    def item_menu(self):
        transport.globalTransport(midi.FPT_ItemMenu, 91)

    def menu(self):
        transport.globalTransport(midi.FPT_Menu, 90)

    def undo_up(self):
        transport.globalTransport(midi.FPT_UndoUp, 21)  

    def undo_down(self):
        general.undoDown()

    def countdown(self):
        transport.globalTransport(midi.FPT_CountDown, 115)
    
    def new_pattern(self):
        transport.globalTransport(midi.FPT_F4, 63)

    def clone_pattern(self):
        patterns.clonePattern()

    def link_last_tweaked(self):
        print('link_last_tweaked')
        device.linkToLastTweaked(1, channels.selectedChannel()) 

    def save(self):
        transport.globalTransport(midi.FPT_Save, 92)

    def snap_toggle(self):
        transport.globalTransport(midi.FPT_Snap, 48)

    def solo(self):
        if ui.getFocused(midi.widMixer):
            mixer.soloTrack(mixer.trackNumber())
        elif ui.getFocused(midi.widChannelRack):
            channels.soloChannel(channels.selectedChannel())
        elif ui.getFocused(midi.widPlaylist) and playlist.isTrackSelected(self.state.selected_playlist_track):
            playlist.soloTrack(self.state.selected_playlist_track)  

    def link_mix(self):
        mixer.linkTrackToChannel(0)
        # (mode) can be one of the: ROUTE_ToThis = 0, ROUTE_StartingFromThis = 1

    def link_mix_relative(self):
        mixer.linkTrackToChannel(1)

    def double_pattern(self):
        '''Repeats steps and notes for all channels in current pattern, doubling its length '''
        pattern = patterns.patternNumber()
        original_length = patterns.getPatternLength(pattern)

        new_length = original_length * 2
        if new_length >= 129:
            print("Pattern too long for doubling")
        else:
            for channel in range(channels.channelCount()):
                for step in range(original_length):
                    new_step = step + original_length  # Calculate the new step index
                    bit = channels.getGridBit(channel, step)
                    channels.setGridBit(channel, new_step, bit)

                    if bit:  
                        note = channels.getStepParam(step, 0, channel, 0, 64)  # Use 64 as padsStride
                        channels.setStepParameterByIndex(channel, pattern, new_step, 0, note) # Use 64 as padsStride

    def print_plugin_data(self):
        '''Outputs plugin parameters and their associated value for use in plugindata.py '''
        plug_dict = {}
        count = plugins.getParamCount(channels.selectedChannel())
        store = []
        num_list = [i for i in range(0, count + 1)]
                
        for i in range(count):
            name = plugins.getParamName(i, channels.selectedChannel())
            store.append(name)
        # print(store)
        # plug_dict = dict(list(enumerate(store)))  # name as value - or -
        plug_dict = dict(zip(store, num_list))      # name as key 
        print(plugins.getPluginName(channels.selectedChannel()))
        print(plug_dict)

    def item_menu(self):
        transport.globalTransport(midi.FPT_ItemMenu, 91)

    def countdown(self):
        transport.globalTransport(midi.FPT_CountDown, 115)

    def select_next_channel(self):
        print(channels.selectedChannel())
        print(self.state.channel_index)
        if self.state.channel_index == -1:
            self.state.channel_index = channels.selectedChannel()
        elif self.state.channel_index >= channels.channelCount() - 1:
            self.state.channel_index = -1
        self.state.channel_index += 1
        channels.selectChannel(self.state.channel_index)

    def change_step_parameter(self):
        self.state.parameter_index += 1
        if self.state.parameter_index > 6:
            self.state.parameter_index = 0
        ui.setHintMsg(f"{self.state.parameter_index}")
        channels.showGraphEditor(True, self.state.parameter_index, self.state.selected_step, channels.selectedChannel())

    def change_color(self):
        if config.COLORS:
            if ui.getFocused(midi.widChannelRack):
                channels.setChannelColor(channels.selectedChannel(), next(self.colors))
            elif ui.getFocused(midi.widMixer):
                mixer.setTrackColor(mixer.trackNumber(), next(self.colors))
            elif ui.getFocused(midi.widPlaylist) and playlist.isTrackSelected(self.state.selected_playlist_track):
                playlist.setTrackColor(self.state.selected_playlist_track, next(self.colors))
        else:
            print('No colors set in config.py file')

    def get_color(self):
        if ui.getFocused(midi.widChannelRack):
            print(f"Add {channels.getChannelColor(channels.selectedChannel())}, to COLORS in config.py, including dash and comma")

    def trig_clip(self):
        mode = playlist.getLiveLoopMode(self.state.performance_row)
        if playlist.getLiveBlockStatus(self.state.performance_row, self.state.track_number, 2) == 2: 
            if mode == 1:
                print(f"mode: {playlist.getLiveLoopMode(self.state.performance_row)}");
                playlist.triggerLiveClip(self.state.performance_row, self.state.track_number, midi.TLC_MuteOthers | midi.TLC_Fill)
            else:
                playlist.triggerLiveClip(self.state.performance_row, -1, midi.TLC_MuteOthers | midi.TLC_Fill)

        else:
            playlist.triggerLiveClip(self.state.performance_row, self.state.track_number, midi.TLC_MuteOthers | midi.TLC_Fill)

    def random_trigs(self):
            """Function clears pattern and for each step, generates a random number. The number is checked"""
            for i in range(patterns.getPatternLength(patterns.patternNumber())): 
                channels.setGridBit(channels.selectedChannel(), i, 0)
            for z in range (patterns.getPatternLength(patterns.patternNumber())):
                y = utility.num_gen()
                if y < ( self.state.random_offset * 516):
                    channels.setGridBit(channels.selectedChannel(), z, 1)
                else:
                    pass

    def random_notes(self):
        """function sets random notes for selected pattern when called based on scale/root selected in switch along with Knob() class"""

        scale = self.state.scale_choice
        root = self.state.root_note
        upper = self.state.random_max_octave
        lower = self.state.random_min_octave
        for i in range(patterns.getPatternLength(patterns.patternNumber())):
            interval = Scales.scales[scale][int(utility.mapvalues(utility.num_gen(), 0, len(Scales.scales[scale]), 0, 65535))]
            octave = int(utility.mapvalues(utility.num_gen(), lower, upper, 0, 65535)) * 12
            note = interval + octave
            finalNote = note + root
            channels.setStepParameterByIndex(channels.selectedChannel(), patterns.patternNumber(), i, 0, finalNote)     

    def random_pattern(self):
        self.random_trigs()
        self.random_notes()

    def shift(self):
        if self.state.shift_status == 0:
            self.state.shift_status = 1
            ui.setHintMsg('Shift Active')
        elif self.state.shift_status == 1:
            self.state.shift_status = 0
            ui.setHintMsg('Shift Disabled')
        self.state.set_plus_minus_leds()

    def get_shift_status(self):
        return self.state.shift_status

    def set_random_offset(valself):
        self.state.random_offset = val
        ui.setHintMsg(f'Random: {int(val/127 * 100)}%')

    def get_step_param(self):
        return self.state.parameter_index

    def nothing(self):
        pass

    def zoom_in_horz(self):
        ui.horZoom(1)

    def zoom_out_horz(self):
        ui.horZoom(-1)

    def zoom_in_vert(self):
        ui.verZoom(1)

    def zoom_out_vert(self):
        ui.verZoom(-1)

    def mixer_solo(self):
        print(f"track_num {self.state.track_number}")
        mixer.soloTrack(self.state.track_number)

    def mixer_record(self):
        print(f"track_num {self.state.track_number}")
        mixer.armTrack(self.state.track_number)

    def mixer_mute(self):
        print(f"track_num {self.state.track_number}")
        mixer.muteTrack(self.state.track_number)

    def select_pattern(self):
        """is pattern_change_wait set, onupbeatindicator will trigger
            change when change_patten = true """

        if self.state.track_original != patterns.patternNumber() and transport.isPlaying() and config.PATTERN_CHANGE_WAIT:
            self.state.change_pattern = True

        else:
            device.midiOutMsg(176, 1, 50, 80)
            patterns.jumpToPattern(self.state.track_original)

    def mute_channel(self):
        chan = self.state.track_original - 1
        if self.state.track_original <= channels.channelCount():
            channels.muteChannel(chan)
    
    def solo_channel(self):
        chan = self.state.track_original - 1
        if self.state.track_original <= channels.channelCount():
            channels.soloChannel(chan)

    def change_pattern_select_mode(self):
        self.state.pattern_change_immediate = not self.state.pattern_change_immediate

    def change_select_range(self):
        self.mode_manager.current_mode.cycle_range()

    def randomize_plugin(self):
        channel = channels.selectedChannel()
        parameter_count = plugins.getParamCount(channel)
        for i in range(parameter_count):
            rand_val = utility.mapvalues(utility.num_gen(), 0, 127, 0, 65535)/127.0
            plugins.setParamValue(rand_val, i, channel)

class EncoderAction(Action):

    parameter_ranges = [ 0, 19, 37, 56, 74, 92, 110, 128 ]

    def set_parameter_value(self, event):

        chan = channels.selectedChannel()
        print(f"chan: {chan}")
        pat = patterns.patternNumber()
        print(f"pat: {pat}")
        step = self.state.selected_step
        print(f"step: {step}")
        param = self.state.parameter_index
        channels.setStepParameterByIndex(chan, pat, step, param, int(utility.mapvalues(event.data2, 0, 255, 0, 127)))
        channels.showGraphEditor(False, self.state.parameter_index, self.state.selected_step, channels.channelNumber(), True)
    #   int index, int patNum, int step, int param, int value, (bool useGlobalIndex = False)

    def call_func(f, event):
        method = getattr(EncoderAction, f)
        return method(event.data2) 

    def set_mixer_route(self, event):
        self.state.mixer_send = event.data2
        ui.setHintMsg(f"Route Mixer to {event.data2}") 

    def set_random_min_octave(self, event):
        self.state.random_min_octave = int(utility.mapvalues(event.data2, 0, 10, 1, 127))
        ui.setHintMsg(f"Min Octave: {self.state.random_min_octave}")
        return 

    def set_random_max_octave(self, event):
        self.state.random_max_octave = int(utility.mapvalues(event.data2, 0, 10, 1, 127))
        ui.setHintMsg(f"Max Octave: {self.state.random_max_octave}")
        return 

    def set_step_parameter(self, event):
        self.state.parameter_index = self.get_param_from_range(event.data2)
        channels.showGraphEditor(True, self.state.parameter_index, self.state.selected_step, channels.selectedChannel())

    def set_random_offset(self, event):
        self.state.random_offset = event.data2
        ui.setHintMsg(f'Random: {int(self.state.random_offset/127 * 100)}%')

    def selected_level(self, event):
        if ui.getFocused(midi.widMixer):
            mixer.setTrackVolume(mixer.trackNumber(), event.data2/127, True)
        elif ui.getFocused(midi.widChannelRack):
            channels.setChannelVolume(channels.selectedChannel(), event.data2/127, True)

    def get_param_from_range(self, cc):
        for i, r in enumerate(EncoderAction.parameter_ranges):
            if cc < r:
                return i 

    def selected_pan(self, event):
        if ui.getFocused(midi.widMixer):
            mixer.setTrackPan(mixer.trackNumber(), utility.mapvalues(event.data2, -1, 1, 0, 127), True)
        elif ui.getFocused(midi.widChannelRack):
            channels.setChannelPan(channels.selectedChannel(), utility.mapvalues(event.data2, -1, 1, 0, 127), True)

    def master_mixer_level(self, event):
        mixer.setTrackVolume(0, event.data2/127, True)

    def set_efx_track(self, event):
        channels.setTargetFxTrack(channels.selectedChannel(), event.data2)

    def set_step(self, event):
        pat_len = patterns.getPatternLength(patterns.patternNumber()) - 1   
        step = int(utility.mapvalues(event.data2, 0, pat_len, 0, 127))
        ui.setHintMsg(f"Step: {step + 1}")              
        return step

    def scroll(self, event):
        if ui.getFocused(midi.widMixer):
            mixer.setTrackNumber(int(utility.mapvalues(event.data2, 0, config.MIXER_SCROLL_MAX, 0, 127)))
            ui.scrollWindow(midi.widMixer, mixer.trackNumber())

        elif ui.getFocused(midi.widChannelRack):
            channels.selectOneChannel(int(round(utility.mapvalues(event.data2, 0, channels.channelCount()-1, 0, 127), 0)))           

        elif ui.getFocused(midi.widPlaylist):
            track = int(utility.mapvalues(event.data2, 1, 30, 0, 127))
            playlist.deselectAll()
            playlist.selectTrack(track)
            self.state.selected_playlist_track = track 
            print(track)

        elif ui.getFocused(midi.widBrowser):
            ui.navigateBrowser(midi.FPT_Down, 41)

    def jog_wheel(self, event):

        """A function specific to the Atom SQ and other compatible controllers whose jog 
        wheel sends the same CC value for up or down, but the data 2 value is different for each.
        In the case of the Atom SQ it is a data 2 value of 65 for up and 1 for down"""

        if event.data2 == 65:
            self.jog_wheel_up(self)
        else:
            self.jog_wheel_down(self)

    def jog_wheel_up(self, event):
        self.jog_wheel_up(self)

    def jog_wheel_down(self, event):
        self.jog_wheel_down(self)

    def mixer_level(self, event):
        print(f"event: {self.state.track_number}")
        mixer.setTrackVolume(self.state.track_number, event.data2/127, True)

    def mixer_pan(self, event):
        mixer.setTrackPan(self.state.track_number, utility.mapvalues(event.data2, -1, 1, 0, 127), True)

    def nothing(self, event):
        pass

