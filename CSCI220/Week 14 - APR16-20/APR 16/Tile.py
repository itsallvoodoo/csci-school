from graphics import*
import random
from Player import *

class Tile():
    def __init__(self,l):
        self.letter = l
        self.setValue()
        self.rect = Rectangle(Point(0,0),Point(10,10))
        self.text_letter = Text(Point(5,5),self.letter)
        self.text_value = Text(Point(8,2),self.value)
        self.text_value.setSize(6)

    def setRect(self,p,win):
        px = p.getX()
        py = p.getY()
        x1 = px-5
        y1 = py-5
        x2 = px+5
        y2 = py+5
        self.rect = Rectangle(Point(x1,y1),Point(x2,y2))
        self.rect.setFill("yellow1")
        self.text_letter = Text(Point((x1+x2)//2,(y1+y2)//2),self.letter)
        self.text_value = Text(Point(x2-1,y1+2),self.value)
        self.text_value.setSize(5)

        
    def draw_tile(self,win):
        self.rect.draw(win)
        self.text_letter.draw(win)
        self.text_value.draw(win)
        
    def setRectColor(self):
        self.rect.setFill("yellow4")
        
    def move(self,p,win):
        c = self.rect.getCenter()
        dx = p.getX()-c.getX()
        dy = p.getY()-c.getY()
        self.rect.move(dx,dy)
        self.rect.setFill("yellow1")
        self.text_value.move(dx,dy)
        self.text_letter.move(dx,dy)

    def clicked(self,p):
        p1 = self.rect.getP1()
        p2 = self.rect.getP2()
        big_x = max([p1.getX(),p2.getX()])
        small_x = min([p1.getX(),p2.getX()])
        big_y = max([p1.getY(),p2.getY()])
        small_y = min([p1.getY(),p2.getY()])
        x = p.getX()
        y = p.getY()
        if y <= big_y and y >= small_y and x <= big_x and x >= small_x:
            return True
        return False
        
    def setLetter(self,l):
        self.letter = l
        self.setValue()
                          
    def setValue(self):
        l = self.letter
        if l == "":
            self.value = 0
        elif l == "A":
            self.value = 1
        elif l == "B":
            self.value = 3
        elif l == "C":
            self.value = 3
        elif l == "D":
            self.value = 2
        elif l == "E":
            self.value = 1
        elif l == "F":
            self.value = 4
        elif l == "G":
            self.value = 2
        elif l == "H":
            self.value = 4
        elif l == "I":
            self.value = 1
        elif l == "J":
            self.value = 8
        elif l == "K":
            self.value = 5
        elif l == "L":
            self.value = 1
        elif l == "M":
            self.value = 3
        elif l == "N":
            self.value = 1
        elif l == "O":
            self.value = 1
        elif l == "P":
            self.value = 3
        elif l == "Q":
            self.value = 10
        elif l == "R":
            self.value = 1
        elif l == "S":
            self.value = 1
        elif l == "T":
            self.value = 1
        elif l == "U":
            self.value = 1
        elif l == "V":
            self.value = 4
        elif l == "W":
            self.value = 4
        elif l == "X":
            self.value = 8
        elif l == "Y":
            self.value = 4
        elif l == "Z":
            self.value = 10
            
 


def main():
##    instructions = Text(Point(105,200),"Click on a tile to move them")
##    instructions.draw(window)
##
##    quit = Button("Quit",Point(175,180),Point(190,190))
##    quit.draw(window)
    
##    while True:
##        p = window.getMouse()
##        for i in range(len(p1.tiles)):
##            if p1.tiles[i].clicked(p):
##                p1.tiles[i].setRectColor()
##                point2 = window.getMouse()
##                p1.tiles[i].move(point2,window)
##            elif p2.tiles[i].clicked(p):
##                p2.tiles[i].setRectColor()
##                point2 = window.getMouse()
##                p2.tiles[i].move(point2,window)
##        if quit.clicked(p):
##            break
##    window.close()

                
    if __name__=="__main__":
        main()

    
    
    
        
    
