# Demonstration_120406.py
# In class demonstration
# <Chad Hobbs>

class Person:
    # Constructor (python specific)
    def __init__(n,p,nw,tg):
        self.name = n
        self.password = p
        self.num_wins = nw
        self.total_games = tg

    def changePassword(self,p):
        self.password = p

    def getPassword(self): # getter - Not needed but good convention
        return self.password

    def setPassword(self,p): # setter - Not needed as well
        if p[0] = '#':
            self.password = p
            
# Use the class

chad = Person("Chad","Hobbs",0,0) # Calls __init__

chad.changePassword("secret") # Calls a function (better)
# paul.password = "blah"  # Modifies attribute directly
