# Presonus Atom SQ MIDI Script for FL Studio

A python MIDI-script to increase the functionality of the Presonus Atom SQ with FL Studio

This is in the beta stage with known bugs and far from complete functionality.
It is functioning well enough to be useful.

If you use this please let me know of any bugs through github or any suggestions at forgery810@gmail.com

#   FL Studio Setup

Update to the latest FL Studio version. This will not work on some earlier versions of FL.

Clone and unzip. Copy folder to Dcouments/Image-Line/Fl Studio/Settings/Hardware
The data should be in a folder together within the Hardware directory.

In the FL Studio Midi Settings, click Refresh Device List. Enable both ATM SQ and MIDIIN2(ATM SQ) and set contoller type to 
Presonus Atom SQ. The should be enabled in both Input and Output. Set the ATM SQ to the same port number in both In and Out. 
The same must be done with both MIDIIN2(ATM SQ) In and Out but must be differnt from the ATM SQ port number.

#   Atom SQ Setup

Go to Setup and on the second page set the SQ to MCU mode. Also set A-H to CC mode.

Under User set Touch to Mod.

Unfortunatley, for the jog wheel to function you must be on the first Song page on the SQ with Cursor highlighted. Otherwise the arrows can be used to move around.
I encourage you to email Presonus to allow the jog wheel to always be active (as well as allowing more shift functionality) 


# Manual:

Letter Buttons:

A is the enter button
B opens the channel window for selected channel
D brings up the plugin picker
E toggles through 3 main modes Notes, Step Sequencer and Pad per Channel
F selects sub-menus
G currently rotates between Piano, Browser, and Playlist windows
H currently rotates between the mixer and channel windows


Transport buttons:

These function as labeled. Shift can be used to access the secondary functions with the expception of Count-in for some reason

Song buttons:

Page 1:

Solo and mute work as expected. If the Mixer window is focused the Arm button will toggle record. If the channels window is focused, 
it will set the current channel to the mixer path of the last selected mixer track. 

Page 2:

Button 1 applies quantizer to selected channel.

Button 4 adds random steps to selected channel in step-mode.

Button 5 applies random notes to selected channel. (See below)

# Pad Modes

In Notes mode the pads become a keyboard (currently not set up. The lights reflect a keyboard but do not play as one. The Pads mode on the Atom SQ under Inst must be changed to key to play as a keyboard)

# Step Sequencer 

Ocatve must be set to zero for this mode to work correctly.
   
When Channels are focused and Step Entry is selected the pads will now input steps. Arrows or jog wheel can used to select the channel. The leds will 
change to reflect the state of the current pattern.  
   
The step-sequencer has four sub-menus: 32 Steps, Pattern Access, Parameter, and Random. 
   
In any sub-menu Button 4 can be used to add random steps. The touchpad controls the liklihood of each step being set on. Touch to the left and all 
steps will be on and to the right for less. This can be used to clear patterns as well the furthest right will almost always empty the patterm.
   
In 32 steps, the top row extends access to steps 17-32.
   
In Pattern Access, the top row allows instant access to patterns 1-16.
   
In Parameter Entry mode, individual steps can be selected to edit their parameters. Select an active step and the knobs can be used to edit the 
Pitch, Velocity, Release, Fine Pitch, Panning, Mod X, and Mod Y of that step using the knobs 1-7 respectively. 
    
In Random mode, random notes from various scales can be applied to a channel. Knob 5 will choose the root note (this will appear in the hint message on the top left of FL).
Knob 6 chooses the scale and knobs 7 and 8 control the low and high range of notes to be used. Push Button 5 to apply.
   

# Knobs

If the Mixer is focused, knob 5 will control the volume of the selected channel and knob 6 will control the panning.

If Channels are focused, the knobs will control the volume of channels 1-8 respectively. Currently, this is limited to those channels but functionality to add control of all channels will be added. 


# Jog Wheel

The jog wheel will scroll through mixer tracks and channels when the respective window is open. As mentioned earlier, due to an unfortunate quirk with the SQ the first page of the Song mode must be open on the controller or the jog wheel does not send any midi data. The jog wheel can be used along with the arrow buttons to scroll through the browser when selected. 


# Bugs

While the up and down arrows work, they have a quirk where the will go the right direction and then every fifth push or so go the wrong direction for one push. It can still get you to your destination though.  

Fixed -> In Pad per Channel mode, recorded notes last until end of pattern. (This has been fixed in 0.01.05)

Not so much a bug, as there may not be anything I can do about it, but the SQ lights the last push button blue or green which can hide the status of its step in step mode. 
