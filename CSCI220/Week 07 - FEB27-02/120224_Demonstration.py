## Problem 2

##from graphics import *
##from math import *
##
##
##
##
##def main():
##
##    clicks = eval(input("How many clicks?"))
##    win = GraphWin("CSCI",400,200)
##    point1 = win.getMouse()
##    point1.draw(win)
##    for r in range(1,clicks):
##        point2 = win.getMouse()
##        line1 = Line(point1,point2)
##        line1.draw(win)
##        point1 = point2
##
##    win.getMouse()
##    win.close()
##    
##main()

# Prob 3

##n = eval(input("How many legs?: "))
##odo = eval(input("Original odo?" ))
##mileage = []
##gas = []
##
##for i in range(1,n+1):
##    miles = eval(input("New odo reading? :"))
##    used = eval(input("Gas used?: "))
##    mileage.append(miles)
##    gas.append(used)
##
##prev = odo
##total = 0
##
##for j in range(n):
##    mpg = ((mileage[j] - prev) / gas[j])
##    total = total + gas[j]
##    print("Leg",j+1,"MPG is:",mpg)
##    prev = mileage[j]
##
##totalmpg = ((mileage[n-1] - odo) / total)
##print("Total gas",totalmpg)

# Prob 4
##
##name = input("Please enter your full name")
##splitted = name.split(" ")
##
##address = splitted[0][0] + splitted[1][0] + splitted[2][0:7] + "@edisto.cofc.edu"
##address2 = address.lower()
##
##print(address2)

print("[{0:^15}]".format("14"))
