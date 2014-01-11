from graphics import *

win = GraphWin("",300,400)
rect = Rectangle(Point(50,30),Point(150,200))
rect.draw(win)
print("Hit any key to close window")
x = win.getMouse()
win.close()
