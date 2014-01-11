## circle.py
## Draws a circle based on user input.
## Chad Hobbs

from math import *
from graphics import *

def main():
    #Creates a graphical window
    win = GraphWin("Sandbox",400,400)
    width = win.getWidth()
    height = win.getHeight()

    #Initially instruct user
    instPt = Point(width/2, height-10)
    instructions = Text(instPt,"Let's draw a circle: Click center of circle.")
    instructions.draw(win)

    #Get first mouse click
    p = win.getMouse()
    dxa = p.getX()
    dya = p.getY()

    #Erase old, instruct user for radius
    instructions.undraw()
    instructions = Text(instPt,"Click outer edge.")
    instructions.draw(win)

    #Get second mouse click
    p = win.getMouse()
    dxb = p.getX()
    dyb = p.getY()


    #builds a circle
    radius = sqrt(((dxb-dxa) ** 2) + ((dyb-dya) ** 2))
    shape = Circle(Point(dxa, dya), radius)
    shape.setOutline("red")
    shape.setFill("green")
    shape.draw(win)

    #Erase old and display
    instructions.undraw()
    instructions = Text(instPt,"Click again to close.")
    instructions.draw(win)
    win.getMouse()
    win.close()

main()
