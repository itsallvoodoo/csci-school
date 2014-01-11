## Linear Search

##find = 4
##
##numbers = [6,4,3,2,8,7,9]
##
##for i in range(len(numbers)):
##    if find == numbers[i]:
##        index = i
##
##print(numbers[index])
##print(index)

## Binary Search

numbers = [1,2,3,4,5,6,7,8,9]
find = 9
imin = 0
imid = int(len(numbers) / 2)
imax = len(numbers)-1

while True:
    if find < numbers[imid]:
        imax = imid
        imid = int(imin + (imax-imin) / 2)
    if find > numbers[imid]:
        imin = imid
        imid = int(imid + (imax - imin)/2)
    if find == numbers[imid]:
        break

print(imid)
        


