# CO2 sensor

import setup
import RoboPiLib as RPL
import time

co = 1
original = co

while True:
    content = RPL.analogRead(co)
    if content - original > 5:
        print "BEEP BEEP BEEP"
