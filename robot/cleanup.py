from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

# Add your code here

move()
move()
move()

n=1
while n < 2000:
  n = n + 1
  
  print left_side()
  if touch() == 'fruit':
    move()
  elif right_side() == 'fruit':
    turn(1)
    move()
  elif left_side() == 'fruit':

    turn(-1)
    move()
  elif look() == 'fruit':
    move()
    print right_side()
  else:
    turn(1)
    move()
    move()
