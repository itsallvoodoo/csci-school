# Assignment_6.py
# Plays Tic Tac Toe with login function and repeatability
# <Chad Hobbs>

from graphics import *

def login():

    # Initiates variables and gets name
    greeting = ""
    name = False
    key = -1
    print("Welcome to Chad's Tic-Tac-Toe game!")
    print("")
    user = input("Please enter your name: ")

    # Gets user and password list and puts it into a basic list
    users = open("userlist.txt","r")
    piece = users.read()
    userlist = piece.split("=")
    users.close()
    
    for l in range(len(userlist)): # Error handling loop, removes blank list entries
        if userlist[l] == '':
            userlist.remove('')
            
    users.close() # closes file from read/write
    
    for i in range(len(userlist)): # Breaks down list into individual elements
        userlist[i] = userlist[i].split("-")
        if user == userlist[i][0]: # While breaking the list down into more lists, we also check to see if the user already exists
            name = True
            key = i

    if name == True: #If a user was found, passord is requested and checked, otherwise a new entry will be made
        for j in range(3): #allow for 3 login attempts
            greeting = "Hello " + user + ", what is your password?: "
            pw = input(greeting)
            if userlist[key][1] == pw:
                print("Your password is correct. You have won",int(userlist[key][2]),"games!")
                return key,userlist
            else:
                print("Your name and password are incorrect. Please try again.")
        print("You have exceeded login attempts. Please contact the administrator.")
        key = -3
        return key,userlist
              
    else: # Gets a pw for a new user
        greeting = "Welcome " + user + ", please enter a password to save your high score: "
        pw = input(greeting)
        temp = [user,pw,0]
        userlist.append(temp)
        key = len(userlist) - 1
        return key,userlist
        
def logout(userlist): # This function stores the user back in the user text file

    string = ""
    users = open("userlist.txt","w") # Get's the userlist file and opens it for overwrite
    
    for i in range(len(userlist)):
        string = string + userlist[i][0] + "-" + userlist[i][1] + "-" + str(userlist[i][2]) + "="
            
    users.write(string) # Writes the data into the file
    users.close() # Closes the file from writing


def create_board():
    board = [['','',''],['','',''],['','','']]
    win = GraphWin("Tic Tac Toe",300,300)
    win.setCoords(30,30,0,0)
    win.setBackground("white")
    Line(Point(10,0),Point(10,30)).draw(win)
    Line(Point(20,0),Point(20,30)).draw(win)
    Line(Point(0,10),Point(30,10)).draw(win)
    Line(Point(0,20),Point(30,20)).draw(win)
    return win,board

def get_column(board,i):
    return board[0][i] + board[1][i] + board[2][i]

def check_winner(board):
    row1 = "".join(board[0])
    if row1 == 'XXX':
        return 'X'
    if row1 == 'OOO':
        return 'O'

    row2 = "".join(board[1])
    if row2 == 'XXX':
        return 'X'
    if row2 == 'OOO':
        return 'O'
    
    row3 = "".join(board[2])
    if row3 == 'XXX':
        return 'X'
    if row3 == 'OOO':
        return 'O'

    col = get_column(board,0)
    if col == 'XXX':
        return 'X'
    if col == 'OOO':
        return 'O'

    col = get_column(board,1)
    if col == 'XXX':
        return 'X'
    if col == 'OOO':
        return 'O'

    col = get_column(board,2)
    if col == 'XXX':
        return 'X'
    if col == 'OOO':
        return 'O'

    diag = board[0][0] + board[1][1] + board[2][2]
    if diag == 'XXX':
        return 'X'
    if diag == 'OOO':
        return 'O'

    diag = board[2][0] + board[1][1] + board[0][2]
    if diag == 'XXX':
        return 'X'
    if diag == 'OOO':
        return 'O'
    
    return None

def take_turn(win,board,who):
    # Get Move
    p = win.getMouse()
    col = int(p.getX() // 10)
    row = int(p.getY() // 10)
    Text(Point(col*10 + 5, row*10 + 5),who).draw(win)
    board[row][col] = who
    
def main():
    log = False
    
    while log == False: # Multiple 3 game set loop
        key,userlist = login() # Logs in user
        if key == -3:
            log = True
            break

        xwins = 0
        owins = 0
        for i in range(3):
            print("Playing best of 3, you are currently on game",i+1)
            
            win,board = create_board() # Creates game board
        
            for turn in range(9):
                if turn % 2 == 0: # Even -> X
                    who = 'X'
                else:
                    who = 'O'

                take_turn(win,board,who)
                if check_winner(board) != None:
                    print("Player",check_winner(board),"has won this game!")
                    if who == 'X':
                        userlist[key][2] = int(userlist[key][2]) + 1
                        xwins = xwins + 1
                    else:
                        owins = owins + 1
                    win.close()
                    # Exit the game
                    break
            if xwins == 2 or owins == 2: # Check to see if either side has won best of 3
                win.close()
                break

        print(userlist[key][0],"has a high score of",userlist[key][2])
        print("")
        repeat = input("Would you like to play another best of 3?(yes or no): ")
        if repeat.lower() != "yes":
            print("Thank you for playing!")
            log = True
            
        logout(userlist) #logs out current user if new data is to be written to file
            
main()
