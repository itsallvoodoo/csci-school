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

    def __getstate__(self):
        result = self.__dict__.copy()
        # Remove the reference to the marker to avoid circular reference
        # But we will need to repopulate it
        result['marker'] = None
        p1 = self.rect.getP1()
        p2 = self.rect.getP2()
        # We cannot pickle graphical objects
        # Replace the actual rectangle with what we need to know to recreate a rectangle
        result['rect'] = {'x1':p1.getX(), 'y1':p1.getY(), 'x2':p2.getX(), 'y2':p2.getY()}
        # Replace the text_letter
        c = self.text_letter.getAnchor()
        text = self.text_letter.getText()
        result['text_letter'] = {'x':c.getX(), 'y':c.getY(), 'text':text}
        # Replace the text_value
        c = self.text_value.getAnchor()
        text = self.text_value.getText()
        result['text_value'] = {'x':c.getX(), 'y':c.getY(), 'text':text}
        return result        

    def __setstate__(self, dict):
        self.__dict__ = dict
        self.rect = Rectangle(Point(dict['rect']['x1'],dict['rect']['y1']),Point(dict['rect']['x2'],dict['rect']['y2']))
        self.text_letter = Text(Point(dict['text_letter']['x'],dict['text_letter']['y']),dict['text_letter']['text'])
        self.text_value = Text(Point(dict['text_value']['x'],dict['text_value']['y']),dict['text_value']['text'])
        self.text_value.setSize(6)
        self.setOrigColor()

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

    def undraw(self):
        self.rect.undraw()
        self.text_letter.undraw()
        self.text_value.undraw()
        
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
    win = GraphWin("Test",400,400)
    win.setCoords(-30,-30,180,180)
    t = Tile("A")
    t.draw(win)
    t.move(Point(50,50))
    t.undraw()
    import pickle
    t2 = pickle.loads(pickle.dumps(t))
    t2.move(Point(75,75))
    t2.draw(win)
    win.getMouse()
    win.close()

                
if __name__=="__main__":
    main()

    
    
    
        
    
