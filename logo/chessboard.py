print "A new file!"
from tealight.logo import move, turn, color

def polygon(edges, size):
  angle = 360.0 / edges
  for i in range(0, edges):
    move(size)
    turn(angle)
    
polygon(4,100)


move(8)
turn(90)
move(8)
turn(90)
move(8)

n = 1
while n < 8:
  turn(180)
  move(10)
  turn(90)
  move(10)
  turn(90)
  move(10)
  n = n + 1

