# prog3_3.py
# A program that generates acronyms from sentences
# <Chad Hobbs>

print("Welcome to Chad's super duper acronym generator!")
print()
print("Please type in a series of words that you would like to turn into an acronym!")
sent = input("??:") # gets the sentence

string = sent.split() # breaks the sentence down into words in a list
acro = ""
piece = ""

for i in range(len(string)):
    piece = string[i] # assigns the list piece into a string piece
    acro = acro + piece[0] # grabs the first character of the string and adds it to an accumulator
    
print()
print("Your new acronym is {0}!".format(acro.upper())) # prints the results while also capitalizing the acronym
