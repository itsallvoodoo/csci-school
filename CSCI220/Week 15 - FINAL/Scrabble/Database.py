from Player import *

class Database:
    def __init__(self,fn):
        self.filename = fn
        self.players = []

    def getPlayers(self):
        return self.players

    def addPlayer(self,player):
        self.players.append(player)

    def read(self):
        infile = open(self.filename,"r")
        lines = infile.readlines()
        self.players = []
        for i in range(len(lines)): # Loop through lines
            if i == 0:
                continue
            lines[i] = lines[i].strip()
            current_line = lines[i].split(",")
            if len(current_line) == 4:
                new_player = Player(current_line[0],current_line[1])
                new_player.setNumWins(int(current_line[2]))
                new_player.setTotalGames(int(current_line[3]))
                self.players.append(new_player)
        infile.close()

        #return users,passwords,wins,total_games

    def write(self):
        outfile = open(self.filename,'w')
        print('user,password,wins,total games',file=outfile,end="")
        for i in range(len(self.players)):
            print("\n",end="",file=outfile)
            print(self.players[i],end="",file=outfile)
        outfile.close()

    def valid_user(self,u,p):
        for i in range(len(self.players)):
            if self.players[i].getName() == u and self.players[i].getPassword() == p:
                return True
        return False

    def get_user(self,u):
        for i in range(len(self.players)):
            if self.players[i].getName() == u:
                return self.players[i]
        return None        

def main():
    db = Database("db.txt")
    db.read()
    for i in range(len(db.players)):
        print(db.players[i])
        db.players[i].incNumWins()
        db.players[i].incTotalGames()
    db.write()
    db.read()
    for i in range(len(db.players)):
        print(db.players[i])    

if __name__=="__main__":
    main()
