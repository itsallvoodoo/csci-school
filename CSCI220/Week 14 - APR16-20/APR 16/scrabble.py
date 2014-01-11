# scrabble.py
# Plays Scrabble with Friends
# <Chad Hobbs>

# ----------------CLASSES---------------------
class Player:
    def __init__(self,n,p): # Constructor
        self.name = n
        self.password = p 
        self.tiles = []
        self.num_win = 0
        self.total_games = 0

    def getName(self):
        return self.name

    def setName(self,n):
        self.name = n

    def getPassword(self):
        return self.password

    def setPassword(self,n):
        if len(p) >= 3:         # Enforces a password length of 3
            self.password = p


def makeBoard():
    pass

def main():
    p = Player("Chad","Hobbs")
    print(p.name)
    print(p.password)
    


main()
