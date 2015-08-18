from tealight.logo import move, turn

def spiral(size):
  
  if size > 350:
    return
  
  move(size)
  turn(90)
  spiral(size + 10)
  
spiral(0)

