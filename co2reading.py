# CO2 sensor
# its lit

import setup
import RoboPiLib as RPL
import time

co = 1

while True:
    print RPL.analogRead(co)
    
