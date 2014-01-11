# Lab8_TicTacToe.py
# Plays Tic Tac Toe with login function and repeatability
# <Chad Hobbs>

from graphics import *
from time import sleep

def login():
    win = GraphWin("Tic-Tac-Toe",300,300)
    win.setCoords(0,0,100,100)
    Text(Point(50,80),"Welcome to Chad's Tic-Tac-Toe game!").draw(win)
    userprompt = Text(Point(50,60),"Please enter your name")
    usertext = Text(Point(20,40),"User: ")
    pwcheck = Text(Point(50,60),"Please enter your password")
    pwprompt = Text(Point(50,60),"Please enter a password to save games")
    pwtext = Text(Point(20,40),"Password: ")
    user_entry = Entry(Point(50,40),10)
    password_entry = Entry(Point(50,40),10)
    message = Text(Point(50,90),"")
    message.draw(win)

    # Initiates variables and gets name
    userprompt.draw(win)
    usertext.draw(win)
    user_entry.draw(win)
    okay_button(win)
    user = user_entry.getText()
    name = False
    key = -1
    userprompt.undraw()
    usertext.undraw()
    user_entry.undraw()
    print(user)

    # Gets user and password list and puts it into a basic list
    users = open("userlist.txt","r")
    piece = users.read()
    userlist = piece.strip().split("=")
    users.close()

    print(userlist)
    for l in range(len(userlist)): # Error handling loop, removes blank list entries
        if userlist[l] == '':
            userlist.remove('')
    print(userlist)        
    for i in range(len(userlist)): # Breaks down list into individual elements
        userlist[i] = userlist[i].split("-")
        if user == userlist[i][0]: # While breaking the list down into more lists, we also check to see if the user already exists
            name = True
            key = i
    print(userlist)
            
          
    if name == True: #If a user was found, passord is requested and checked, otherwise a new entry will be made
        pwtext.draw(win)
        for j in range(3): #allow for 3 login attempts
            pwcheck.draw(win)
            password_entry.draw(win)
            okay_button(win)
            pw = password_entry.getText()
            pwcheck.undraw()
            password_entry.undraw()
            if userlist[key][1] == pw:
                verify = "You have won " + str(userlist[key][2]) + " games!"
                Text(Point(50,30),"Your password is correct.").draw(win)
                Text(Point(50,20),verify).draw(win)
                okay_button(win)
                win.close()
                return key,userlist
            else:
                faila = Text(Point(50,30),"Your password is incorrect.")
                failb = Text(Point(50,10),"Please try again.")
                faila.draw(win)
                failb.draw(win)
                time.sleep(5)
                faila.undraw()
                failb.undraw()
        Text(Point(50,30),"You have exceeded attempts. Goodbye.").draw(win)
        okay_button(win)
        win.close()
        key = -3
        return key,userlist
              
    else: # Gets a pw for a new user
        pwprompt.draw(win)
        password_entry.draw(win)
        okay_button(win)
        pw = password_entry.getText()
        temp = [user,pw,0]
        userlist.append(temp)
        key = len(userlist) - 1
        win.close()
        return key,userlist

def okay_button(win):
    box = Rectangle(Point(25,5),Point(75,15))
    boxtext = Text(Point(50,10),"Continue")
    box.draw(win)
    boxtext.draw(win)
    click = False
    while click == False:
        xy = win.getMouse()
        if xy.getX() > 25 and xy.getX() < 75 and xy.getY() > 5 and xy.getY() < 75:
            click = True
        
    box.undraw()
    boxtext.undraw()
    return
        
def logout(userlist): # This function stores the user back in the user text file

    string = ""
    users = open("userlist.txt","w") # Get's the userlist file and opens it for overwrite
    
    for i in range(len(userlist)):
        string = string + userlist[i][0] + "-" + userlist[i][1] + "-" + str(userlist[i][2]) + "="
            
    users.write(string) # Writes the data into the file
    users.close() # Closes the file from writing


def create_board():
    board = [['','',''],['','',''],['','','']]
    win = GraphWin("Tic Tac Toe",300,400)
    win.setCoords(30,40,0,0)
    win.setBackground("white")
    Line(Point(10,0),Point(10,30)).draw(win)
    Line(Point(20,0),Point(20,30)).draw(win)
    Line(Point(0,10),Point(30,10)).draw(win)
    Line(Point(0,20),Point(30,20)).draw(win)
    return win,board

def get_column(board,i):
    return board[0][i] + board[1][i] + board[2][i]

def get_row(board,i):
    return board[i][0] + board[i][1] + board[i][2]

def check_winner(board):
    for rc in range(0,3):
        row = get_row(board,rc)
        if row == 'XXX':
            return 'X'
        if row == 'OOO':
            return 'O'

    for cc in range(0,3):
        col = get_column(board,cc)
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

def show_winner(who,win):
    output = "Player " + who + " has won this game!"
    outputtext = Text(Point(15,38),output)
    outputtext.draw(win)
    time.sleep(5)
    return

def exit_game(key,userlist):
    display = ""
    win = GraphWin("Tic-Tac-Toe",300,300)
    win.setCoords(0,0,100,100)
    print(userlist[key][0])
    print(userlist[key][1])
    print(userlist[key][2])
    print(userlist)
    display = str(userlist[key][0]) + " has a high score of " + str(userlist[key][2])
    Text(Point(50,60),display).draw(win)

    Rectangle(Point(15,25),Point(45,35)).draw(win)
    Text(Point(30,30),"Play again").draw(win)
    Rectangle(Point(60,25),Point(80,35)).draw(win)
    Text(Point(70,30),"Quit").draw(win)
    click = False
    while click == False:
        xy = win.getMouse()
        if xy.getX() > 15 and xy.getX() < 45 and xy.getY() > 25 and xy.getY() < 35:
            win.close()
            return False
        if xy.getX() > 60 and xy.getX() < 80 and xy.getY() > 25 and xy.getY() < 35:
            win.close()
            return True

    
def main():
    besttext = ""
    log = False
    
    while log == False: # Multiple 3 game set loop
        key,userlist = login() # Logs in user
        if key == -3:
            log = True
            break

        xwins = 0
        owins = 0
        for i in range(3):
            win,board = create_board() # Creates game board
            besttext = "Playing best of 3, you are on game " + str(i+1)
            Text(Point(15,35),besttext).draw(win)
            
            for turn in range(9):
                if turn % 2 == 0: # Even -> X
                    who = 'X'
                else:
                    who = 'O'

                take_turn(win,board,who)
                if check_winner(board) != None:
                    show_winner(who,win)
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
      
        log = exit_game(key,userlist)
            
        logout(userlist) #logs out current user if new data is to be written to file
            
main()
