cases = int(raw_input())

for i in range (cases):
    goodTotal = 0
    badTotal = 0
    
    good = raw_input()
    bad = raw_input()

    goodString = good.split(" ")
    badString = bad.split(" ")

    goodTotal = int(goodString[0])*1 + int(goodString[1])*2 + int(goodString[2])*3 + int(goodString[3])*3 + int(goodString[4])*4 + int(goodString[5])*10
    badTotal = int(badString[0])*1 + int(badString[1])*2 + int(badString[2])*2 + int(badString[3])*2 + int(badString[4])*3 + int(badString[5])*5 + int(badString[6])*10

    if(goodTotal < badTotal):
        print("Battle " + str(i + 1) + ": Evil eradicates all trace of Good")
 
    elif(badTotal < goodTotal):
        print("Battle " + str(i + 1) + ": Good triumphs over Evil")
            
    else:
        print("Battle " + str(i + 1) + ": No victor on this battle field")
    
