from Player import *
from Tile import *
from Board import *
from Database import *
from StartScreen import *
from ChangePasswordScreen import *
from CreateNewUserScreen import *
from Button import *
from Dictionary import *
import os
import pickle

class Game:
    def set_new_game_id(self): # adds current game to directory of game_ids       
        previous_ids = []
        for filename in os.listdir("games"):
            previous_ids.append(int(filename))
        if len(previous_ids) == 0:
            self.game_id = 1
        else:
            self.game_id = max(previous_ids) + 1

    def start_new_game(self,player):
        self.set_new_game_id()

        # Create the board
        player2 = Player("Player 2","")
        self.board = Board(400,400,player,player2,self.game_id)
        self.board.refill(player)
        self.board.display_tiles()

        # Set up the rest of the current game state
        self.current_player = player # Default to the first person
        self.players.append(player) # Add the first player to the list of players
        self.prev_result = None

    def run(self):
        self.players = []
        # Read the players from the database
        self.db = Database("db.txt")
        self.db.read()
        # From our tic-tac-toe game, we need to have the user login
        start_screen = StartScreen()
        while True:
            result = start_screen.login(self.db)
            if result == "new":
                self.start_new_game(start_screen.getPlayer())
                break
            elif result == "quit": # Quit was hit, so end the game
                return
            else: # Must be a game id
                # TODO
                # First start a new game. This will create window that we can adjust
                # Then call the load function, passing in the game id that was entered and
                # the player that logged in using the start_screen
                break

        # TODO: Save the game (should be one line)
        
        while True:
            self.result = self.board.take_turn(self.current_player)
            if self.result == "pass" and self.prev_result == "pass":
                break # Show result
            if self.result == "quit":
                return
            if self.result == "submit":
                self.board.refill(self.current_player)
                self.board.update_screen()
            elif self.result == "refresh":
                # TODO: Call the load function with the correct player being shown for this screen
                continue # A refresh was issued, that does not constitute a turn, so continue

            #TODO: Change players to the other player
            
            #TODO: Save the same
                
            self.prev_result = self.result

    def save(self):
        outfile = open("games/"+str(self.game_id),"wb")
        game_state = {};
        game_state['db'] = self.db
        game_state['players'] = self.players
        game_state['board'] = self.board
        game_state['prev_result'] = self.prev_result
        game_state['current_player'] = self.current_player
        game_state['game_id'] = self.game_id
        outfile.write(pickle.dumps(game_state))
        outfile.close()

    def load(self,game_id,player):
        self.game_id = game_id
        infile = open("games/"+str(game_id),'rb')
        game_state_pickled = infile.read()
        infile.close()
        game_state = pickle.loads(game_state_pickled)
        # Make sure there is a spot for this player or they are already part of the game
        joined = False
        for i in range(len(game_state['players'])):
            if player.getName() == game_state['players'][i].getName():
                joined = True
                player = game_state['players'][i] # Set to the actual player
            else:
                player2 = game_state['players'][i] # Other player
            
        if not joined and len(game_state['players']) == 2: # Cannot join
            return False

        # Now load up the game
        self.board.undraw()
        self.players = game_state['players']
        if not joined:
            self.players.append(player)
        self.db = game_state['db']
        self.prev_result = game_state['prev_result']
        self.game_id = game_id
        self.current_player = game_state['current_player']
        self.board.setPlayer1(player)
        if len(self.players) == 1:
            self.board.setPlayer2(self.board.getPlayer2()) # Get generic player 2
        elif self.players[0] != player:
            self.board.setPlayer2(self.players[0])
        else:
            self.board.setPlayer2(self.players[1])

        self.board.current_score = game_state['board'].current_score
        self.board.markers = game_state['board'].getMarkers()
        self.board.tiles_list = game_state['board'].getTilesList()
        # Go through each marker and if it has a tile, adjust the tile to point to the marker
        markers = self.board.getMarkers()
        for i in range(len(markers)):
            for j in range(len(markers[i])):
                markers[i][j].draw(self.board.win)
                if markers[i][j].getTile() != None:
                    tile = markers[i][j].getTile()
                    tile.setMarker(markers[i][j])
                    tile.draw(self.board.win)
        for tile in self.board.tiles_list:
            tile.draw(self.board.win)
        for player in self.players:
            for tile in player.getTiles():
                tile.draw(self.board.win)

        if not joined:
            self.board.refill(player)
        self.board.setGameID(game_id)
        self.board.update_screen()
        
# Main routine that runs the game
def main():
    g = Game()
    g.run()

main()
    
