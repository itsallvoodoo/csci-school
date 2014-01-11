## squares-multi.py
## Moves a square based on user clicks
## Chad Hobbs

from graphics import *

def main():
    #Creates a graphical window
    win = GraphWin()
    width = win.getWidth()
    height = win.getHeight()

    #number of times user can move circle
    numClicks = 5

    #create a space to instruct user
    instPt = Point(width/2, height-10)
    instructions = Text(instPt,"Click to move rectangle")
    instructions.draw(win)

    #builds a square
    shape = Rectangle(Point(50, 50), Point(70,70))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    #allows the user to click multiple times to move the
    #rectangle
    for i in range(numClicks):
        p = win.getMouse()
        c = shape.getCenter() #center of rectangle

        #move amount is distance from center of rectangle to the
        #point where the user clicked
        dx = p.getX()
        dy = p.getY()
        shape = Rectangle(Point(dx+10, dy+10), Point(dx-10,dy-10))
        shape.setOutline("red")
        shape.setFill("red")
        shape.draw(win)

    instructions.setText("Click again to close")
    win.getMouse()
    win.close()

main()
