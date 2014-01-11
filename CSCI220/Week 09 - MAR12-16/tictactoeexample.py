from graphics import *

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
        if row1 == 'XXX':
            return 'X'
        if row1 == 'OOO':
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
    users = ["Paul","Joe"]
    passwords = ["Anderson","Smith"]
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

def login():
    win = GraphWin("Login",300,300)
    win.setCoords(0,0,100,100)
    Text(Point(20,60),"User: ").draw(win)
    Text(Point(20,40),"Password: ").draw(win)
    user_entry = Entry(Point(50,60),10)
    user_entry.draw(win)
    password_entry = Entry(Point(50,40),10)
    password_entry.draw(win)
    message = Text(Point(50,90),"")
    message.draw(win)

    # Create a login button and a quit button
    login_button = Rectangle(Point(5,15),Point(25,25))
    login_button.draw(win)
    p1 = login_button.getP1()
    p2 = login_button.getP2()
    Text(Point((p1.getX() + p2.getX())/2,(p1.getY() + p2.getY())/2),"Login").draw(win)    

    quit_button = Rectangle(Point(35,15),Point(55,25))
    quit_button.draw(win)
    p1 = quit_button.getP1()
    p2 = quit_button.getP2()
    Text(Point((p1.getX() + p2.getX())/2,(p1.getY() + p2.getY())/2),"Quit").draw(win)
    
    for i in range(3): # Maximum number of clicks
        p = win.getMouse()
        if button_clicked(login_button,p):
            user = user_entry.getText()
            password = password_entry.getText()
            if valid_user(user,password):
                win.close()
                return True
            else:
                message.setText("Invalid user and/or password")
        elif button_clicked(quit_button,p):
            win.close()
            return None
            
    win.close()
    return False

def show_winner(wins_X,wins_O):
    # Display the results
    win = GraphWin("Final Results",300,300)
    win.setCoords(0,0,100,100)
    Text(Point(50,75),"Number of wins for X: "+str(wins_X)).draw(win)
    Text(Point(50,25),"Number of wins for O: "+str(wins_O)).draw(win)
    win.getMouse()
    win.close()    

def main():
    is_valid = login()
    if not is_valid:
        return
    
    wins_X = 0
    wins_O = 0
    for g in range(3):
        winner = run_game()
        if winner == 'X':
            wins_X = wins_X + 1
        elif winner == 'O':
            wins_O = wins_O + 1

    show_winner(wins_X,wins_O)

main()
