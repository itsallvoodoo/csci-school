# target.py
# Draws an archery target
# Chad Hobbs and Luke Duvall
 
from graphics import *

win = GraphWin("Archery Target",600,600)
win.setCoords(0,0,600,600)


num = Entry(Point(300,10),5)
num.setText("0.0")
num.draw(win)
txt = Text(Point(300,30),"Enter the desired radius between 1-55, then click mouse.")
txt.draw(win)

win.getMouse()

txt.undraw()
num.undraw()

radius = eval(num.getText())
circle = Circle(Point(300,300),radius*5)
circle.setFill("white")
circle.setOutline("black")
circle.draw(win)
circle = Circle(Point(300,300),radius*4)
circle.setFill("black")
circle.setOutline("black")
circle.draw(win)
circle = Circle(Point(300,300),radius*3)
circle.setFill("blue")
circle.setOutline("blue")
circle.draw(win)
circle = Circle(Point(300,300),radius*2)
circle.setFill("red")
circle.setOutline("red")
circle.draw(win)
circle = Circle(Point(300,300),radius)
circle.setFill("yellow")
circle.setOutline("yellow")
circle.draw(win)

txt = Text(Point(300,30),"Click again to close.")
txt.draw(win)


win.getMouse()
win.close()

    
    
    











