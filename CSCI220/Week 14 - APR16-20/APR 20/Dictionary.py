from Tile import *

class Dictionary:
    def __init__(self,filename):
        # read the list of words
        infile = open(filename,'r')
        self.words = infile.readlines()
        for i in range(len(self.words)):
            self.words[i] = self.words[i].strip()
            self.words[i] = self.words[i].upper()
        infile.close()

    def check(self,tiles):
        word = ""
        for tile in tiles:
            word = word + tile.getLetter()

        for i in range(len(self.words)):
            if word == self.words[i]:
                return True
        return False

def main():
    dict = Dictionary("wordlist.txt")
    tiles = [Tile("C"),Tile("A"),Tile("T")]
    print(dict.check(tiles))

if __name__ == '__main__':
    main()
