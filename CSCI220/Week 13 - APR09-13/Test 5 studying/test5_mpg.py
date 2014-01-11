# test5_mpg.py
# Test 5 Problem 2
# <Chad Hobbs>

##data = [[12000,15],[15000,30]]

sepped_data = []
userentry = input("What is the beginning odo reading? ")
sepped_data[ = eval(userentry)
i = 1

while True:
    
    print("For leg: ",i)
    userentry = input("What is odo reading and how many gallons used, sep with space? ")
    if userentry == "":
        break
    userentry = userentry.split(" ")
    sepped_data.append(userentry)
    i = i + 1

for j in range(0,i):
    MPG = (sepped_data[j+1,0] - sepped_data[j,0]) / sepped_data[j+1,1]
    print("MPG for leg",j+1,"is:",MPG)
    total_gallons = total_gallons + sepped_data[j+1,1]

total_MPG = (sepped[i,0] - sepped[0,0] ) / total_gallons
print(total_MPG)
    
