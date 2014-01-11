## hangman.py
## This program plays the Hangman game
## <Chad Hobbs>

from random import randrange
from graphics import *

def createwin(): # Build the basic window and greet the user
    win = GraphWin("Hangman",400,400)
    win.setCoords(0,0,100,100)
    win.setBackground("White")
    greet = Text(Point(50,80),"Welcome to Chad's Hangman game!")
    greet.draw(win)
    click = Text(Point(50,50),"Click to contine")
    click.draw(win)
    p = win.getMouse()
    click.undraw()
    greet.undraw()
    return win

def draw_main(win,display,guesses,unused,used,status,keepgoing): # draw things to window based on conditions
    dis_text = Text(Point(50,5),display)
    unused_text = Text(Point(50,10),unused)
    used_text = Text(Point(50,15),used)
    guess_string = "You have " + str(guesses) + " guesses left."
    guess_text = Text(Point(50,95),guess_string)
    status_text = Text(Point(40,50),status)
    dis_text.draw(win)
    unused_text.draw(win)
    used_text.draw(win)
    guess_text.draw(win)
    status_text.draw(win)
    
    if guesses < 8:
        Line(Point(60,20),Point(100,20)).draw(win)
        Line(Point(80,20),Point(80,90)).draw(win)
        Line(Point(80,90),Point(60,90)).draw(win)
    if guesses < 7:
        Line(Point(60,90),Point(60,80)).draw(win)
    if guesses < 6:
        Circle(Point(60,75),5).draw(win)
    if guesses < 5:
        Line(Point(60,70),Point(60,40)).draw(win)
    if guesses < 4:
        Line(Point(60,60),Point(50,50)).draw(win)
    if guesses < 3:
        Line(Point(60,60),Point(70,50)).draw(win)
    if guesses < 2:
        Line(Point(60,40),Point(50,30)).draw(win)
    if guesses < 1:
        Line(Point(60,40),Point(70,30)).draw(win)
        return ""
    if keepgoing:
        return True
    letter = get_letter(win)
    dis_text.undraw()
    unused_text.undraw()
    used_text.undraw()
    guess_text.undraw()
    status_text.undraw()
 
    return letter

def get_letter(win): # Get a letter from the user

    entered = Entry(Point(10,60),4)
    entered.draw(win)
    submit_button = Rectangle(Point(2,35),Point(18,45))
    submit_button.draw(win)
    submit_word = Text(Point(10,40),"Submit")
    submit_word.draw(win)
    button = False

    while button == False:
        p = win.getMouse()
        button = button_clicked(submit_button,p)
    
    letter = entered.getText().lower()
    entered.setText("")

    submit_word.undraw()
    submit_button.undraw()
    entered.undraw()
                 
    return letter

def button_clicked(button,p): # Check to see whether or not the button has been clicked
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

def getword(): # Get a word from the database
    infile = open("wordlist.txt","r")
    lines = infile.readlines()
    wordline = randrange(0,len(lines))
    word = lines[wordline].lower()
    infile.close()
    return word

def createstrings(word): # Buld the initial strings to read or write to
    display = []
    for i in range(1,len(word)):
        display.append('_')
    unused = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    used = []
    return display,used,unused
    
def game(word,win): # Play the game
    notguessed = True
    guesses = 7
    display,used,unused = createstrings(word)
    status = ""
    
    while notguessed:
        keepgoing = checkwinner(display)
        letter = draw_main(win,display,guesses,unused,used,status,keepgoing)
        status = ""
        if guesses == 0:
            return False
        if keepgoing:
            return True
        skip = False
        for i in range(0,len(used)): # Scan letters guessed to make sure you haven't already tried it
            if letter == used[i]:
                status = "You have already guessed this letter!"
                skip = True
                break
        if skip == False:
            for j in range(0,len(unused)): # Removes letter from your guessable letter list
                if letter == unused[j]:
                    unused.remove(letter)
                    break
            match = False
            for k in range(0,len(word)): # Checks the word against the letter and if there is a match, updates the display
                if letter == word[k]:
                    display[k] = letter
                    match = True
            used.append(letter)
            if not match:
                guesses = guesses - 1
           
def checkwinner(display): # See whether or not somebody won
    for i in range(0,len(display)):
        if display[i] == '_':
            return False
    return True

def main(): # Main program
    word = getword()
    # print(word) This is in for testing and knowing the word
    win = createwin()
    winner = game(word,win)

    if winner:
        Text(Point(30,60),"You Win!!").draw(win)
    else:
        Text(Point(30,60),"You Lose!!").draw(win)
    
    Text(Point(30,50),"Click to close").draw(win)
    p = win.getMouse()
    win.close()
    

main()

        
