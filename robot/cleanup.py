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
  n = n + 1
  
  print left_side()
  if left_side() == 'fruit':

    turn(-1)
    move()
    print right_side()
  elif right_side() == 'fruit':
    turn(1)
    move()
  else:
    turn(2)
    move()
