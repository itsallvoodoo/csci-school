## temperature.py
## Convert F to C in a graphical window.
## Chad Hobbs

from math import *
from graphics import *


def main():
    win = GraphWin("Temperature Converter",400,400)
    win.setCoords(0.0, 0.0, 3.0, 4.0)

    # Create graphical window
    Text(Point(1,3), "   Fahrenheit Temperature:").draw(win)
    Text(Point(1,1), "   Celsius Temperature:").draw(win)
    tmp = Entry(Point(2,3), 5)
    tmp.setText("0.0")
    tmp.draw(win)
    output = Text(Point(2,1),"")
    output.draw(win)
    button = Text(Point(1.5,2.0),"Convert!")
    Rectangle(Point(1.2,1.7), Point(1.8,2.3)).draw(win)
    button.draw(win)

    # Get mouseclick and convert
    win.getMouse()

    F = eval(tmp.getText())
    C = round((5.0/9.0 * (F - 32)),2)

    # Display conversion and update button
    output.setText(C)
    button.setText("Quit")

    # Get mouseclick and quit
    win.getMouse()
    win.close()

main()

