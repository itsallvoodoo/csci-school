from graphics import *

def read_db(filename):
    infile = open(filename,"r")
    lines = infile.readlines()
    users = []
    passwords = []
    wins = []
    total_games = []
    for i in range(len(lines)): # Loop through lines
        if i == 0:
            continue
        lines[i] = lines[i].strip()
        current_line = lines[i].split(",")
        if len(current_line) == 4:
            users.append(current_line[0])
            passwords.append(current_line[1])
            wins.append(int(current_line[2]))
            total_games.append(int(current_line[3]))
    infile.close()

    return users,passwords,wins,total_games

def write_db(filename,users,passwords,wins,total_games):
    outfile = open(filename,'w')
    print('user,password,wins,total games',file=outfile,end="")
    for i in range(len(users)):
        print("\n"+users[i],passwords[i],wins[i],total_games[i],end="",sep=',',file=outfile)
    outfile.close()

def create_board():
    board = [['','',''],['','',''],['','','']]
    wwin = GraphWin("Tic Tac Toe",300,300)
    wwin.setCoords(30,30,0,0)
    Line(Point(10,0),Point(10,30)).draw(wwin)
    Line(Point(20,0),Point(20,30)).draw(wwin)
    Line(Point(0,10),Point(30,10)).draw(wwin)
    Line(Point(0,20),Point(30,20)).draw(wwin)
    return wwin,board

def get_column(board,i):
    return board[0][i] + board[1][i] + board[2][i]

def get_row(board,i):
    return board[i][0] + board[i][1] + board[i][2]

def check_winner(board):
    for i in range(3):
        row = get_row(board,i)
        if row == 'XXX':
            return 'X'
        if row == 'OOO':
            return 'O'

    for i in range(3):
        col = get_column(board,i)
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
    
def run_game():
    win,board = create_board()

    for turn in range(9):
        if turn % 2 == 0: # Even -> X
            who = 'X'
        else:
            who = 'O'

        take_turn(win,board,who)
        if check_winner(board) != None:
            win.close()
            return check_winner(board) # Exit the game

    win.close()
    return check_winner(board)

def valid_user(u,p):
    users,passwords,wins,total_wins = read_db("db.txt")
    for i in range(len(users)):
        if users[i] == u and passwords[i] == p:
            return True
    return False

def button_clicked(button,p):
    p1 = button.getP1()
    p2 = button.getP2()
    big_x = max([p1.getX(),p2.getX()])
    small_x = min([p1.getX(),p2.getX()])
    big_y = max([p1.getY(),p2.getY()])
    small_y = min([p1.getY(),p2.getY()])
    x = p.getX()
    y = p.getY()
    if y <= big_y and y >= small_y and x <= big_x and x >= small_x:
        return True
    return False

def create_button(p1,p2,display_text,win):
    button = Rectangle(p1,p2)
    button.draw(win)
    #p1 = button.getP1()
    #p2 = button.getP2()
    Text(Point((p1.getX() + p2.getX())/2,(p1.getY() + p2.getY())/2),display_text).draw(win)    
    return button

def change_password():
    win = GraphWin("Change Password",300,300)
    win.setCoords(0,0,100,100)
    Text(Point(20,80),"User: ").draw(win)
    Text(Point(20,60),"Old Password: ").draw(win)
    Text(Point(20,40),"New password: ").draw(win)
    user_entry = Entry(Point(50,80),10)
    user_entry.draw(win)
    password_entry = Entry(Point(50,60),10)
    password_entry.draw(win)
    password_entry2 = Entry(Point(50,40),10)
    password_entry2.draw(win)
    message = Text(Point(50,90),"")
    message.draw(win)

    # Create a create button and a quit button
    change_button = create_button(Point(5,15),Point(25,25),"Change",win)

    quit_button = create_button(Point(35,15),Point(55,25),"Quit",win)

    for i in range(3): # Maximum number of clicks
        p = win.getMouse()
        if button_clicked(change_button,p):
            users,passwords,wins,total_games = read_db("db.txt")
            found = False
            for j in range(len(users)):
                if users[j] == user_entry.getText():
                    found = True
                    break
            if found:
                passwords[j] = password_entry2.getText()
                write_db("db.txt",users,passwords,wins,total_games)
                win.close()
                return
            else:
                message.setText("Password incorrect")
        elif button_clicked(quit_button,p):
            win.close()
            return

