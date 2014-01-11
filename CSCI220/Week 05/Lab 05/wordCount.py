# wordCount.py
# A program that counts the number of words in a sentence entered by user.
# <Chad Hobbs>

print("Please type in any sentence you would like a wordcount of!")
sent = input("??:") # gets the sentence

string = sent.split() # Breaks the sentence down into words in a list

print()
print("There are",len(string),"words in that sentence.") # Uses the len function to return the amount of total words
