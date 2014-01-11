# 120222_Demonstration.py
# In class exercise creating a tic tac toe board
# <Chad Hobbs>

#Global Commands
from graphics import *

#Functions
def create_board(): # Opens a new window and draws our board
    bboard = [['','',''],['','',''],['','','']]
    wwin = GraphWin("Tic-Tac-Toe",600,600)
    wwin.setCoords(0,0,30,30)
    Line(Point(10,0),Point(10,30)).draw(wwin)
    Line(Point(20,0),Point(20,30)).draw(wwin)
    Line(Point(0,10),Point(30,10)).draw(wwin)
    Line(Point(0,20),Point(30,20)).draw(wwin)
    return wwin,bboard

def check_winner(board):
    #if board[0][0] == board [0][1] and board [0]][1] == board[0][2]:
    row1 = "".join(board[0]) #puts the top line together
    if row1 == 'XXX': # checks for a X winner on top line
        return 'X'
    if row2 == 'OOO': # checks for a Y winner on top line
        return 'O'
    return None # returns a null argument in the event of a tie
        


def main(): # Main program
    win,board = create_board()


    win.getMouse()
    win.close()

    

main() # Opens the actual program

