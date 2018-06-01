# CO2 sensor

import setup
import RoboPiLib as RPL
import time

co = 1
original = RPL.analogRead(co)
print original

while True:
    content = RPL.analogRead(co)
    print content
    if content - original > 3:
        print "BEEP BEEP BEEP"
