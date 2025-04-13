import _random 
import itertools
from midi import *
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
import data 

class Shifter():
    def __init__(self):
        self.channel = channels.selectedChannel()
        self.pat_num = patterns.patternNumber()
        self.pat_len = patterns.getPatternLength(self.pat_num)
        print(f"pat_len: {self.pat_len}")
        self.pattern, self.notes = self.get_pattern_and_notes() # Get the old state and notes

    def back(self):
        self.pattern, self.notes = self.shift_left(self.pattern, self.notes) # set our values here
        self.write_to_pattern()

    def forward(self):
        self.pattern, self.notes = self.shift_right(self.pattern, self.notes)  # set our values here
        self.write_to_pattern()

    def get_pattern_and_notes(self):
        """
        Takes current pattern, appends the grid bit and note to separate lists, 
        then returns both.
        """
        pattern = []
        notes = []
        for bit in range(self.pat_len):
            grid_bit = channels.getGridBit(self.channel, bit)
            # int step, int param, int offset, int startPos, (int padsStride = 16), (bool useGlobalIndex* = False)
            note_value = channels.getStepParam(bit, 0, channels.selectedChannel(), 0, self.pat_len)
            print(f"note_value: {note_value}")
            pattern.append(grid_bit)
            notes.append(note_value)  # Store the note value (or None)
        return pattern, notes

    def shift_left(self, data_list, note_list):
        """Shifts a list left by one position, wrapping the first element to the end."""
        if not data_list:  # Check if the list is empty
            return data_list, note_list

        shifted_data = data_list[1:] + data_list[:1]
        shifted_notes = note_list[1:] + note_list[:1]
        return shifted_data, shifted_notes

    def shift_right(self, data_list, note_list):
        """Shifts a list right by one position, wrapping the last element to the beginning."""
        if not data_list:  # Check if the list is empty
            return data_list, note_list

        shifted_data = data_list[-1:] + data_list[:-1]
        shifted_notes = note_list[-1:] + note_list[:-1]
        return shifted_data, shifted_notes

    def write_to_pattern(self):
        """Writes bit shifted pattern and notes to the appropriate channel."""
        if patterns.patternNumber() == self.pat_num:
            for i in range(self.pat_len):
                channels.setGridBit(self.channel, i, 0)
                #Added here that the setStepParameterByIndex function set a value rather than add another function to check if we are adding 0.
                channels.setGridBit(self.channel, i, self.pattern[i])
                channels.setStepParameterByIndex(self.channel, self.pat_num, i, 0, self.notes[i])
            print(self.pattern, self.notes)