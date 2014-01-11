
def Linear(numbers,n): # Linear search
    for i in range(len(numbers)):
        if n == numbers[i]:
            return True
    return False




def main():
    numbers = [1,2,3,9,81,32]
    n = eval(input('n: '))

    print(Linear(numbers,n))

    
main()
