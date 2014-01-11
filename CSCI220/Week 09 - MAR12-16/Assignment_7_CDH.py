# Assignment_7_CDH.py
# Plays tic-tac-toe with 2 players and a database
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

    turn = 9
    while turn > 0:
        turn = turn - 1
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

def get_data(): # Gets data out of database
    users = []
    passwords = []
    scores = []
    games = []
    infile = open("db.txt","r")
    first_line = infile.readline()
    for line in infile:
        if line != '':
            u_p_s = line.strip().split(',')
            if len(u_p_s) == 4:
                users.append(u_p_s[0])
                passwords.append(u_p_s[1])
                scores.append(int(u_p_s[2]))
                games.append(int(u_p_s[3]))
                
    infile.close()          
    return users,passwords,scores,games

def get_user(key):
    users,passwords,scores,games = get_data()
    user = users[key]
    return user

def get_password(key):
    users,passwords,scores,games = get_data()
    password = passwords[key]
    return password

def get_score(key):
    users,passwords,scores,games = get_data()
    score = scores[key]
    return score

def get_game(key):
    users,passwords,scores,games = get_data()
    game = games[key]
    return game

def update_password(key,password):
    users,passwords,scores,games = get_data()
    passwords[key] = password
    store_data(users,passwords,scores,games)
    return

def update_score(key,score):
    users,passwords,scores,games = get_data()
    scores[key] = score
    store_data(users,passwords,scores,games)
    return

def update_game(key,game):
    users,passwords,scores,games = get_data()
    games[key] = game
    store_data(users,passwords,scores,games)
    return

def store_data(users,passwords,scores,games):
        outfile = open("db.txt","w")
        print("user,password,wins,games",file=outfile)
        i = 0
        while i < len(users):
            print(users[i],passwords[i],scores[i],games[i],sep=',',file=outfile)
            i = i + 1
        outfile.close()
        return
                    
def valid_user(u,p):
    users,passwords,scores,games = get_data()
    i = 0
    while i < len(users):
        if users[i] == u and passwords[i] == p:
            return True,i
        i = i+1
    return False,i

def button_clicked(p1,p2,p):
    big_x = max([p1.getX(),p2.getX()])
    small_x = min([p1.getX(),p2.getX()])
    big_y = max([p1.getY(),p2.getY()])
    small_y = min([p1.getY(),p2.getY()])
    x = p.getX()
    y = p.getY()
    if y <= big_y and y >= small_y and x <= big_x and x >= small_x:
        return True
    return False


def draw_button(win,pt1,pt2,text):
    button = Rectangle(pt1,pt2)
    button.draw(win)
    Text(Point((pt1.getX() + pt2.getX())/2,(pt1.getY() + pt2.getY())/2),text).draw(win)
    return

def login(player):
    key = 99
    win = GraphWin("Login",300,300)
    win.setCoords(0,0,100,100)
    player_text = "Player " + str(player)
    Text(Point(50,80),player_text).draw(win)
    Text(Point(20,60),"User: ").draw(win)
    Text(Point(20,40),"Password: ").draw(win)
    user_entry = Entry(Point(50,60),10)
    user_entry.draw(win)
    password_entry = Entry(Point(50,40),10)
    password_entry.draw(win)
    message = Text(Point(50,90),"")
    message.draw(win)

    # Create a login button and a quit button
    login_p1 = Point(15,15)
    login_p2 = Point(35,25)
    draw_button(win,login_p1,login_p2,"Login")    

    quit_p1 = Point(65,15)
    quit_p2 = Point(85,25)
    draw_button(win,quit_p1,quit_p2,"Back")
        
    while True: # Maximum number of clicks
        p = win.getMouse()
        if button_clicked(login_p1,login_p2,p):
            user = user_entry.getText()
            password = password_entry.getText()
            check_users,key = valid_user(user,password)
            if check_users:
                win.close()
                return True,key
            else:
                message.setText("Invalid user and/or password")
        elif button_clicked(quit_p1,quit_p2,p):
            win.close()
            return None,key
            
    #win.close()
    #return None,key

def show_winner(best,key):
    # Display the results
    win = GraphWin("Final Results",300,300)
    win.setCoords(0,0,100,100)
    Text(Point(50,80),"The Winner of this best of 3 is "+str(best)).draw(win)
    user = get_user(key)
    score = get_score(key)
    games = get_game(key)
    Text(Point(50,60),"Statistics for "+user).draw(win)
    Text(Point(50,40),"Lifetime wins: "+str(score)).draw(win)
    Text(Point(50,20),"Lifetime games: "+str(games)).draw(win)
    win.getMouse()
    win.close()
    return

