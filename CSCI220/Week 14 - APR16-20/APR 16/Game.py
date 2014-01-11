from Player import *
from Tile import *
from Board import *

class Game:
    def __init__(self):
        self.create_tiles()

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
        
    def get_tile_from_pile(self):
        tile_i = random.randint(0,len(self.tiles_list)-1)
        tile = self.tiles_list[tile_i]
        self.tiles_list.remove(tile)
        return tile
    
    def refill(self,current_player):
        if len(self.tiles_list) < (7 - len(current_player.getTiles())):
            num_tiles_to_distribute = len(self.tiles_list)
        else:
            num_tiles_to_distribute = 7 - len(current_player.getTiles())
        for i in range(num_tiles_to_distribute):
            current_player.addTile(self.get_tile_from_pile())      

    def showTiles(self,current_player,window):
        i = 45
        j = -20
        for k in range(len(current_player.getTiles())):
            p = Point(i,j)
            current_tile = current_player.getTile(k)
            current_tile.setRect(p,window)
            current_tile.draw_tile(window)
            i = i + 10

    def test_eraseTiles(self,current_player,window):
        for i in range(len(current_player.getTiles())):
            current_tile = current_player.getTile(0)
            current_tile.move(Point(170,170),window)
            current_player.removeTile(current_tile)
            

def main():
    game = Game()
    b = Board(500,500)
    player1 = Player("Chad","Hobbs")
    player2 = Player("John","Smith")
    current_player = player1
    submitbutton = Button("Submit",Point(-5,160),Point(20,170))
    submitbutton.draw(b.win)
    quitbutton = Button("Quit",Point(145,160),Point(160,170))
    quitbutton.draw(b.win)
    game.refill(current_player)
    play = True
    while len(game.tiles_list) > 1 and play:
        game.showTiles(current_player,b.win)
        while True:
            p = b.win.getMouse()
            if submitbutton.clicked(p):
                game.test_eraseTiles(current_player,b.win) ## Temp for testing
                game.refill(current_player)
                break
            if quitbutton.clicked(p):
                play = False
                b.win.close()
                break
                

                
        
        
        
    
    
    
if __name__ == '__main__':
    main()
