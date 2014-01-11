# 120208_Demonstration.py
# In class exercises for Feb 8th
# Chad Hobbs

from graphics import *
import random, time


# -----------printing with lists---------------

##n = eval(input("n: "))
##
##win = GraphWin("Example",300,300)
##
##ball_list = []
##for i in range(n):
##    x = random.randint(0,299)
##    y = random.randint(0,299)
##    circle = Circle(Point(x,y),10)
##    circle.draw(win)
##    ball_list.append(circle)
##
#### time.sleep(1)
##
##
##for j in range(1000):
##
##    # for i in range(n):
##    for ball in ball_list:
##        dx = random.randint(-10,10)
##        dy = random.randint(-10,10)
##        #    ball_list[i].move(dx,dy)
##        ball.move(dx,dy)


## --------------commands with lists-------------------------
num_list = []
for i in range(10):
    num_list.append(random.randint(0,10))
    print(num_list)

print("Directly")
for num in num_list:
    print(num)

print("Using index:")
for i in range(len(num_list)):
    print(num_list[i])


# num_list.remove(10) removes the first number 10 from the list, if it exists

# num_list.insert(3,"Paul") will insert Paul after the first 3 is found

board = [['0','',''],['','X',''],['X','','']]
location = [[[15,75],[45,75],[75,75]],[[15,45],[45,45],[75,45]],[[15,15],[45,15],[75,15]]]

win = GraphWin('Tic-Tac-Toe',400,400)
win.setCoords(0,0,90,90)

Line(Point(30,0),Point(30,90)).draw(win)
Line(Point(60,0),Point(60,90)).draw(win)
Line(Point(0,30),Point(90,30)).draw(win)
Line(Point(0,60),Point(90,60)).draw(win)

for i in range(len(board)): # Each rox
    for j in range(len(board[i])):
        x = location[i][j][0]
        y = location[i][j][1]
        text = Text(Point(x,y),board[i][j])
        text.draw(win)






win.getMouse()
win.close()
