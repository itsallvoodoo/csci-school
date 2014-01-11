

def changeName(name):
    name[0],name[1],name[2] = name[1],name[2],name[0]
    
    return name

def main():
    name = ['Hobbs','Chad','Derek']
    print_name = changeName(name)

    print(print_name)

main()
    
    

    


