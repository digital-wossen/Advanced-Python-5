# JTSK-350112
# a5_2.py
# Wossen Hailemariam
# w.hailemariam@jacobs-university.de

import time
import random
from graphics import *



d = int(input())
number_points = int(input())
    

if d > 1000 or number_points > 10000000:
    win = GraphWin("Approximate Pi", 500, 500)
    message = Text(Point(240, 240), "Value - More than VALID")
    message.draw(win)

    if win.getMouse():
        win.close()


else:
        
    win = GraphWin("Approximate Pi", d, d)
    start = time.time()
    all_points = 0
    inside_circle = 0

    for i in range(number_points):
        x = random.randrange(d)
        y = random.randrange(d)
        if(x - (d/2))**2 +(y - (d/2))**2 <= (d**2)/4:
            win.plotPixel(x, y, 'red')
            inside_circle += 1
            all_points += 1
        else:
            win.plotPixel(x, y, 'blue')
            all_points += 1
        if (i+1) % 100 == 0:
            print((inside_circle / all_points) * 4)

    win.plotPixel(d/2, d/2, "black")
    stop = time.time()
    win.getMouse()
    win.close()