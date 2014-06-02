#!/usr/bin/sudo python
# This first line, which starts with the special characters #! is there to
# tell the rapberry pi how to run the file. You can use it as a reminder as 
# well! To start python open a terminal program and type: sudo python

# This program uses three different libraries which we must "import" before
# we can use them.
import pibrella, random, time

mychoices = ( pibrella.light.red, pibrella.light.yellow, pibrella.light.green )
for i in range(50):
	light = random.choice(mychoices)
	light.toggle()
	time.sleep((random.random() / 2) + 0.1)

#
# Breaking it apart:
#
# Line 1:
#
#   mychoices is a "tuple" (a group of objects) containing three things, the
#   red light object, the yellow light object and the green light object.
#   
#   Commands to try:
#
#     mychoices
#     mychoices[0].on()
#     mychoices[0].off()
#     mychoices[2].toggle()
#
# Line 2:
#
#   Makes the indented commands run 50 times. This is called a loop. The first
#   line called the loop condition and the indented lines are called the
#   loop body.
#
#   Commands to try:
#
#     range(50)
#     range(5)
#     for i in range(5):
#         print i
#
# Line 3:
#
#   Selects a random value from mychoices and stores it in a "variable" called
#   light.
#
#   Commands to try (repeat these, random things don't go the same thing
#   every time):
#
#     random.choice(mychoices)
#     random.choice(mychoices).toggle()
#
# Line 4:
#
#   Makes the object held in the variable called light change its state
#   (on becomes off and off becomes on).
#
#   Commands to try:
#
#     light = mychoices[0]
#     light.toggle()
#     light.on()
#     light.off()
#     light = pibrella.light.green
#     light.toggle()
#
# Line 5:
#
#   Makes the program do nothing for a short but randomly selected period
#   of time.
#
#   Commands to try (repeat these, random things don't go the same thing
#   every time):
#
#     random.random()
#     random.random() / 2
#     (random.random() / 2) + 0.1
#     (random.random() / 10) + 0.9
#     time.sleep(5)
#

# 
# Challenges:
#
# 1. Make the random blinking go faster (change both numbers).
#
# 2. Make the random blinking happen as fast as possible.
#
# 3. Make the random blinking happen at the speed you thing is nicest!
#
# 4. Make the random blinking run forever.
#
#    As a hint find out what this command does (and when you find out, press
#    Control and C to stop the program):
#
#      while True:
#          print("Why not try moving the scroll bar?")
# 
# 5. Make four more of the lights on the pibrella join in the blinking.
#
#    Hint:
#
#      pibrella.output.e.toggle()
#      pibrella.output.h.toggle()
#      A, B, C, D, E, ...
#
