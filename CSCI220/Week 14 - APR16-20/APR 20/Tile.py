from graphics import*
import random
from Player import *
from Button import *

class Tile():
    def __init__(self,l):
        self.letter = l
        self.setValue()
        self.rect = Rectangle(Point(0,0),Point(10,10))
        self.text_letter = Text(Point(5,5),self.letter)
        self.text_value = Text(Point(8,2),self.value)
        self.text_value.setSize(6)
        self.setOrigColor()
        self.marker = None

    def setMarker(self,marker):
        self.marker = marker

    def getMarker(self):
        return self.marker

    def setRect(self,p,win):
        px = p.getX()
        py = p.getY()
        x1 = px-10
        y1 = py-10
        x2 = px+10
        y2 = py+10
        self.rect = Rectangle(Point(x1,y1),Point(x2,y2))
        self.rect.setFill("yellow1")
        self.text_letter = Text(Point((x1+x2)//2,(y1+y2)//2),self.letter)
        self.text_value = Text(Point(x2-3,y1+4),self.value)
        self.text_value.setSize(6)

        
    def draw(self,win):
        self.rect.draw(win)
        self.text_letter.draw(win)
        self.text_value.draw(win)
        
    def setClickedColor(self):
        self.rect.setFill("yellow4")

    def setOrigColor(self):
        self.rect.setFill("yellow1")
        
    def move(self,p):
        c = self.rect.getCenter()
        dx = p.getX()-c.getX()
        dy = p.getY()-c.getY()
        self.rect.move(dx,dy)
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

    def getValue(self):
        return self.value

    def getLetter(self):
        return self.letter
                          
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
    letters_list = ["",""]
    for i in range(9):
        letters_list.append("A")
    for i in range(2):
        letters_list.append("B")
        letters_list.append("C")
    for i in range(4):
        letters_list.append("D")
    for i in range(12):
        letters_list.append("E")
    for i in range(2):
        letters_list.append("F")
    for i in range(3):
        letters_list.append("G")
    for i in range(2):
        letters_list.append("H")
    for i in range(9):
        letters_list.append("I")
    for i in range(1):
        letters_list.append("J")
        letters_list.append("K")
    for i in range(4):
        letters_list.append("L")
    for i in range(2):
        letters_list.append("M")
    for i in range(6):
        letters_list.append("N")
    for i in range(8):
        letters_list.append("O")
    for i in range(2):
        letters_list.append("P")
    for i in range(1):
        letters_list.append("Q")
    for i in range(6):
        letters_list.append("R")
    for i in range(4):
        letters_list.append("S")
    for i in range(6):
        letters_list.append("T")
    for i in range(4):
        letters_list.append("U")
    for i in range(2):
        letters_list.append("V")
        letters_list.append("W")
    for i in range(1):
        letters_list.append("X")
    for i in range(2):
        letters_list.append("Y")
    for i in range(1):
        letters_list.append("Z")
    window = GraphWin("Tiles",400,400)
    window.setCoords(0,0,210,210)
    
    p1 = Player("Paul","123")
    p2 = Player("Liz", "123")
    
    instructions = Text(Point(105,200),"Click on a tile to move them")
    instructions.draw(window)

    quit = Button("Quit",Point(175,180),Point(190,190))
    quit.draw(window)
    
    i = 0
    while i < 7:
        letter_i = random.randint(0,len(letters_list)-1)
        letter = letters_list[letter_i]
        letters_list.remove(letter)
        tile = Tile(letter)
        p1.addTile(tile)
        i = i + 1
        
    k = 0
    while k < 7:
        letter_i = random.randint(0,len(letters_list)-1)
        letter = letters_list[letter_i]
        letters_list.remove(letter)
        tile = Tile(letter)
        p2.addTile(tile)
        k = k + 1
    
    xp1 = 25
    yp1 = 10
    for j in range(len(p1.tiles)):
        p = Point(xp1,yp1)
        p1.tiles[j].setRect(p,window)
        p1.tiles[j].draw_tile(window)
        xp1 = xp1 + 25
        
    xp2 = 15
    yp2 = 190
    for j in range(len(p1.tiles)):
        p = Point(xp2,yp2)
        p2.tiles[j].setRect(p,window)
        p2.tiles[j].draw_tile(window)
        yp2 = yp2 - 25
        
    while True:
        p = window.getMouse()
        for i in range(len(p1.tiles)):
            if p1.tiles[i].clicked(p):
                p1.tiles[i].setRectColor()
                point2 = window.getMouse()
                p1.tiles[i].move(point2,window)
            elif p2.tiles[i].clicked(p):
                p2.tiles[i].setRectColor()
                point2 = window.getMouse()
                p2.tiles[i].move(point2,window)
        if quit.clicked(p):
            break
    window.close()

                
if __name__=="__main__":
    main()

    
    
    
        
    
