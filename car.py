from graphics import *
from arc import *

win = GraphWin("car", 500, 500)


poly1 = Polygon(Point(50, 200), Point(80, 195), Point(100, 170), Point(200, 170), Point(220, 195), Point(280, 210),
                Point(280, 230), Point(50, 230))
poly1.setFill('red')
poly1.draw(win)

pt1 = Point(50, 80)
line = Line(Point(50, 200), pt1)
line.draw(win)

bal = Circle(pt1, 15)
bal.setFill('yellow')
bal.draw(win)


poly2 = Polygon(Point(200, 175), Point(215, 195), Point(150, 195), Point(150, 175))
poly2.setFill('blue')
poly2.draw(win)

poly3 = Polygon(Point(90, 195), Point(105, 175), Point(140, 175), Point(140, 195))
poly3.setFill('blue')
poly3.draw(win)

cir1 = Circle(Point(220, 230), 15)
cir1.setFill('black')
cir1.draw(win)

cir1w = Circle(Point(220, 230), 10)
cir1w.setFill('grey')
cir1w.draw(win)

cir2 = Circle(Point(90, 230), 15)
cir2.setFill('black')
cir2.draw(win)

cir2w = Circle(Point(90, 230), 10)
cir2w.setFill('grey')
cir2w.draw(win)


for i in range(20):
    poly1.move(5, 0)
    poly2.move(5, 0)
    poly3.move(5, 0)
    cir1.move(5, 0)
    cir1w.move(5, 0)
    cir2.move(5, 0)
    cir2w.move(5, 0)
    line.move(5, 0)
    bal.move(5, 0)
    time.sleep(0.05)
for i in range(20):
    poly1.move(-5, 0)
    poly2.move(-5, 0)
    poly3.move(-5, 0)
    cir1.move(-5, 0)
    cir1w.move(-5, 0)
    cir2.move(-5, 0)
    cir2w.move(-5, 0)
    line.move(-5, 0)
    bal.move(-5, 0)
    time.sleep(0.05)

win.getMouse()
