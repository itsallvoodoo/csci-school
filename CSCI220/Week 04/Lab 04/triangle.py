## triangle.py
## Draw triangle using user mouse clicks and print the
## perimeter and area of the triangle
## Luke Duvall and Chad Hobbs

from graphics import *
from math import *

win = GraphWin("Triangle",400,400)
win.setCoords(0,0,400,400)

points = [[0,0],[0,0],[0,0]]

txt1 = Text(Point(200,390),"Draw a triangle by clicking 3 points in the window")
txt1.draw(win)

for i in range(3):
    txt2 = Text(Point(200,10),"Click on point "+str(i+1))
    txt2.draw(win)
    p = win.getMouse()
    points[i][0] = p.getX()
    points[i][1] = p.getY()
    txt2.undraw()

triangle = Polygon(Point(points[0][0],points[0][1]),Point(points[1][0],points[1][1]),Point(points[2][0],points[2][1]))
triangle.draw(win)

l1 = sqrt((points[1][0]-points[0][0])**2 + (points[1][1]-points[0][1])**2)
l2 = sqrt((points[2][0]-points[1][0])**2 + (points[2][1]-points[1][1])**2)
l3 = sqrt((points[0][0]-points[2][0])**2 + (points[0][1]-points[2][1])**2)

perimeter = l1+l2+l3

s = (l1+l2+l3)/2
area = sqrt(s*(s-l1)*(s-l2)*(s-l3))

txt3 = Text(Point(200,10),"The Perimeter is "+str(int(perimeter))+" and the Area is "+str(int(area))+" Click to Exit")
txt3.draw(win)

win.getMouse()
win.close()
