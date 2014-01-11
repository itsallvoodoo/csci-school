# Practice exam
# 1 Open a file Test2-3.in and read avg words per line


infile = open("Test2-3.txt","r")


database = []
for line in infile:
     oneline = line.strip().split(' ')
     database.append(oneline)

number_words = 0

for i in range(len(database)):
    number_words = number_words + len(database[i])
    
avg_words = number_words / len(database)

print(avg_words)


    
    
