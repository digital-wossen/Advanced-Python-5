import time
from graphics import *

win = GraphWin("plotPixelFast vs. plotPixel", 300, 300)
message = Text(Point(150, 280), "Click for first pixel")
message.draw(win)
win.getMouse()
start1 = time.time()
for i in range(1000):
    win.plotPixel(50, 50, 'blue')
stop1 = time.time()
print(stop1 - start1)
message.setText("Click for second pixel.")
win.getMouse()
start2 = time.time()
for i in range(1000):
    win.plotPixel(100, 100, 'red')
stop2 = time.time()
print(stop2 - start2)
message.setText("Click for exit.")
win.getMouse()
win.close()