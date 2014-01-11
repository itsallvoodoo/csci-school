# prog6_11.py
# This program bounces a ball around the screen and other fun stuff
# <Chad Hobbs>

from graphics import *
from time import sleep
from random import *
from math import *


def getstart(win): #gets the initial click so the ball knows where to start
    txt = "Please click anywhere inside the box to start the ball at that point"
    box = Text(Point(400,300),txt)
    box.draw(win)
    p = win.getMouse()
    x = p.getX()
    y = p.getY()
    box.undraw()
    return x,y


def main(): # Main program
    win = GraphWin("Interactive Bouncing Ball",800,600)
    win.setCoords(0,0,800,600)

    x,y = getstart(win)

    r = 100
    g = 100
    b = 100
    ball = Circle(Point(x,y),10)
    ball.setFill(color_rgb(r,g,b))
    ball.setOutline(color_rgb(r,g,b))
    ball.draw(win)
    
    dx = -1
    dy = -1

    txt = "Clicking on the ball changes it's direction!!"
    box = Text(Point(400,590),txt)
    
    for i in range(5000):
       
        # This area changes where the ball is going depending on boundaries
        center = ball.getCenter()
        x = center.getX()
        y = center.getY()
        if x > 795:
            dx = -1
        if x < 5:
            dx = 1
        if y > 595:
            dy = -1
        if y < 5:
            dy = 1

        # This area changes the direction of the ball based on clicks
        click = win.checkMouse()
        if click != None:
            clx = click.getX()
            cly = click.getY()
            if (abs(clx - x)) < 5 or (abs(cly - y)) < 5:
                chgx = randrange(0,9)
                chgy = randrange(0,9)
                if chgx > 5:
                    dx = -1
                else:
                    dx = 1
                if chgy > 5:
                    dy = -1
                else:
                    dy = 1
        

        # This area changes the color of the ball randomly
        chance = randrange(1,100)
        if chance == 6:
            r = randrange(0,256)
            g = randrange(0,256)
            b = randrange(0,256)
            ball.setFill(color_rgb(r,g,b))
            ball.setOutline(color_rgb(r,g,b))

        # Actual ball movement and pause  
        ball.move(dx,dy)
        sleep(0.008)

    win.close()




            



main()
