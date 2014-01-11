# 120203_Demonstration.py
# In class exercises for Feb 3rd
# Chad Hobbs

from graphics import * # loads the graphics library
import time # loads clock function


win = GraphWin("Friday",600,400) # win is an object, GraphWin() is a class, and a constructor. Args are (name,width,height)

# win.close() or win.draw() .close is a method. If you do not put () on the method, it tells you what you about it.

p = Point(100,100)
circle = Circle(p,50)

circle.draw(win) # draws the object into the named GraphWin

time.sleep(10) # sleeps computer for 10 seconds

circle.move(10,10) # moves the circle object right 10 and up 10







win.getMouse()
win.close()
