# Bubble Sort

numbers = [2,3,7,5,9,8,1,5,0,4,3,2]
n = len(numbers)

while n > 0:
    for j in range(0,n-1):
        if numbers[j] > numbers[j+1]:
            numbers[j],numbers[j+1] = numbers[j+1],numbers[j]

    n = n - 1

print(numbers)
