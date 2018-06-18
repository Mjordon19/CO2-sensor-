# CO2 sensor

import RoboPiLib as RPL
RPL.RoboPiInit("/dev/ttyAMA0",115200)
import post_to_web as PTW
import time


co = 1
print RPL.analogRead(co)
average = [ ]
base = 0
detect = 0
content = 0
x = 0
PTW.state['detect'] = 1

# ^ setup

# begins by averaging the first 1000 readings in order to get a base reading
base = RPL.analogRead(co)

while True:
    content = RPL.analogRead(co)
    if content <= 190 or base - content >= 50:
        x = x + 1
        detect = 2
        PTW.state['detect'] = 2
        if x >= 3: # this indicates breathing
            detect = 3
            PTW.state['detect'] = 3

    else:
        detect = 1
        PTW.state['detect'] = 1
        x = 0

    PTW.post()
