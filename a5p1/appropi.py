# JTSK-350112
# a5_1.py
# Wossen Hailemariam
# w.hailemariam@jacobs-university.de

import time
import random
from graphics import *

d = 477
win = GraphWin("Approximate Pi", d, d)
start = time.time()
all_points = 0
inside_circle = 0

for i in range(10000):
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