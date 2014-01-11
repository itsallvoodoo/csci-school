# Lab7_squareView_LCC.py
# This program takes pictures while travelling in a square
# Chad Luke and Corey

def makeSquare(sides):
    pic0 = takePicture()
    show(pic0)
    forward(.8,sides)
    turnLeft(.8,.46)
    pic1 = takePicture()
    show(pic1)
    forward(.8,sides)
    turnLeft(.8,.46)
    pic2 = takePicture()
    show(pic2)
    forward(.8,sides)
    turnLeft(.8,.46)
    pic3 = takePicture()
    show(pic3)
    forward(.8,sides)
    turnLeft(.8,.46)
    pic4 = takePicture()
    show(pic4)
    stop()
#end makeSquare

def main():
    sides = input("How long should the sides be(in seconds)?: ")
    makeSquare(sides)

#end main

main()
