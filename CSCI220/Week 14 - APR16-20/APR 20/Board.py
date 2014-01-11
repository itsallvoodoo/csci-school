from graphics import *
from Button import *
from Tile import *
from Dictionary import *

class Board:
    def __init__(self,w,h,player1,player2):
        self.dict = Dictionary("wordlist.txt")
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
            self.markers.append([]) # Make two dimensional
            for j in range(15):
                if self.find_ij(i,j,tws_i,tws_j):
                    self.markers[i].append(TripleWordScoreMarker(i,j,self.win))
                elif i == 7 and j == 7:
                    self.markers[i].append(StartMarker(i,j,self.win))
                elif self.find_ij(i,j,dls_i,dls_j):
                    self.markers[i].append(DoubleLetterScoreMarker(i,j,self.win))
                elif self.find_ij(i,j,tls_i,tls_j):
                    self.markers[i].append(TripleLetterScoreMarker(i,j,self.win))
                elif self.find_ij(i,j,dws_i,dws_j):
                    self.markers[i].append(DoubleWordScoreMarker(i,j,self.win))
                else:
                    self.markers[i].append(BlankMarker(i,j,self.win))

        self.player1_name_text = Text(Point(75,-25),player1.getName())
        self.player1_name_text.draw(self.win)

        self.player2_name_text = Text(Point(-15,170),player2.getName())
        self.player2_name_text.draw(self.win)

        self.quit_button = Button("Quit",Point(152,160),Point(170,170))
        self.quit_button.draw(self.win)

        self.submit_button = Button("Submit",Point(152,140),Point(180,150))
        self.submit_button.draw(self.win)

        self.check_button = Button("Check",Point(152,120),Point(180,130))
        self.check_button.draw(self.win)

        self.pass_button = Button("Pass",Point(152,100),Point(180,110))
        self.pass_button.draw(self.win)

        self.message = Text(Point(75,175),"")
        self.message.draw(self.win)

        self.create_tiles()

        self.player1 = player1
        self.player2 = player2

        self.player1_score = Text(Point(-15,160),str(player2.getScore()))
        self.player1_score.draw(self.win)
        
        self.player2_score = Text(Point(160,-15),str(player1.getScore()))
        self.player2_score.draw(self.win)

        self.update_screen()

        self.current_score = 0 # Current score of the board

    def setPlayer1(self,player):
        self.player1 = player

    def setPlayer2(self,player):
        self.player1 = player

    def update_screen(self):
        self.player1_name_text.setText(self.player1.getName())
        self.player2_name_text.setText(self.player2.getName())
        self.display_tiles()

        self.player1_score.setText(self.player1.getScore())
        self.player2_score.setText(self.player2.getScore())
        
    def display_tiles(self):
        # Move tiles to the correct location
        x = 30
        y = -15
        for tile in self.player1.getTiles():
            tile.move(Point(x,y))
            x = x + 15

        x = -15
        y = 150
        for tile in self.player2.getTiles():
            tile.move(Point(x,y))
            y = y - 15

    def create_tiles(self):
        self.tiles_list = [Tile(""),Tile("")]
        for i in range(9):
            self.tiles_list.append(Tile("A"))
        for i in range(2):
            self.tiles_list.append(Tile("B"))
            self.tiles_list.append(Tile("C"))
        for i in range(4):
            self.tiles_list.append(Tile("D"))
        for i in range(12):
            self.tiles_list.append(Tile("E"))
        for i in range(2):
            self.tiles_list.append(Tile("F"))
        for i in range(3):
            self.tiles_list.append(Tile("G"))
        for i in range(2):
            self.tiles_list.append(Tile("H"))
        for i in range(9):
            self.tiles_list.append(Tile("I"))
        for i in range(1):
            self.tiles_list.append(Tile("J"))
            self.tiles_list.append(Tile("K"))
        for i in range(4):
            self.tiles_list.append(Tile("L"))
        for i in range(2):
            self.tiles_list.append(Tile("M"))
        for i in range(6):
            self.tiles_list.append(Tile("N"))
        for i in range(8):
            self.tiles_list.append(Tile("O"))
        for i in range(2):
            self.tiles_list.append(Tile("P"))
        for i in range(1):
            self.tiles_list.append(Tile("Q"))
        for i in range(6):
            self.tiles_list.append(Tile("R"))
        for i in range(4):
            self.tiles_list.append(Tile("S"))
        for i in range(6):
            self.tiles_list.append(Tile("T"))
        for i in range(4):
            self.tiles_list.append(Tile("U"))
        for i in range(2):
            self.tiles_list.append(Tile("V"))
            self.tiles_list.append(Tile("W"))
        for i in range(1):
            self.tiles_list.append(Tile("X"))
        for i in range(2):
            self.tiles_list.append(Tile("Y"))
        for i in range(1):
            self.tiles_list.append(Tile("Z"))
        # Draw off screen for now
        for tile in self.tiles_list:
            tile.move(Point(-100,-100))
            tile.draw(self.win)
        
    def get_tile_from_pile(self):
        tile_i = random.randint(0,len(self.tiles_list)-1)
        tile = self.tiles_list[tile_i]
        self.tiles_list.remove(tile)
        return tile
    
    def refill(self,player):
        num_tiles_to_distribute = 7 - len(player.getTiles())
        if num_tiles_to_distribute > len(self.tiles_list):
            num_tiles_to_distribute = len(self.tiles_list)
            
        for i in range(num_tiles_to_distribute):
            player.addTile(self.get_tile_from_pile())

    def check_word(self,markers):
        tiles = []
        for marker in markers:
            tiles.append(marker.getTile())
        return self.dict.check(tiles)

    def build_list_of_tiles(self,ci,cj,inxs):
        if ci > 1:
            if self.markers[ci-1][cj].getTile() and not ([ci-1,cj] in inxs):
                inxs.append([ci-1,cj])
                self.build_list_of_tiles(ci-1,cj,inxs)
        if cj > 1:
            if self.markers[ci][cj-1].getTile() and not ([ci,cj-1] in inxs):
                inxs.append([ci,cj-1])
                self.build_list_of_tiles(ci,cj-1,inxs)
        if ci < 14:
            if self.markers[ci+1][cj].getTile() and not ([ci+1,cj] in inxs):
                inxs.append([ci+1,cj])
                self.build_list_of_tiles(ci+1,cj,inxs)
        if cj < 14:
            if self.markers[ci][cj+1].getTile() and not ([ci,cj+1] in inxs):
                inxs.append([ci,cj+1])
                self.build_list_of_tiles(ci,cj+1,inxs)

    def score_board(self):
        ci = None
        cj = None
        num_tiles = 0
        for i in range(len(self.markers)):
            for j in range(len(self.markers[i])):
                if self.markers[i][j].getTile():
                    if ci == None and cj == None:
                        ci = i
                        cj = j
                    num_tiles = num_tiles + 1   

        if num_tiles == 0: # Nothing on the board
            return 0
        
        # Check to make sure a list of letters
        tile_inxs = [[ci,cj]]
        self.build_list_of_tiles(ci,cj,tile_inxs)
        if len(tile_inxs) != num_tiles: # not all tiles are reachable
            return -1
    
        total_score = 0
        for i in range(len(self.markers)): # Go through each row
            word = [] # List of markers
            for j in range(len(self.markers[i])-1,-1,-1):
                if self.markers[i][j].hasTile() == False and len(word) > 0:
                    if len(word) == 1:
                        word = []
                        continue
                    elif self.check_word(word):
                        total_score = total_score + self.score(word)
                        word = []
                    else:
                        return -1
                elif self.markers[i][j].hasTile():
                    word.append(self.markers[i][j])
                    
            if len(word) > 1:
                if self.check_word(word):
                    total_score = total_score + self.score(word)
                else:
                    return -1
                
        for j in range(len(self.markers[0])): # Go through each column
            word = [] # List of markers
            for i in range(len(self.markers)):
                if self.markers[i][j].hasTile() == False and len(word) > 0:
                    if len(word) == 1:
                        word = []
                        continue                    
                    elif self.check_word(word):
                        total_score = total_score + self.score(word)
                        word = []
                    else:
                        return -1
                elif self.markers[i][j].hasTile():
                    word.append(self.markers[i][j])
                    
            if len(word) > 1:
                if self.check_word(word):
                    total_score = total_score + self.score(word)
                else:
                    return -1

        return total_score

    def check(self):
        total_score = self.score_board()        
        if total_score == -1: # Invalid board
            self.message.setText("Invalid board")
        else:
            self.message.setText("You would gain: " + str(total_score - self.current_score))

    def submit(self,player):
        total_score = self.score_board()
        if total_score == -1: # Invalid board
            self.message.setText("Invalid board")
            return -1
        
        self.message.setText("You gain: " + str(total_score - self.current_score))
        points = total_score - self.current_score
        self.current_score = total_score
        # remove the tiles
        tiles_to_remove = []
        for tile in player.getTiles():
            if tile.getMarker():
                tiles_to_remove.append(tile)
        for tile in tiles_to_remove:
            player.getTiles().remove(tile)
        self.update_screen()
        return points
            
    def take_turn(self,player):
        tiles = player.getTiles()
        tile_selected = None
        while True:
            p = self.win.getMouse()
            
            # Check to see if a tile was clicked
            tile_clicked = False
            for i in range(len(tiles)):
                if tiles[i].clicked(p):
                    if tile_selected:
                        tile_selected.setOrigColor()
                    tile_selected = tiles[i]
                    tile_selected.setClickedColor()
                    tile_clicked = True
                    break
                    
            # Check to see if a mark was clicked
            mark_clicked = False
            if not tile_clicked and tile_selected:
                for i in range(len(self.markers)):
                    for j in range(len(self.markers[i])):
                        if self.markers[i][j].clicked(p):
                            p2 = self.markers[i][j].rect.getCenter()
                            tile_selected.move(p2)
                            mark_clicked = True
                            self.markers[i][j].setTile(tile_selected)
                            tile_selected.setMarker(self.markers[i][j])
                            break
                    
            if tile_clicked or mark_clicked: # Done
                continue
            elif self.pass_button.clicked(p):
                return "pass"                    
            elif self.submit_button.clicked(p):
                points = self.submit(player)
                if points != -1:
                    player.setScore(player.getScore() + points)
                    return "submit"                    
            elif self.check_button.clicked(p):
                self.check()                    
            elif self.quit_button.clicked(p):
                self.win.close()
                return "quit"
            elif tile_selected: # Generic move
                tile_selected.move(p)
                marker = tile_selected.getMarker()
                if marker:
                    marker.setTile(None)
                tile_selected.setMarker(None)

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

    def score(self,markers):
        sc = 0
        mult = 1
        for i in range(len(markers)):
            if isinstance(markers[i],DoubleWordScoreMarker):
                mult = mult*2
            elif isinstance(markers[i],TripleWordScoreMarker):
                mult = mult*3
                
            if isinstance(markers[i],DoubleLetterScoreMarker):
                sc = sc + markers[i].getTile().getValue()*2
            elif isinstance(markers[i],TripleLetterScoreMarker):
                sc = sc + markers[i].getTile().getValue()*3
            else:
                sc = sc + markers[i].getTile().getValue()
        sc = mult*sc
        return sc

    def __del__(self):
        self.win.close()

