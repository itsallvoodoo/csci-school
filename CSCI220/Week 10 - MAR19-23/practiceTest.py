## practiceTest.py

# Write a segment of code that opens the file Test2-3.in
# and determines the average number of words per line
# in the text

def avgWordsPerLine():
    inFile = open('Test2-3.in', 'r')
    lines = inFile.readlines()
    totalWords = 0
    
    for line in lines:
        totalWords = totalWords + len(line.split())

    return totalWords / len(lines)

# Write a segment of code that opens the file Test2-4.in and
# copies every odd numbered line to Test2-4.out

def copyOddLines():
    inFile = open('Test2-4.in', 'r')
    lines = inFile.readlines()
    newFile = open('Test2-4.out', 'a')

    for i in range(1,len(lines),2):
        print(lines[i], file = newFile )

# Write a conditional statement that prints the appropriate
# message based on user input.  Assum the user input is stored
# in a variable, num, and is an integer
# User Input       Output
#  0 or less         "Error"
#  1 ... 10          "Good"
#  11 ... 15         "OK"
#  16 or more        "Awful"

def approvalFunc():
    num = input('Input an integer: ')

    if num <= 0:
        print('Error')
    elif num <= 10:
        print('Good')
    elif num <= 15:
        print('OK')
    else:
        print('Awful')

def main():
    print("Average words per line: ", avgWordsPerLine())
    copyOddLines()
    approvalFunc()
      

main()


    
