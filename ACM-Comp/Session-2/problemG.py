vowels = ['a', 'i', 'y', 'e', 'o', 'u'] 
capVowels = ['A', 'I', 'Y', 'E', 'O', 'U']
conts = ['b','k','x','z','n','h','d','c','w','g','p','v','j','q','t','s','r','l','m','f'] 
capConts = ['B','K','X','Z','N','H','D','C','W','G','P','V','J','Q','T','S','R','L','M','F'] 
answers = []
while True:
	outstr = ''
	try:
		instr = raw_input()
	except:
		break
	for char in instr:
		if char in conts:
			outstr += conts[conts.index(char)-10]
		elif char in vowels:
			outstr += vowels[vowels.index(char)-3]
		elif char in capVowels:
			outstr += capVowels[capVowels.index(char)-3]
		elif char in capConts:
			outstr += capConts[capConts.index(char)-10]
		else:
			outstr += char 
	print outstr
