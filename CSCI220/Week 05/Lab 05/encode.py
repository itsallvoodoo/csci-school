# encode.py
# A program that will encode words using a simple cypher
# <Chad Hobbs>

word = input("Enter a lowercase word that you would like to encode: ")
word = word.lower()
num = eval(input("Enter a cypher key (1 to 9): "))

letters = []

for i in range(len(word)):
    letters.append(word[i])
    
display = ""

for i in range(len(word)):
    letter = ord(letters[i])
    letters[i] = chr(letter + num)
    display = display + letters[i]

print("Your encoded word is",display)


