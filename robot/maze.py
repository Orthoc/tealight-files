from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

# Add your code here
move()
n = 1
while n > 2000:
  n = n + 1
  if touch() == None:
    move()
  elif left_side == 'wall':
    turn()
  elif right_side == 'wall':
    turn()

