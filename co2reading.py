# CO2 sensor

import setup
import RoboPiLib as RPL
import time

co = 1
print RPL.analogRead(co)

while len(average) <= 100:
    content = RPL.analogRead(co)
    average.append(content)
    if len(average) == 100:
        base = sum(average) / len(average)
        print base


while True:
    content = RPL.analogRead(co)
    if content - base > 3:
        print "BEEP BEEP BEEP"
