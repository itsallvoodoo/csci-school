from graphics import *

class Button:
    def __init__(self,text,p1,p2):
        self.text = text
        self.rectangle = Rectangle(p1,p2)
        self.label = Text(self.rectangle.getCenter(),self.text)

    def draw(self,win):
        self.rectangle.draw(win)
        self.label.draw(win)
        
    def clicked(self,p):
        p1 = self.rectangle.getP1()
        p2 = self.rectangle.getP2()
        big_x = max([p1.getX(),p2.getX()])
        small_x = min([p1.getX(),p2.getX()])
        big_y = max([p1.getY(),p2.getY()])
        small_y = min([p1.getY(),p2.getY()])
        x = p.getX()
        y = p.getY()
        if y <= big_y and y >= small_y and x <= big_x and x >= small_x:
            return True
        return False
