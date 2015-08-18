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
  
  #print left_side()
  if left_side() == 'fruit':

    turn(-1)
    move()
  elif right_side() == 'fruit':
    turn(1)
    move()
