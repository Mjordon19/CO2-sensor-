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
y = 0

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
        y = 0
        print content
        x = x + 1
        detect = 2
        PTW.state['detect'] = 2
        if x >= 3: # this indicates breathing
            print "!!!!"
            detect = 3
            PTW.state['detect'] = 3
    elif content - base <= -3:
        x = 0
        y = y + 1
        if y >= 3:
            average = [ ]
            while len(average) < 1000:
                content = RPL.analogRead(co)
                average.append(content)
                if len(average) == 1000:
                    base = sum(average) / len(average)
                    print "NEW BASE"
                    print base
    else:
        detect = 1
        PTW.state['detect'] = 1
        x = 0
        y = 0

    PTW.post()
