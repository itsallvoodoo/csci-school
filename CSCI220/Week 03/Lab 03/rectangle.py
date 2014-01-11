## rectangle.py
## Draws a rectangle based on user input.
## Chad Hobbs

from math import *
from graphics import *

def main():
    #Creates a graphical window
    win = GraphWin("Sandbox",600,600)
    width = win.getWidth()
    height = win.getHeight()

    #Initially instruct user
    instPt = Point(width/2, height-10)
    instructions = Text(instPt,"Create a box: Click first point.")
    instructions.draw(win)

    #Get first mouse click
    p = win.getMouse()
    dxa = p.getX()
    dya = p.getY()

    #Erase old, instruct user for new location
    instructions.undraw()
    instPt = Point(width/2, height-10)
    instructions = Text(instPt,"Click second point of box")
    instructions.draw(win)

    #Get second mouse click
    p = win.getMouse()
    dxb = p.getX()
    dyb = p.getY()


    #builds a rectangle
    shape = Rectangle(Point(dxa, dya), Point(dxb,dyb))
    shape.setOutline("blue")
    shape.setFill("grey")
    shape.draw(win)

    #Erase old, calculate dimensions and display
    area = (sqrt(((dxb - dxa) * (dyb - dya)) ** 2))
    perim = 2 * (sqrt((dxb - dxa) ** 2) + sqrt((dyb - dya) ** 2))
    instructions.undraw()
    instPta = Point(width/2, height-50)
    instPtb = Point(width/2, height-30)
    instPtc = Point(width/2, height-10)
    instructionsa = Text(instPta,"The area is " + str(area))
    instructionsb = Text(instPtb,"The perimeter is " + str(perim))
    instructionsc = Text(instPtc,"Click again to close")
    instructionsa.draw(win)
    instructionsb.draw(win)
    instructionsc.draw(win)
    win.getMouse()
    win.close()

main()
