# JTSK-350112
# a5 3.py
# Wossen Hailemariam
# w.hailemariam@jacobs-university.de


from graphics import *
import random

def main():
    win = GraphWin("Coloring Pixels",255,255)
    for i in range(255):
     a = random.randrange(255)
     b = random.randrange(255)
         x = i
         z = 40
         for i in range(255):
             y = i
    win.plotPixelFast(a, b, color_rgb(x,y,z))

    if win.getMouse():
        win.close()

main()