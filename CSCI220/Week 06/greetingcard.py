# greetingcard.py
# Lecture program
# <Chad Hobbs>

from graphics import*
from time import sleep
import random

win = GraphWin("Season Greetings", 400, 400)

win.setCoords(0, 0, 200, 200)

#Sky
sky = Rectangle(Point(0, 50), Point(200, 200))
sky.setFill(color_rgb(0, 10, 60))
sky.draw(win)

#Roof of House
roof= Polygon(Point(80, 120),Point(110, 110),Point(50, 110))
roof.setFill(color_rgb(30, 20, 30))
roof.draw(win)


#House
house = Rectangle(Point(110, 110), Point(50, 50))
house.setFill(color_rgb(65, 75, 85))
house.draw(win)
window = Rectangle(Point(100, 90), Point(80, 70))
window.setFill('lightblue')
window.draw(win)
window1 = Line(Point(90, 90), Point(90, 70))
window1.draw(win)
window2 = Line(Point(100, 80), Point(80, 80))
window2.draw(win)
door = Rectangle(Point(70, 70), Point(60, 50))
door.setFill('red')
door.draw(win)
doorknob = Circle(Point(62.25, 60), 1)
doorknob.setFill('yellow')
doorknob.draw(win)

#Garage
garage = Rectangle(Point(150, 80), Point(110, 50))
garage.setFill(color_rgb(65, 75, 85))
garage.draw(win)
garageroof = Polygon(Point(130, 90), Point(150, 80), Point(110, 80))
garageroof.setFill(color_rgb(30, 20, 30))
garageroof.draw(win)
groof1 = Line(Point(130, 90), Point(150, 80))
groof1.draw(win)
groof2 = Line(Point(150, 80), Point(110, 80))
groof2.draw(win)
groof3 = Line(Point(110, 80), Point(130, 90))
groof3.draw(win)
gdoor = Rectangle(Point(140, 70), Point(120, 50))
gdoor.setFill(color_rgb(30, 20, 30))
gdoor.draw(win)
gwindow = Rectangle(Point(125.5, 70.25), Point(137.5, 77.5))
gwindow.setFill('lightblue')
gwindow.draw(win)

#Ground
ground = Rectangle(Point(0, 0), Point(200, 50))
ground.setFill('green')
ground.draw(win)


COLOR_TREE = color_rgb(120, 160, 56)


#Tree
top = Polygon(Point(20,100), Point(25, 90), Point(15, 90))
top.setFill(COLOR_TREE)
top.draw(win)
middle = Polygon(Point(20, 90), Point(30, 80), Point(10, 80))
middle.setFill(COLOR_TREE)
middle.draw(win)
bottom = Polygon(Point(20, 80), Point(35, 60), Point(5, 60))
bottom.setFill(COLOR_TREE)
bottom.draw(win)

trunk = Rectangle(Point(17.5, 50), Point(22.5, 60))
trunk.setFill('brown')
trunk.draw(win)

#Moon
sun = Circle(Point(50, 170), 15)
sun.setFill('lightyellow')
sun.draw(win)



instructions = Text(Point(110, 140), "Click anywhere 10 times to make it snow!")
instructions.setFill('red')
instructions.setSize(7)
instructions.draw(win)

win.getMouse()
instructions.undraw()

#Snowflake
numClicks = 10
snowflake = Circle(Point(130, 170), 1.75)
snowflake.setFill('white')
snowflake.draw(win)
####newflakes = []
for i in range(numClicks):
    p = win.getMouse()
    c = snowflake.getCenter()

    dx = p.getX() - c.getX()
    dy = p.getY() - c.getY()

    newsnow = snowflake.clone()
    newsnow.move(dx, dy)
    newsnow.draw(win)

#Fading Stuff
instructions.setText("click again to see what happenes next!")
instructions.draw(win)
win.getMouse()
instructions.undraw()

ground.setFill('white')

#Light
light1 = Circle(Point(11, 65), 2)
light1.setFill('red')
light1.draw(win)
light2 = Circle(Point(25, 65), 2)
light2.setFill('yellow')
light2.draw(win)
light3 = Circle(Point(20, 70), 2)
light3.setFill('green')
light3.draw(win)
light4 = Circle(Point(15, 84), 2)
light4.setFill('yellow')
light4.draw(win)
light5 = Circle(Point(24, 82), 2)
light5.setFill('green')
light5.draw(win)
light6 = Circle(Point(20, 93), 2)
light6.setFill('red')
light6.draw(win)

lights = []
lights.append(light1)
lights.append(light2)
lights.append(light3)
lights.append(light4)
lights.append(light5)
lights.append(light6)

#Snowman

snowman = []
head = Circle(Point(175, 72), 2)
snowman.append(head)
middle = Circle(Point(175, 65), 4)
snowman.append(middle)
last = Circle(Point(175, 55), 6)
snowman.append(last)
for snow in snowman:
    snow.setFill('white')
    snow.draw(win)

#W

ww = Circle(Point(65, 82), 8)
ww.setFill('green')
ww.draw(win)
w = Circle(Point(65, 82), 4)
w.setFill(color_rgb(65, 75, 85))
w.draw(win)
lw = Circle(Point(65, 88), 1.5)
lw.setFill('red')
lw.draw(win)
lw2 = Circle(Point(65, 77), 1.5)
lw2.setFill('red')
lw2.draw(win)
lw3 = Circle(Point(60, 81), 1.5)
lw3.setFill('red')
lw3.draw(win)
lw4 = Circle(Point(71, 82), 1.5)
lw4.setFill('red')
lw4.draw(win)

message= Text(Point(90,30), "Season Greetings!")
message.setFill('red')
message.draw(win)

newflakes = []
numClicks = 825
colors = ['yellow', 'green', 'red', 'blue', 'orange']
for i in range(numClicks):
    px = int(win.width * random.random())
    py = int(win.height * random.random())
    p = Point(px, py)
    newflake = Circle(p, 1.75)
    newflake.setFill('white')
    newflake.draw(win)
    newflakes.append(newflake)

for i in range(win.height):
    for flake in newflakes:
        flake.move(0, -random.random())
    for light in lights:
        coli = int(random.random() * len(colors))
        light.setFill(colors[coli])

    sleep(0.025)
        

instructions.setText("click again to close!")
mag = message.getAnchor()
iga = instructions.getAnchor()
instructions.move(mag.getX() - iga.getX() + 20, mag.getY() - iga.getY() - 6)
instructions.draw(win)
win.getMouse()
win.close()
