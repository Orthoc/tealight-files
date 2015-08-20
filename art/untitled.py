print "A new file!"
from tealight.art import (color, line, spot, circle, box, image, text, background)
from tealight import *



color("black")
box(0,0,1000,1200)

color("white")
box(180,200,546,546)

x = 182
y = 202

for Ycounter in range(0,16):
  for Xcounter in range(0,16):
    color("grey")
    box(x,y,32,32)
    x = x + 34
  y = y + 34
  x = 182

color("black")
spot(231,354,10)

color("white")
spot(227,349,2)

color("black")
line(231,342,231,339)

color("black")
line(231,366,231,369)

color("black")
line(242,354,245,354)

color("black")
line(220,354,217,354)


color("black")
spot(222,345,1)

color("black")
spot(240,345,1)

color("black")
spot(222,364,1)

color("black")
spot(240,364,1)

def DrawMark(x,y):
  color('blue')
  spot(x, y, 10, 10)

def Drawemptysquare(x,y):
  color('white')
  box(x, y, 30, 30)

def handle_mousedown(x,y,button):
  if button == "right":
    DrawMark()
  elif button == "left":
    
    
def DrawBomb(x,y):
  color('red')
  spot(  
    