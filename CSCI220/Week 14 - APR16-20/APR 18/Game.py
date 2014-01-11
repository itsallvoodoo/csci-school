from Player import *
from Tile import *
from Board import *
from Database import *
from StartScreen import *
import os

class Game:
    def set_new_game_id(self):        
        previous_ids = []
        for filename in os.listdir("games"):
            previous_ids.append(int(filename))
        if len(previous_ids) == 0:
            self.game_id = 1
        else:
            self.game_id = max(previous_ids) + 1

    def is_game_in_progress(gid):
        for filename in os.listdir("games"):
            if str(gid) == filename:
                return True
        return False

    def start_new_game(self,player):
        self.set_new_game_id()

        # Create the board
        self.board = Board(400,400,player,Player("Player 2",""))
        self.board.refill(player)
        self.board.display_tiles()

        # Set up the rest of the current game state
        self.current_player = player # Default to the first person
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
                self.load(result,start_screen.getPlayer())
        
        while True:
            self.result = self.board.take_turn(self.current_player)
            if self.result == "pass" and self.prev_result == "pass":
                break # Show result
            if self.result == "quit":
                return
            if self.result == "submit":
                self.current_player.refill()
                
            self.prev_result = self.result

    def load(self,game_id,player):
        return
        
# Main routine that runs the game
def main():
    g = Game()
    g.run()

main()
    
