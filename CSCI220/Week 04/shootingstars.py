# shootingStars.py
# Creates a house with a night sky and shooting stars
# <Chad Hobbs>

from graphics import *
import random, math

# Global Variables


#create main window
win = GraphWin("Shooting Stars",600,400)
win.setCoords(0,0,30,20)
win.setBackground("white")


def build(): # Construct the house and all of it's components

    #create house
    house_color = color_rgb(255,255,210)
    house = Rectangle(Point(10,1), Point(20,8))
    house.setOutline(house_color)
    house.setFill(house_color)
    house.draw(win)
    gable = Polygon(Point(10,8),Point(15,10),Point(20,8),Point(10,8))
    gable.setOutline(house_color)
    gable.setFill(house_color)
    gable.draw(win)
    for i in range(1,8):
        siding = Line(Point(10,i+.3),Point(20,i+.3))
        siding.setOutline("black")
        siding.draw(win)

    #create roof
    roof_color = color_rgb(110,50,20)
    roof1 = Line(Point(9.5,8),Point(15.08,10.1))
    roof2 = Line(Point(14.92,10.1),Point(20.5,8))
    roof1.setWidth(10)
    roof2.setWidth(10)
    roof1.setOutline(roof_color)
    roof2.setOutline(roof_color)
    roof1.draw(win)
    roof2.draw(win)

    #create door
    door_color = color_rgb(180,0,0)
    door = Rectangle(Point(13.5,1), Point(16.5,6))
    door.setOutline("black")
    door.setFill(door_color)
    door.draw(win)
    handle = Circle(Point(14,3.3),.25)
    handle.setOutline("black")
    handle.setFill("black")
    handle.draw(win)

    #create windows
    window1 = Rectangle(Point(10.75,3.5), Point(12.75,5.5))
    window1.setOutline("black")
    window1.setFill("yellow1")
    window1.draw(win)
    window2 = window1.clone()
    window2.move(6.5,0)
    window2.draw(win)
    bar1 = Rectangle(Point(10.75,4.4), Point(12.75,4.6))
    bar1.setOutline("black")
    bar1.setFill(house_color)
    bar1.draw(win)
    bar2 = bar1.clone()
    bar2.move(6.5,0)
    bar2.draw(win)
    bar3 = Rectangle(Point(11.65,3.5), Point(11.85,5.5))
    bar3.setOutline("black")
    bar3.setFill(house_color)
    bar3.draw(win)
    bar4 = bar3.clone()
    bar4.move(6.5,0)
    bar4.draw(win)

def night():

    for i in range(100):
        dx = random.randrange(0,29) + random.random()
        dy = random.randrange(2,19) + random.random()
        size = random.random()
        size = size / 10
        circle = Circle(Point(dx,dy),size)
        circle.setOutline(color_rgb(255,255,80))
        circle.setFill(color_rgb(255,255,80))
        circle.draw(win)


def movestar(x,y): # Draw a star on the screen and it's associated movement

    if (x == -1):     # do this if not based on user input
        dx = random.randint(0,10)
        dy = random.randint(12,15)
    else:   # do this if clicking start point
        dx = x
        dy = y

    # draw star
    star1 = Polygon(Point(dx-.75,dy-.25),Point(dx,dy+.75),Point(dx+.75,dy-.25))
    star2 = Polygon(Point(dx-.75,dy+.32),Point(dx,dy-.68),Point(dx+.75,dy+.32))
    star1.setOutline("yellow")
    star1.setFill("yellow")   
    star1.draw(win)
    star2.setOutline("yellow")
    star2.setFill("yellow")   
    star2.draw(win)
    factor = 0.01
    
    while (dx < 30): # create parabolic path for star to travel
        dxa = dx
        dya = dy
        dy = (8*math.sin(.08 * dx))
        dx = dx + 0.007
        dya = (8*math.sin(.08 * dx)) - dy
        star1.move((dx-dxa),(dya))
        star2.move((dx-dxa),(dya))
     
    star1.undraw()
    star2.undraw()

def main(): # Main program loop
    
    #create grass
    grass_color = color_rgb(0,120,0)
    grass = Rectangle(Point(0,0), Point(30,1.1))
    grass.setOutline(grass_color)
    grass.setFill(grass_color)
    grass.draw(win)

    #create sky
    sky_color = color_rgb(0,0,50)
    sky = Rectangle(Point(0,1.1), Point(30,20))
    sky.setOutline(sky_color)
    sky.setFill(sky_color)
    sky.draw(win)

    night()
    
    build() #initial house construction

    txt = Text(Point(15,.5),"April Showers bring meteor showers! Click mouse to start.") # wait for user input
    txt.draw(win)
    win.getMouse()
    txt.undraw()
    
    for i in range(5): # initial loop of 5 stars
        x = -1
        y = -1
        movestar(x,y)

    Text(Point(15,.5),"Click the screen to shoot a star! Click the grass to exit.").draw(win)  
    loop = 0
    while (loop == 0): # secondary loop for user based shooting stars
        p = win.checkMouse()
        if p != None:
            x = p.getX()
            y = p.getY()
            if (y < 1.1):
                loop = 1
            else:
                movestar(x,y)

    win.close() # exit the program

main()

