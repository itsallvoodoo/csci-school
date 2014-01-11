# 120229_Demonstration.py
# In class demonstration of Tic Tac Toe
# <Chad Hobbs>


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


def take_turn(win,board,who): #Get's a move, draws it to the board, and records it
    p = win.getMouse()
    col = int(p.getX() // 10)
    row = int(p.getY() // 10)
    Text(Point(col*10 + 5, row*10 + 5),who).draw(win)
    board[row][col] = who
    return board

    
def main():
    win,board = create_board()

    for turn in range(9):
        if turn % 2 == 0: # Even -> X
            who = 'X'
        else:
            who = 'O'
        if check_winner(board) != None:
            print(check_winner(board))
    
    win.getMouse()
    win.close()

main()
