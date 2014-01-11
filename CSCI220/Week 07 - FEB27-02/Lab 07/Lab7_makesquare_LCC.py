# Lab7_makesquare_LCC.py
# Doing a square dance with the robot
# Chad Luke and Corey

# This square dance ended in the same exact point as it started

def makeSquare(sides):
    for i in range(4):# how many sides, normally 4
        forward(.8,sides)
        turnLeft(.8,.46)
        
    stop()
#end makeSquare
    
def main():
    sides = input("How long should the sides be(in seconds)?: ")
    makeSquare(sides)
#end main

main()
