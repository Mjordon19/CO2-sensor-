# CO2 sensor

import setup
import RoboPiLib as RPL
import post_to_web as PTW
import time


co = 1
print RPL.analogRead(co)
average = [ ]
base = 0
detect = 0
x = 0

# ^ setup

# begins by averaging the first 1000 readings in order to get a base reading
while len(average) < 1000:
    content = RPL.analogRead(co)
    average.append(content)
    if len(average) == 1000:
        base = sum(average) / len(average)
        print base


while True:
    content = RPL.analogRead(co)
    if content - base >= 2: # a difference >= 2 signifies a significant change
        x = x + 1
        if x >= 3:
            print "BEEP BEEP BEEP" # this indicates breathing
            detect = 0
            PTW.state['detect'] = 0
    else:
        print " "
        detect = 1
        PTW.state['detect'] = 1
        x = 0

    PTW.post()
