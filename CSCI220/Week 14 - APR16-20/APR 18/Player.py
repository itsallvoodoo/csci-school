class Player:
    def __init__(self,n,p): # Constructor
        self.name = n
        self.password = p
        self.tiles = []
        self.num_wins = 0
        self.total_games = 0
        self.score = 0

    def getScore(self):
        return self.score

    def setScore(self,sc):
        self.score = sc

    def getNumWins(self):
        return self.num_wins

    def getTotalGames(self):
        return self.total_games

    def incNumWins(self):
        self.num_wins = self.num_wins + 1

    def incTotalGames(self):
        self.total_games = self.total_games + 1
    
    def setNumWins(self,w):
        self.num_wins = w

    def setTotalGames(self,t):
        self.total_games = t

    def getName(self):
        return self.name

    def setName(self,n):
        self.name = n
        
    def getPassword(self):
        return self.password

    def setPassword(self,p):
        if len(p) >= 4:
            self.password = p

    def getTiles(self):
        return self.tiles

    def addTile(self,tile):
        self.tiles.append(tile)

    def __str__(self):
        return self.name + ',' + self.password + ',' + str(self.num_wins) + ',' + str(self.total_games)


    
def main():
    player = Player("Paul","Anderson")
    player.setPassword("blah")
    print(player.getPassword())
    #print(p)
    #p.setPassword("a")
    #p.password = "a"
    #print(p.getPassword())
    
if __name__ == '__main__':
    main()
