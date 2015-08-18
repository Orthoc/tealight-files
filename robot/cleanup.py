from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

# Add your code here

move()

n=1
while n < 2000:
  if left_side() == 'fruit':
    print left_side()
    turn(-1)
    move()
  elif right_side() == 'fruit':
    turn(1)
    move()
