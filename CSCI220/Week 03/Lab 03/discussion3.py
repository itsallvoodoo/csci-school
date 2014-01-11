## Discussion #3, Graphics chapter of Zelle text
## Moves a circle based on user clicks
## Comments added: RHS

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
    instructions = Text(instPt,"Click to move circle")
    instructions.draw(win)

    #builds a circle
    shape = Circle(Point(50, 50), 20)
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    #allows the user to click multiple times to move the
    #circle
    for i in range(numClicks):
        p = win.getMouse()
        c = shape.getCenter() #center of circle

        #move amount is distance from center of circle to the
        #point where the user clicked
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        shape.move(dx, dy)

    instructions.setText("Click again to close")
    win.getMouse()
    win.close()

main()
