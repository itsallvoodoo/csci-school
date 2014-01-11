# 120206_Demonstration.py
# In class exercises for Feb 6th
# Chad Hobbs

# ------------- Slicing Strings -------------------

# name = "Chad Hobbs" # this is a string

# print(name[0]) # putting brackets and a valid number gets a piece of the string out

# print(name[1]) # the string slice starts at 0 and goes up to the total characters minus 1

# print(name[0:4]) # using a colon reports a section of the string, the ending needs to be the total characters of the string

# print(len(name)) # len reports the length of the string

# print(name[0:11]) # this is a full slice of the string

# print(name[2:11]) # the slice can start anywhere that is less than the end length


# ------------- Working with Lists ------------------

##name = input("Name (First Last): ")
##result = name.split(" ")
##print(result[1],result[0],sep=",")
##
##
##
##
##index = name.find(" ")
##first_name = name[0:index]
##last_name = name[index+1:] # or end the brackets with len(name) or leave blank
##print(last_name,first_name,sep=",")


# --------------- Capitalizing parts of strings -----------------------

name = input("Enter your name: ")
new_name = [] # empty list

for ch in name:
    new_name.append(ch)


new_name[0] = chr(ord(new_name[0]) - 32) # ord grabs the ordinal number of a character, chr returns the character based on ordinal number

print("".join(new_name))
