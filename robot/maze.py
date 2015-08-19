from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

# Add your code here

n = 1
while n < 2000:
  n = n + 1
  if touch() == None:
    move()
    print left_side()
  elif left_side() == 'wall':
    turn(1)
    move()
  elif right_side() == 'wall':
    turn(-1)
    move()
    print left_side()
  elif touch() == 'wall':
    turn(1)

