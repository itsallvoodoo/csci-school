# prog3_2.py
# A program that calculates the average word length of a sentence.
# <Chad Hobbs>

print("Welcome to Chad's super duper average word-length-of-a-sentence analyzer!")
print()
print("Please type in any sentence you would like the average word-length of!")
sent = input("??:") # gets the sentence

string = sent.split() # breaks the sentence down into words in a list
total = 0

for i in range(len(string)):
    total = total + len(string[i]) # totals the lengths of all of the words in the sentence

total = total / len(string) # divides the total by the amount of words
print()
print("For the",len(string),"words in that sentence, the average word length is {0:0.1f}".format(total))
