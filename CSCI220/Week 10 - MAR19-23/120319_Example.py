

def changeName(name):
    new_name = name.split(', ')
    new_name = new_name[1] + " " + new_name[0]
    return new_name

def main():
    name = "Anderson, Paul Edward"
    new_name = changeName(name)
    print(new_name)

main()
