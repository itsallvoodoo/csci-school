# Lab7_yoyo_LCC.py
# Going back and forth with robot
# Chad Luke and Corey

def yoyo(n,s,t):
    for i in range(n):
        forward(s,t)
        wait(1)
        backward(s,t)
        wait(1)
#end yoyo()

def main():
    n = eval(raw_input("How many iterations?: "))
    s = eval(raw_input("How fast?(0.1 to 1): "))
    t = eval(raw_input("For how long?: "))
    yoyo(n,s,t)

main()
