tower = [0,0,0,0,0,0]

while True:

	try:
		inputStr = raw_input()
	except:
		break

        inputSet = inputStr.split(" ")
        for i in range(6):
                tower[i] = int(inputSet[i])

        

        
