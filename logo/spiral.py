from tealight.logo import move, turn

def spiral(size):
  
  if size > 300:
    return
  
  move(size)
  turn(90)
  spiral(size + 10)
  
spiral(0)

def spiral2(size):
  if size > 300:
    return
  
  move (size)
  turn (90)
  spiral(size + 0)

spiral (1)