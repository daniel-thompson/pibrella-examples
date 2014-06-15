
# coding: utf-8

## Quick reference

# Always begin by importing (at least) the pibrella libary:

# In[ ]:

import pibrella


# All of Pibrella's inputs, outputs and lights are stored in collectons. You can reference a pin by name or by number in any of three ways:

# In[ ]:

pibrella.light[0]


# In[ ]:

pibrella.light['red']


# In[ ]:

pibrella.light.red


# You can also perform actions on every object in a collection at once:

# In[ ]:

pibrella.light


# There are lots of different collections and objects can appears in more than one collection:
# 
# * `pibrella.pin` contains an object for every "pin" in the pibrella: a, b, c, d, button, buzzer, red, yellow, green, e, f, g, h.
# * `pibrella.input` contains an object for every input pin: a, b, c, d
# * `pibrella.output` contains an object for every output pin: e, f, g, h
# * `pibrella.light` contains an object for every light: red, yellow, green

# Examples:

# In[ ]:

pibrella.pin.read()


# In[ ]:

pibrella.output.blink()


# In[ ]:

pibrella.output.off()


## Outputs and lights

# Outputs and lights accept exactly the same set of commands:
# 
# * `.on()` turns the output or light on
# * `.off()` turns the output or light off
# * `.toggle()` changes the output from on to off or from off to on
# * `.write(state)` sets the output from a variable (1 is on and 0 is off)
# * `.pulse()` causes the output to fade on and off. Variants include: `.pulse(fade_time)` and `.pulse(fade_on_time, fade_off_time, time_on, time_off)`.
# * `.blink()` dauses the output to turn on and off without fading. Variants include: `.blink(time)` and `.blink(time_on, time_off)`
# * `.read()` gets the current state of the pin

# Examples:

# In[ ]:

pibrella.output.pulse(2, 0.25, 1, 0.25)


# In[ ]:

pibrella.light.red.blink(0.05)


# In[ ]:

pibrella.output.off(); pibrella.light.off()


## Inputs

# The inputs include the input pins: a, b, c and d together with the button. Commands include:
# 
# * `.read()` gets the current state of the input
# * `.changed(handler)` allows a change of state handler to be installed

# Examples:

# In[ ]:

pibrella.input.read()


# In[ ]:

def button_pressed(pin):
    print pin.read()
pibrella.button.changed(button_pressed)


## Buzzer

# The buzzer supports a wide range of commands including:
# 
# * `.buzz(frequency)` buzzes at a fixed frequency (if you are musical try 440Hz, this is the "A" note you tune to)
# * `.note(number)` buzzes as musical pitches. The number you must give is the number of semitones above or below "A"
# * `.off()` stops the buzzer from making any noise
# * `.success()` plays a happy sound
# * `.fail()` plays a sad sound
# * `.melody((notes), note_length)` plays the notes in a loop. To avoid looping try `.melody((notes), note_length, False)` 

# Examples:

# In[ ]:

pibrella.buzzer.melody((0, 2, 4, 5, 7, 9, 11, 12), 0.25)


# In[ ]:

pibrella.buzzer.off()


## Other calls

# Finally there are some commands that can be run without an object. Instead these command are used directly on the imported library.
# 
# * `pibrella.pause()` prevents you script from exiting (allowing you to see any pulsing, blinking or buzzing)
# * `pibrella.loop(handler)` allows you to run the handler function over and over again. Use this to run complicated sequences of commands "in the background" whilst you continue to work at the python prompt.
