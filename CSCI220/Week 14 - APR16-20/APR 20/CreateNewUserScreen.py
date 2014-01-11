from Button import *
from graphics import *
from Player import *

class CreateNewUserScreen:
    def create_new_user(self,db):
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
        new_button = Button("Create",Point(5,15),Point(25,25))
        new_button.draw(win)

        quit_button = Button("Quit",Point(35,15),Point(55,25))
        quit_button.draw(win)

        while True:
            p = win.getMouse()
            if new_button.clicked(p):
                player = Player(user_entry.getText(),password_entry.getText())
                db.addPlayer(player)
                db.write()
                win.close()
                break
            elif quit_button.clicked(p):
                win.close()
                break
