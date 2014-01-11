from Button import *
from graphics import *

class ChangePasswordScreen:
    def change_password(self,db):        
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
        change_button = Button("Change",Point(5,15),Point(25,25))
        change_button.draw(win)

        quit_button = Button("Quit",Point(35,15),Point(55,25))
        quit_button.draw(win)

        while True:
            p = win.getMouse()
            if change_button.clicked(p):
                player = db.get_user(user_entry.getText())
                if player == None:
                    message.setText("User invalid")
                elif player.getPassword() != password_entry.getText():
                    message.setText("Old password incorrect")
                else:
                    player.setPassword(password_entry2.getText())
                    db.write()
                    win.close()
                    return
            elif quit_button.clicked(p):
                win.close()
                return
