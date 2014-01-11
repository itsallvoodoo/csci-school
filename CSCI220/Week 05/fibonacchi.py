F = 1
L = 0
n = eval(input("Numbers?: "))
for i in range(n):
    print(F,end = ",")
    F,L = F+L,F
