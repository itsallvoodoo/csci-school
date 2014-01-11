# 120313_Demonstration.py
# In class lecture
# <Chad Hobbs>

infile = open("db.txt","r") # relative path to our database file

##  lines = infile.readlines() # gets everything in file and puts it in a string

## for h in range(len(lines)):
##     lines[h] = lines[h].strip()


users = []
passwords = []
first_line = infile.readline()

for line in infile:
    if line != '':
        user_password = line.strip().split(',') # separates by ,
        if len(user_password) == 2:
            users.append(user_password[0])
            passwords.append(user_password[1])

print(first_line)    
print(users)
print(passwords)
               