def new_player():
    # Draw prompts and entry boxes
    win = GraphWin("Create New Player",300,300)
    win.setCoords(0,0,100,100)
    Text(Point(50,90),"Please enter a name and password").draw(win)
    Text(Point(20,70),"User: ").draw(win)
    Text(Point(20,50),"Password: ").draw(win)
    Text(Point(20,30),"Verify PW: ").draw(win)
    user = Entry(Point(50,70),10)
    user.draw(win)
    pw1 = Entry(Point(50,50),10)
    pw1.draw(win)
    pw2 = Entry(Point(50,30),10)
    pw2.draw(win)
    submit_p1 = Point(15,10)
    submit_p2 = Point(35,20)
    draw_button(win,submit_p1,submit_p2,"Submit")
    back_p1 = Point(65,10)
    back_p2 = Point(85,20)
    draw_button(win,back_p1,back_p2,"Back")

    # Get mouseclick and either submit or go back
    clicked = False
    while not clicked:
        p = win.getMouse()
        if button_clicked(submit_p1,submit_p2,p):
            password_entry = pw1.getText()
            password_entry2 = pw2.getText()
            user_entry = user.getText()
            if password_entry == password_entry2:
                users,passwords,scores,games = get_data()
                users.append(user_entry)
                passwords.append(password_entry)
                scores.append(0)
                games.append(0)
                store_data(users,passwords,scores,games)
                clicked = True
            else:
                Text(Point(50,40),"Password Mismatch!").draw(win)
        if button_clicked(back_p1,back_p2,p):
            clicked = True
    
    win.close()
    return

def change_pw():
    valid,key = login(1)
    win = GraphWin("Update Password",300,300)
    win.setCoords(0,0,100,100)
    

    if valid:
        Text(Point(50,90),"Please enter new password").draw(win)
        Text(Point(20,50),"Password: ").draw(win)
        Text(Point(20,30),"Again: ").draw(win)
        pw1 = Entry(Point(50,50),10)
        pw1.draw(win)
        pw2 = Entry(Point(50,30),10)
        pw2.draw(win)
        submit_p1 = Point(15,10)
        submit_p2 = Point(35,20)
        draw_button(win,submit_p1,submit_p2,"Submit")
        back_p1 = Point(65,10)
        back_p2 = Point(85,20)
        draw_button(win,back_p1,back_p2,"Back")

        # Get mouseclick and either submit or go back
        clicked = False
        while not clicked:
            p = win.getMouse()
            if button_clicked(submit_p1,submit_p2,p):
                password_entry = pw1.getText()
                password_entry2 = pw2.getText()
                if password_entry == password_entry2:
                    update_password(key,password_entry)
                    clicked = True
                else:
                    Text(Point(50,40),"Password Mismatch!").draw(win)
            if button_clicked(back_p1,back_p2,p):
                clicked = True
            
    else:
        Text(Point(50,50),"Your login was incorrect!").draw(win)
        Text(Point(50,50),"Click on screen to close").draw(win)
        win.getMouse()

    win.close()
    return

def welcome(): # Initial user interaction screen.
    win = GraphWin("Tic Tac Toe",300,300)
    win.setCoords(0,0,100,100)
    Text(Point(50,95),"Welcome to Chad's Tic-tac-toe game!").draw(win)

    # Draw all of our welcome screen buttons
    c_p1 = Point(35,77)
    c_p2 = Point(65,87)
    draw_button(win,c_p1,c_p2,"Create New")
    pw_p1 = Point(35,58)
    pw_p2 = Point(65,68)
    draw_button(win,pw_p1,pw_p2,"Update PW")
    onep_p1 = Point(35,39)
    onep_p2 = Point(65,49)
    draw_button(win,onep_p1,onep_p2,"1 Player")
    twop_p1 = Point(35,20)
    twop_p2 = Point(65,30)
    draw_button(win,twop_p1,twop_p2,"2 Player")
    q_p1 = Point(35,1)
    q_p2 = Point(65,11)
    draw_button(win,q_p1,q_p2,"Quit")

    # Check see which route to take
    clicked = False
    while not clicked:
        click = win.getMouse()
        if button_clicked(c_p1,c_p2,click):
            new_player()
            win.close()
            return 0,0,0
        if button_clicked(onep_p1,onep_p2,click):
            play,key = login(1)
            win.close()
            return 1,key,0
        if button_clicked(pw_p1,pw_p2,click):
            change_pw()
            win.close()
            return 0,0,0
        if button_clicked(twop_p1,twop_p2,click):
            play,key = login(1)
            play,key2 = login(2)
            win.close()
            return 2,key,key2
        if button_clicked(q_p1,q_p2,click):
            win.close()
            return 3,0,0

def main():
    play = 0
    while play != 3:
        play,key,key2 = welcome()

        if play == 1: # 1 Player Version
            wins_X = 0
            wins_O = 0
            
            while wins_X < 2 and wins_O < 2:
                winner = run_game()
                if winner == 'X':
                    wins_X = wins_X + 1
                    score = get_score(key) + 1
                    update_score(key,score)
                elif winner == 'O':
                    wins_O = wins_O + 1
                game = get_game(key)
                game = game + 1
                update_game(key,game)

            if wins_X > wins_O:
                best = 'X'
            else:
                best = 'O'
                
            show_winner(best,key)

        if play == 2: # 2 Player Version
            wins_X = 0
            wins_O = 0

            while wins_X < 2 and wins_O < 2:
                winner = run_game()
                if winner == 'X':
                    wins_X = wins_X + 1
                    score = get_score(key) + 1
                    print(score)
                    update_score(key,score)
                elif winner == 'O':
                    wins_O = wins_O + 1
                    score = get_score(key2) + 1
                    update_score(key2,score)
                game = get_game(key)
                game = game + 1
                update_game(key,game)
                game = get_game(key2)
                game = game + 1
                update_game(key2,game)

            if wins_X > wins_O:
                best = 'X'
            else:
                best = 'O'
                
            show_winner(best,key)
            show_winner(best,key2)

    # If 3 becomes true exit game
    


main()
