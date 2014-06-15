
# coding: utf-8

## Random blink

# This program uses three different libraries which we must "import" before we can use them:

# In[ ]:

import pibrella, random, time


# Next we have the program itself:

# In[ ]:

mychoices = ( pibrella.light.red, pibrella.light.yellow, pibrella.light.green )
for i in range(50):
    light = random.choice(mychoices)
    light.toggle()
    time.sleep((random.random() / 2) + 0.1)


## Breaking it apart

### Line 1

# In[ ]:

mychoices = ( pibrella.light.red, pibrella.light.yellow, pibrella.light.green )


# `mychoices` is a "tuple" (a group of objects) containing three things, the red light object, the yellow light object and the green light object.
# 
# Commands to try to help you understand `mychoices`:

# In[ ]:

mychoices


# In[ ]:

mychoices[0].on()


# In[ ]:

mychoices[0].off()


# In[ ]:

mychoices[2].toggle()


### Line 2

# In[ ]:

for i in range(50):
    print "An example indented line"


# Makes the indented command or commands run 50 times. This is called a loop. The first line is called the loop condition and the indented lines are called the loop body.
# 
# Commands to try:

# In[ ]:

range(50)


# In[ ]:

range(5)


# In[ ]:

for i in range(5):
    print i


### Line 3

# In[ ]:

light = random.choice(mychoices)


# Selects a random value from mychoices and stores it in a "variable" called light.
# 
# Commands to try (remember to repeat these, randomness means that that they don't do the same thing every time):

# In[ ]:

random.choice(mychoices)


# In[ ]:

random.choice(mychoices).toggle()


### Line 4

# In[ ]:

light.toggle()


# Makes the object held in the variable called light toggle its state (on becomes off and off becomes on).
# 
# Commands to try:

# In[ ]:

light = mychoices[0]


# In[ ]:

light.toggle()


# In[ ]:

light.on()


# In[ ]:

light.off()


# In[ ]:

light = pibrella.light.green


# In[ ]:

light.toggle()


### Line 5

# In[ ]:

time.sleep((random.random() / 2) + 0.1)


# Makes the program do nothing for a short but randomly selected period of time.

# Commands to try (repeat these, random things don't go the same thing every time):

# In[ ]:

random.random()


# In[ ]:

random.random() / 2


# In[ ]:

(random.random() / 2) + 0.1


# In[ ]:

(random.random() / 10) + 0.9


# In[ ]:

time.sleep(5)


## Challenges

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
#        while True:
#            print("Why not try moving the scroll bar?")
# 
# 5. Make four more of the lights on the pibrella join in the blinking.
# 
#    Hint:
# 
#        pibrella.output.e.toggle()
#        pibrella.output.h.toggle()