def create_new_user():
    win = GraphWin("Create new user",300,300)
    win.setCoords(0,0,100,100)
    Text(Point(20,60),"User: ").draw(win)
    Text(Point(20,40),"Password: ").draw(win)
    user_entry = Entry(Point(50,60),10)
    user_entry.draw(win)
    password_entry = Entry(Point(50,40),10)
    password_entry.draw(win)
    message = Text(Point(50,90),"")
    message.draw(win)

    # Create a create button and a quit button
    new_button = create_button(Point(5,15),Point(25,25),"Create",win)

    quit_button = create_button(Point(35,15),Point(55,25),"Quit",win)

    for i in range(3): # Maximum number of clicks
        p = win.getMouse()
        if button_clicked(new_button,p):
            users,passwords,wins,total_games = read_db("db.txt")
            users.append(user_entry.getText())
            passwords.append(password_entry.getText())
            wins.append(0)
            total_games.append(0)
            write_db("db.txt",users,passwords,wins,total_games)
            win.close()
            return
        elif button_clicked(quit_button,p):
            win.close()
            return

def login(users_logged_in):
    win = GraphWin("Login",300,300)
    win.setCoords(0,0,100,100)

    Text(Point(17,80),"User 1: ").draw(win)
    Text(Point(17,70),"Password 1: ").draw(win)
    user_entry = Entry(Point(50,80),10)
    user_entry.draw(win)
    password_entry = Entry(Point(50,70),10)
    password_entry.draw(win)

    Text(Point(17,60),"User 2: ").draw(win)
    Text(Point(17,50),"Password 2: ").draw(win)
    user_entry2 = Entry(Point(50,60),10)
    user_entry2.draw(win)
    password_entry2 = Entry(Point(50,50),10)
    password_entry2.draw(win)

    message = Text(Point(50,90),"")
    message.draw(win)

    # Create a login button and a quit button
    login_button = create_button(Point(5,15),Point(25,25),"Login",win)

    new_button = create_button(Point(5,2),Point(35,12),"New user",win)

    change_button = create_button(Point(45,2),Point(95,12),"Change Password",win)

    quit_button = create_button(Point(35,15),Point(55,25),"Quit",win)
    
    for i in range(10): # Maximum number of clicks
        p = win.getMouse()
        if button_clicked(login_button,p):
            user1 = user_entry.getText()
            password1 = password_entry.getText()
            user2 = user_entry2.getText()
            password2 = password_entry2.getText()
            if valid_user(user1,password1) and valid_user(user2,password2):
                users_logged_in.append(user1)
                users_logged_in.append(user2)
                win.close()
                return True
            else:
                message.setText("Invalid user and/or password")
        elif button_clicked(new_button,p):
            create_new_user()
        elif button_clicked(change_button,p):
            change_password()
        elif button_clicked(quit_button,p):
            win.close()
            return None
            
    win.close()
    return False

def update_wins_total_games(user_X,user_O,wins_X,wins_O):
    users,passwords,wins,total_games = read_db("db.txt")
    for j in range(len(users)):
        if users[j] == user_X:
            wins[j] = wins[j] + wins_X
            total_games[j] = total_games[j] + wins_X + wins_O
        elif users[j] == user_O:            
            wins[j] = wins[j] + wins_O
            total_games[j] = total_games[j] + wins_X + wins_O
        
    write_db("db.txt",users,passwords,wins,total_games)

def show_winner(wins_X,wins_O):
    # Display the results
    win = GraphWin("Final Results",300,300)
    win.setCoords(0,0,100,100)
    Text(Point(50,75),"Number of wins for X: "+str(wins_X)).draw(win)
    Text(Point(50,25),"Number of wins for O: "+str(wins_O)).draw(win)
    win.getMouse()
    win.close()    

def main():
    users_logged_in = []
    is_valid = login(users_logged_in)
    if not is_valid:
        return
    user_X = users_logged_in[0]
    user_O = users_logged_in[1]
    
    wins_X = 0
    wins_O = 0
    for g in range(3):
        winner = run_game()
        if winner == 'X':
            wins_X = wins_X + 1
        elif winner == 'O':
            wins_O = wins_O + 1

    update_wins_total_games(user_X,user_O,wins_X,wins_O)
    show_winner(wins_X,wins_O)

main()
