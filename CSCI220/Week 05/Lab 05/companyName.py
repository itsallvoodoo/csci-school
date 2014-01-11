# companyName.py
# This program will pull out a company name from a web address
# <Chad Hobbs>

name = input("Please enter the domain name (www.): ")

comp = name.split(".")

if len(comp) < 3:
    print("That was not a valid web address.")
else:
    print("The web company's name is",comp[1])

