from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

# Add your code here

move()
  
if left_side() == 'fruit':
  turn(-1)
  move()
elif right_side() == 'fruit':
  turn(1)
  move()
