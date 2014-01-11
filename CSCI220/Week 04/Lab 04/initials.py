## initials.py
## Ask how many students are in class and thier names
## Print the students initials
## Luke Duvall and Chad Hobbs

students = eval(input("How many students are in the class: "))
for i in range(1, students+1):
    first = input("Student "+str(i)+" First Name: ")
    last = input("Enter "+first+"'s Last Name: ")
    print(first+"'s initials are "+first[0]+last[0])
    
