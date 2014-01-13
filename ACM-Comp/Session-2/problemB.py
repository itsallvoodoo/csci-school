answers = []

while True: 
	try:
		instr = raw_input()
		if instr == None or len(instr) == 0:
			break
	except:
		break
	a = int(instr)
	digits = ['0','1','2','3','4','5','6','7','8','9']
	k = 1 
	while not len(digits) == 0:
		b = str(a*k)
		for char in b:
			if char in digits:
				digits.remove(char)
		if len(digits) == 0:
			break
		k += 1
	answers.append(k)
for answer in answers:
	print answer
