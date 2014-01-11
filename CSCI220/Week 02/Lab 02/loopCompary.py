# loopCompare.py
#
# Pen and Paper comparative exercise
#
# <Chad Hobbs>

print ("a:")
for i in range(8):
    print (i)

print ("b:")
for i in [1, 3, 9]:
    print (i, end = " ")

print(end="\n")
print ("c:")
for i in range(-1):
    print (i)

print ("d:")
sum = 0
for i in range(5):
    sum = sum + i
print (sum)

print ("e:")
power = 2
for i in [2, 4, 6]:
    print (i ** power)

print ("f:")
difference = 0
for i in [1, 8, -2, 15, 0]:
    difference = difference - i
    print (difference)

print ("g:")
product = 1
for i in range(4):
    product = product * i
print(product)

print ("h:")
product = 1
for i in [1, 3, 5]:
    product = product * i
    print (product)


