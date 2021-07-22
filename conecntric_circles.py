from graphics import *

win = GraphWin("cc", 500, 500)

pt1 = Point(250,250)

cir1 = Circle(pt1, 10)
cir2 = Circle(pt1, 30)
cir3 = Circle(pt1, 50)

cir1.setFill('blue')
cir2.setFill('white')
cir3.setFill('red')

cir3.draw(win)
cir2.draw(win)
cir1.draw(win)

for i in range(20):
    cir1.move(5, 0)
    cir2.move(5, 0)
    cir3.move(5, 0)
    time.sleep(0.05)
for i in range(20):
    cir1.move(-5, 0)
    cir2.move(-5, 0)
    cir3.move(-5, 0)
    time.sleep(0.05)
    
win.getMouse()
