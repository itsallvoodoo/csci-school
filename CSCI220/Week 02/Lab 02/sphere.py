# sphere.py
#
# A program that calculates the volume and surface area of a sphere from radius
#
# <Chad Hobbs>

import math
print("Let's calculate the volume and surface area of a sphere!")
print()

p = math.pi
radius = eval(input("What is the radius of the sphere?: "))
print()

v = (4/3) * p * radius ** 3
a = 4 * p * radius ** 2

print("The volume is ","{0:0.2f}".format(v)," and the area is ","{0:0.2f}".format(a),", truncated to 2 significant digits.",sep="")
