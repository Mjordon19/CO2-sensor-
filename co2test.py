import setup
import RoboPiLib as RPL

while True:
  print RPL.analogRead(1)

#    elif content - base <= -3:
#        x = 0
#        y = y + 1
#        if y >= 3:
#            average = [ ]
#            while len(average) < 1000:
#                content = RPL.analogRead(co)
#                average.append(content)
#                if len(average) == 1000:
#                    base = sum(average) / len(average)
#                    print "NEW BASE"
#                    print base
