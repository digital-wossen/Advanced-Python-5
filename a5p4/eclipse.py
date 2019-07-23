# JTSK-350112
# a5 4.py
# Wossen Hailemariam
# w.hailemariam@jacobs-university.de


from graphics import *
import datetime
from datetime import datetime 

def main():
    win = GraphWin("eclipse",700,700)
    date_format = "%m/%d/%Y"

    d0 = datetime.strptime('8/18/2008', date_format)
    d1 = datetime.datetime.now()
    delta =  d1 - d0
    days = Text(Point(340,340),"the date that passed:") 
    days.draw(win)
 

    if win.getMouse():
        win.close()

main()