class Marker:
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

class BlankMarker(Marker):
    def __init__(self,i,j,win):
        self.rect = Rectangle(Point(10*i,10*j),Point(10*i+10,10*j+10))
        self.rect.draw(win)
        self.tile = None

class StartMarker(Marker):
    def __init__(self,i,j,win):
        self.rect = Rectangle(Point(10*i,10*j),Point(10*i+10,10*j+10))
        self.rect.draw(win)
        self.rect.setFill('purple')
        Text(Point((10*i+10*i+10)/2,(10*j+10*j+10)/2),"@").draw(win)
        self.tile = None

class TripleWordScoreMarker(Marker):
    def __init__(self,i,j,win):
        self.rect = Rectangle(Point(10*i,10*j),Point(10*i+10,10*j+10))
        self.rect.draw(win)
        self.rect.setFill('red')
        self.tile = None
        Text(Point((10*i+10*i+10)/2,(10*j+10*j+10)/2),"x3").draw(win)
    
class DoubleWordScoreMarker(Marker):
    def __init__(self,i,j,win):
        self.rect = Rectangle(Point(10*i,10*j),Point(10*i+10,10*j+10))
        self.rect.draw(win)
        self.rect.setFill('purple')
        Text(Point((10*i+10*i+10)/2,(10*j+10*j+10)/2),"x2").draw(win)
        self.tile = None

class DoubleLetterScoreMarker(Marker):
    def __init__(self,i,j,win):
        self.rect = Rectangle(Point(10*i,10*j),Point(10*i+10,10*j+10))
        self.rect.draw(win)
        self.rect.setFill('cyan')
        Text(Point((10*i+10*i+10)/2,(10*j+10*j+10)/2),"DL").draw(win)
        self.tile = None

class TripleLetterScoreMarker(Marker):
    def __init__(self,i,j,win):
        self.rect = Rectangle(Point(10*i,10*j),Point(10*i+10,10*j+10))
        self.rect.draw(win)
        self.rect.setFill('blue')
        Text(Point((10*i+10*i+10)/2,(10*j+10*j+10)/2),"TL").draw(win)
        self.tile = None

def main():
    b = Board(500,500)
    # Get three markers
    word_markers = []
    tiles = [1,2,1]
    while len(word_markers) < 3:
        p = b.win.getMouse()
        marker = b.get_marker_clicked(p)
        if marker != None:
            word_markers.append(marker)
    print(b.score(word_markers,tiles))

if __name__=="__main__":
    main()
        
