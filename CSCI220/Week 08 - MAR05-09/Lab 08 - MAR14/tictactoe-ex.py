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

def main():
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
    
    for i in range(3): # Maximum number of incorrect logins
        win.getMouse()
        user = user_entry.getText()
        password = password_entry.getText()
        if valid_user(user,password):
            break
        else:
            message.setText("Invalid user and/or password")
            
    win.close()
    if not valid_user(user,password):
        return
    
    wins_X = 0
    wins_O = 0
    for g in range(3):
        winner = run_game()
        if winner == 'X':
            wins_X = wins_X + 1
        elif winner == 'O':
            wins_O = wins_O + 1

    # Display the results
    win = GraphWin("Final Results",300,300)
    win.setCoords(0,0,100,100)
    Text(Point(50,75),"Number of wins for X: "+str(wins_X)).draw(win)
    Text(Point(50,25),"Number of wins for O: "+str(wins_O)).draw(win)
    win.getMouse()
    win.close()

main()
