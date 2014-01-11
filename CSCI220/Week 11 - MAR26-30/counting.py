summed = 0
number = 2
while summed < 30 and number < 7:
    counter = 0
    while counter < 2:
        summed = summed + counter
        counter = counter + 1
    number = number + 2

print(summed, number, counter)
