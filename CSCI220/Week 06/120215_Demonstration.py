# 120215_Demonstration.py
# In class exercises
# <Chad Hobbs>

## Login Example



def login(user,password):


    database_users = ["Paul","Luke","Pasha","Anna","Mac"]
    database_passwords = ["Anderson","Duvall","S","Bishop","Kimmerle"]

    valid = False

    for i in range(len(database_users)): # Go through the database and check each user
        db_user = database_users[i]
        db_password = database_passwords[i]
        if db_user == user and db_password == password:
            valid = True

    return valid
    


def main():

    choice = 1
    while choice > 0:
        user = input("Enter your user name: ")
        password = input("Enter your password: ")
        result = login(user,password)

        if result == True:
            print("Welcome to the fold.")
        else:
            print("Your password is incorrect.")

main()
