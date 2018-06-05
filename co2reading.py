# CO2 sensor

import setup
import RoboPiLib as RPL
import time

co = 1
print RPL.analogRead(co)
average = [ ]
base = 0

while len(average) < 1000:
    content = RPL.analogRead(co)
    average.append(content)
    if len(average) == 1000w:
        base = sum(average) / len(average)
        print base


while True:
    content = RPL.analogRead(co)
    if content - base >= 2:
        print "BEEP BEEP BEEP"
