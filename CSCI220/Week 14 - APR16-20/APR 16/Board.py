from graphics import *

class Board:
    def __init__(self,w,h):
        self.win = GraphWin('Scrabble',w,h)
        self.win.setCoords(-30,-30,180,180)
        self.markers = []
        tws_j = [0,0,0,7,7,14,14,14]
        tws_i = [0,7,14,0,14,0,7,14]
        dls_j = [0,0,2,2,3,3,3,6,6,6,6,7,7,8,8,8,8,11,11,11,12,12,14,14]
        dls_i = [3,11,6,8,0,7,14,2,6,8,12,3,11,2,6,8,12,0,7,14,6,8,3,11]
        dws_j = [1,1,2,2,3,3,4,4,10,10,11,11,12,12,13,13]
        dws_i = [1,13,2,12,3,11,4,10,4,10,3,11,2,12,1,13]
        tls_j = [1,1,5,5,5,5,9,9,9,9,13,13]
        tls_i = [5,9,1,5,9,13,1,5,9,13,5,9]
        for i in range(15):
            for j in range(15):
                if self.find_ij(i,j,tws_i,tws_j):
                    self.markers.append(TripleWordScoreMarker(i,j,self.win))
                elif i == 7 and j == 7:
                    self.markers.append(StartMarker(i,j,self.win))
                elif self.find_ij(i,j,dls_i,dls_j):
                    self.markers.append(DoubleLetterScoreMarker(i,j,self.win))
                elif self.find_ij(i,j,tls_i,tls_j):
                    self.markers.append(TripleLetterScoreMarker(i,j,self.win))
                elif self.find_ij(i,j,dws_i,dws_j):
                    self.markers.append(DoubleWordScoreMarker(i,j,self.win))
                else:
                    self.markers.append(BlankMarker(i,j,self.win))

    # Linear search
    def find_ij(self,i,j,list_i,list_j):
        for z in range(len(list_i)):
            if i == list_i[z] and j == list_j[z]:
                return True
        return False

    def get_marker_clicked(self,p):
        for marker in self.markers:
            if marker.clicked(p):
                return marker
        return None

    def score(self,markers,tiles):
        sc = 0
        mult = 1
        for i in range(len(markers)):
            if isinstance(markers[i],DoubleWordScoreMarker):
                mult = mult*2
            elif isinstance(markers[i],TripleWordScoreMarker):
                mult = mult*3
                
            if isinstance(markers[i],DoubleLetterScoreMarker):
                sc = sc + tiles[i]*2
            elif isinstance(markers[i],TripleLetterScoreMarker):
                sc = sc + tiles[i]*3
            else:
                sc = sc + tiles[i]
        sc = mult*sc
        return sc

    def __del__(self):
        self.win.close()
      
class Button:
    def __init__(self,text,p1,p2):
        self.text = text
        self.point1 = p1
        self.point2 = p2
        self.rectangle = Rectangle(self.point1,self.point2)
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

class Marker:
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

class BlankMarker(Marker):
    def __init__(self,i,j,win):
        self.rect = Rectangle(Point(10*i,10*j),Point(10*i+10,10*j+10))
        self.rect.draw(win)

class StartMarker(Marker):
    def __init__(self,i,j,win):
        self.rect = Rectangle(Point(10*i,10*j),Point(10*i+10,10*j+10))
        self.rect.draw(win)
        self.rect.setFill('purple')
        Text(Point((10*i+10*i+10)/2,(10*j+10*j+10)/2),"@").draw(win)

class TripleWordScoreMarker(Marker):
    def __init__(self,i,j,win):
        self.rect = Rectangle(Point(10*i,10*j),Point(10*i+10,10*j+10))
        self.rect.draw(win)
        self.rect.setFill('red')
        Text(Point((10*i+10*i+10)/2,(10*j+10*j+10)/2),"x3").draw(win)
    
class DoubleWordScoreMarker(Marker):
    def __init__(self,i,j,win):
        self.rect = Rectangle(Point(10*i,10*j),Point(10*i+10,10*j+10))
        self.rect.draw(win)
        self.rect.setFill('purple')
        Text(Point((10*i+10*i+10)/2,(10*j+10*j+10)/2),"x2").draw(win)

class DoubleLetterScoreMarker(Marker):
    def __init__(self,i,j,win):
        self.rect = Rectangle(Point(10*i,10*j),Point(10*i+10,10*j+10))
        self.rect.draw(win)
        self.rect.setFill('cyan')
        Text(Point((10*i+10*i+10)/2,(10*j+10*j+10)/2),"DL").draw(win)

class TripleLetterScoreMarker(Marker):
    def __init__(self,i,j,win):
        self.rect = Rectangle(Point(10*i,10*j),Point(10*i+10,10*j+10))
        self.rect.draw(win)
        self.rect.setFill('blue')
        Text(Point((10*i+10*i+10)/2,(10*j+10*j+10)/2),"TL").draw(win)

def main():
##    b = Board(500,500)
##    # Get three markers
##    word_markers = []
##    tiles = [1,2,1]
##    while len(word_markers) < 3:
##        p = b.win.getMouse()
##        marker = b.get_marker_clicked(p)
##        if marker != None:
##            word_markers.append(marker)
##    print(b.score(word_markers,tiles))

    if __name__=="__main__":
        main()
        
