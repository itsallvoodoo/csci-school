# smiley.py
# This program will draw smiley or grim faces
# <Chad Hobbs>

#Global Commands
from graphics import *

def makewin(): # Creates the window
    win = GraphWin("Smiley Faces",600,600)
    win.setCoords(0,0,30,30)
    return win
    

def drawFace(center,size,win): # Draws a face in the main window
    face = Circle(center,size)
    face.setFill("yellow")
    face.setOutline("black")
    face.draw(win)
    x = center.getX()
    y = center.getY()
    eye1 = Circle(Point(x - (size / 3),y + (size / 3)),(size / 6))
    eye1.setFill("black")
    eye1.setOutline("black")
    eye1.draw(win)
    eye2 = Circle(Point(x + (size / 3),y + (size / 3)),(size / 6))
    eye2.setFill("black")
    eye2.setOutline("black")
    eye2.draw(win)
    mouth = Line(Point(x - (size / 3),y - (size / 3)),Point(x + (size / 3),y - (size / 3)))
    mouth.setOutline("black")
    mouth.draw(win)
                  

def main(): # Main program
    n = eval(input("How many faces would you like to draw?: "))
    win = makewin()

    for r in range(n):
        print("Inputs for face",r+1)
        print("-" * 18)
        
        cx,cy = eval(input("Please enter the centerpoints x and y, separated by commas, between 5 and 25 (ie: 13,24): "))
        center = Point(cx,cy)
        size = eval(input("Please enter the radius of the face between 1 and 5: "))
        drawFace(center,size,win)
        print()

    win.getMouse()
    win.close()

main()
