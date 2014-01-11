# sphereFunctions.py
# This program will call functions that will return area and volume of spheres
# <Chad Hobbs>

import math

def sphereArea(radius): # Function that calculates area radius
    area = 4 * math.pi * radius ** 2
    return area

def sphereVolume(radius): # Function that calculates volume given radius
    volume = (4/3) * math.pi * radius ** 3
    return volume

def main(): # Main program
    rad = eval(input("Please enter the radius of the sphere: "))
    a = sphereArea(rad)
    v = sphereVolume(rad)
    print("The area of the sphere is {0:.2f} and the volume is {1:.2f}".format(a,v))

main()

    
