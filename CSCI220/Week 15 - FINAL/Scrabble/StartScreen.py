from graphics import *
from Button import *
from CreateNewUserScreen import *
from ChangePasswordScreen import *
import os

class StartScreen:
    def is_game_in_progress(self,gid):
        for filename in os.listdir("games"):
            if str(gid) == filename:
                return True
        return False

    def __init__(self):
        self.player = None

    def getPlayer(self):
        return self.player
    
    def login(self,db):        
        win = GraphWin("CofC Scrabble",300,300)
        win.setCoords(0,0,100,100)

        Text(Point(17,80),"User: ").draw(win)
        Text(Point(17,70),"Password: ").draw(win)
        user_entry = Entry(Point(50,80),10)
        user_entry.draw(win)
        password_entry = Entry(Point(50,70),10)
        password_entry.draw(win)

        message = Text(Point(50,90),"")
        message.draw(win)

        # Create a login button and a quit button
        login_button = Button("New game",Point(5,50),Point(35,60))
        login_button.draw(win)

        continue_button = Button("Continue game",Point(5,35),Point(50,45))
        continue_button.draw(win)
        game_id_entry = Entry(Point(70,40),10)
        game_id_entry.draw(win)

        new_button = Button("New user",Point(5,2),Point(35,12))
        new_button.draw(win)

        change_button = Button("Change Password",Point(45,2),Point(95,12))
        change_button.draw(win)

        quit_button = Button("Quit",Point(5,15),Point(25,25))
        quit_button.draw(win)
        
        while True: # Maximum number of clicks
            p = win.getMouse()
            if login_button.clicked(p):
                user1 = user_entry.getText()
                password1 = password_entry.getText()
                if db.valid_user(user1,password1):
                    self.player = db.get_user(user1)
                    win.close()
                    return "new"
                else:
                    message.setText("Invalid user and/or password")
            elif continue_button.clicked(p):
                user1 = user_entry.getText()
                password1 = password_entry.getText()
                gid = int(game_id_entry.getText())
                in_progress = self.is_game_in_progress(gid)
                if db.valid_user(user1,password1) and in_progress:
                    self.player = db.get_user(user1)
                    win.close()
                    return gid
                else:
                    message.setText("Invalid user/password or game ID")
            elif new_button.clicked(p):
                screen = CreateNewUserScreen()
                screen.create_new_user(db)
            elif change_button.clicked(p):
                screen = ChangePasswordScreen()
                screen.change_password(db)
            elif quit_button.clicked(p):
                win.close()
                return "quit"
            
