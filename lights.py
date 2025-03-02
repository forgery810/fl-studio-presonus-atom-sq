import device
import channels
import midi
import ui
import mixer
import playlist
import transport
import channels
import patterns
import plugins
from midi import *
import data

top_keys = [52, 53, 55, 56, 57, 59, 60, 62, 63, 64, 66, 67]
continuous_black = [37, 39, 42, 44, 46, 49, 51, 54, 56, 58, 61, 63, 66]
sequence_fours = [36, 40, 44, 48, 52, 56, 60, 64]

led_colors = {
    "purple": {"midi_id": 146, "data_2": 0},
    "light_purple": {"midi_id": 146, "data_2": 60},
    "mid_purple": {"midi_id": 146, "data_2": 10},
    "white": {"midi_id": 144, "data_2": 127},
    "light_white": {"midi_id": 144, "data_2": 6},
    "yellow": {"midi_id": 147, "data_2": 0},
    "light_yellow": {"midi_id": 147, "data_2": 40},
    "blue": {"midi_id": 145, "data_2": 0},
    "light_blue": {"midi_id": 145, "data_2": 50},
    "light_green": {"midi_id": 36, "data_2": 0},
    "off": {"midi_id": 144, "data_2": 0}
}

octave_colors = {
    "plus_white": {"midi_id": 0, "channel": 0, "data_1": 127, "data_2": 0},
    "white": {"midi_id": 0, "channel": 0, "data_1": 127, "data_2": 127},
    "minus_white": {"midi_id": 0, "channel": 1, "data_1": 127, "data_2": 0},
    "plus_turquoise": {"midi_id": 144, "channel": 0, "data_1": 1, "data_2": 127},
    "plus_off": {"midi_id": 144, "channel": 0, "data_1": 0, "data_2": 0}
}


class Lights:
    def __init__(self, num_leds=32):
        self.off_keys = (54, 58, 61, 65)
        self.num_leds = num_leds
        # Initialize all LEDs to "off"
        self._led_state = [(i, 0, "off") for i in range(36, 36 + num_leds)]
        self.c_keys = [36, 43, 50]
        self.c_keys_cont = [36, 48, 60]


    @property
    def led_state(self):
        return self._led_state

    def update_octaves(self, new_state):
        for color in new_state:
            if color in octave_colors:
                color_data = octave_colors[color]
                midi_id = color_data["midi_id"]
                data_2 = color_data["data_2"]
                data_1 = color_data["data_1"]
                channel = color_data["channel"]
                device.midiOutMsg(midi_id, channel, data_1, data_2)
            else:
                print("color not in octave_colors")

    def update_led_state(self, new_state):
        """Updates the internal LED state based on the provided new_state.

        Args:
            new_state: A list of tuples, where each tuple represents the desired state 
                       of an LED: (led_number, state, color_name).
                       - led_number: The number of the LED (36-67 on the Atom SQ).
                       - state: 1 for on, 0 for off.
                       - color_name: The name of the color (e.g., "red", "blue", "off").
        """
        for led_num, state, color_name in new_state:
            if 36 <= led_num < 36 + self.num_leds:
                index = led_num - 36
                # self.led_state[index] = (led_num, state, color_name)
                self._led_state[index] = (led_num, state, color_name)  # Update _led_state                

    def send_midi_messages(self):
        """Translates the current LED state into MIDI messages and sends them to the device."""
        for led_num, state, color_name in self._led_state:
            if state == 1 and color_name in led_colors:
                device.midiOutMsg(144, 0, led_num, 127) # send white first
                color_data = led_colors[color_name]
                midi_id = color_data["midi_id"]
                data_2 = color_data["data_2"]
                device.midiOutMsg(midi_id, 0, led_num, data_2)
            else:
                # Use "off" color to turn off
                device.midiOutMsg(led_colors["off"]["midi_id"], 0, led_num, led_colors["off"]["data_2"])

    def clear_all_leds(self):
        """Turns off all LEDs by setting their state to 'off'."""
        self.update_led_state([(i, 0, "off") for i in range(36, 36 + self.num_leds)])
        self.send_midi_messages()

    def all_leds_white(self):
        """Turns off all LEDs by setting their state to 'off'."""
        self.update_led_state([(i, 0, "white") for i in range(36, 36 + self.num_leds)])
        self.send_midi_messages()

    def set_led_on(self, led_num, color_name):
        """Turns on a specific LED with a given color.

        Args:
            led_num: The LED number.
            color_name: The name of the color.
        """
        if color_name in led_colors:  # Validate color
            self.update_led_state([(led_num, 1, color_name)])
            self.send_midi_messages()
        else:
            print(f"Error: Invalid color name '{color_name}'")

    def set_led_off(self, led_num):
        """Turns off a specific LED."""
        self.update_led_state([(led_num, 0, "off")])
        self.send_midi_messages()

    def set_led_color(self, led_num, color_name):
        """Changes the color of a specific LED (even if it's already on)."""
        if color_name in led_colors:
            self.update_led_state([(led_num, 1, color_name)])
            self.send_midi_messages()
        else:
            print(f"Error: Invalid color name '{color_name}'")


class Color():
    """Returns the color values for the various colors."""

    colors = {
            "purple": 146,
            "white": 144,
            "yellow": 127,
            "blue": 145
        }

    def get(color):
        return Color.colors[color]