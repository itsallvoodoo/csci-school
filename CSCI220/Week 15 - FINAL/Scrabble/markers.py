from graphics import *

class Marker:
    def __getstate__(self):
        result = self.__dict__.copy()
        # We cannot pickle graphical objects
        # Replace the actual rectangle with what we need to know to recreate a rectangle
        p1 = self.rect.getP1()
        p2 = self.rect.getP2()
        result['rect'] = {'x1':p1.getX(), 'y1':p1.getY(), 'x2':p2.getX(), 'y2':p2.getY()}
        # Replace the text_letter
        c = self.text_letter.getAnchor()
        text = self.text_letter.getText()
        result['text_letter'] = {'x':c.getX(), 'y':c.getY(), 'text':text}
        return result        

    def __setstate__(self, dict):
        self.__dict__ = dict
        self.rect = Rectangle(Point(dict['rect']['x1'],dict['rect']['y1']),Point(dict['rect']['x2'],dict['rect']['y2']))
        self.text_letter = Text(Point(dict['text_letter']['x'],dict['text_letter']['y']),dict['text_letter']['text'])
        self.rect.setFill(self.fill)

    def setTile(self,tile):
        self.tile = tile

    def hasTile(self):
        if self.tile == None:
            return False
        return True

    def getTile(self):
        return self.tile
    
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

    def draw(self,win):
        self.rect.draw(win)
        self.text_letter.draw(win)

    def undraw(self):
        self.rect.undraw()
        self.text_letter.undraw()

class BlankMarker(Marker):
    def __init__(self,i,j,win):
        self.rect = Rectangle(Point(10*i,10*j),Point(10*i+10,10*j+10))
        self.rect.draw(win)
        self.text_letter = Text(Point((10*i+10*i+10)/2,(10*j+10*j+10)/2),"")
        self.tile = None
        self.fill = None

class StartMarker(Marker):
    def __init__(self,i,j,win):
        self.rect = Rectangle(Point(10*i,10*j),Point(10*i+10,10*j+10))
        self.rect.draw(win)
        self.rect.setFill('purple')
        self.text_letter = Text(Point((10*i+10*i+10)/2,(10*j+10*j+10)/2),"@")
        self.text_letter.draw(win)
        self.tile = None
        self.fill = 'purple'

class TripleWordScoreMarker(Marker):
    def __init__(self,i,j,win):
        self.rect = Rectangle(Point(10*i,10*j),Point(10*i+10,10*j+10))
        self.rect.draw(win)
        self.rect.setFill('red')
        self.tile = None
        self.text_letter = Text(Point((10*i+10*i+10)/2,(10*j+10*j+10)/2),"x3")
        self.text_letter.draw(win)
        self.fill = 'red'
    
class DoubleWordScoreMarker(Marker):
    def __init__(self,i,j,win):
        self.rect = Rectangle(Point(10*i,10*j),Point(10*i+10,10*j+10))
        self.rect.draw(win)
        self.rect.setFill('purple')
        self.text_letter = Text(Point((10*i+10*i+10)/2,(10*j+10*j+10)/2),"x2")
        self.text_letter.draw(win)
        self.tile = None
        self.fill = 'purple'

class DoubleLetterScoreMarker(Marker):
    def __init__(self,i,j,win):
        self.rect = Rectangle(Point(10*i,10*j),Point(10*i+10,10*j+10))
        self.rect.draw(win)
        self.rect.setFill('cyan')
        self.text_letter = Text(Point((10*i+10*i+10)/2,(10*j+10*j+10)/2),"DL")
        self.text_letter.draw(win)        
        self.tile = None
        self.fill = 'cyan'

class TripleLetterScoreMarker(Marker):
    def __init__(self,i,j,win):
        self.rect = Rectangle(Point(10*i,10*j),Point(10*i+10,10*j+10))
        self.rect.draw(win)
        self.rect.setFill('blue')
        self.text_letter = Text(Point((10*i+10*i+10)/2,(10*j+10*j+10)/2),"TL")
        self.text_letter.draw(win)        
        self.tile = None
        self.fill = 'blue'
