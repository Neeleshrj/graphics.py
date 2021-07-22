from graphics import *
from arc import *
win = GraphWin("flag", 600, 600)

pt1 = Point(280, 100)
pt2 = Point(500, 150)

rect = Rectangle(pt1, pt2)
rect.setFill('orange')
rect.draw(win)

pt3 = Point(280, 150)
pt4 = Point(500, 200)
rect = Rectangle(pt3, pt4)
rect.setFill('white')
rect.draw(win)

pt5 = Point(280, 200)
pt6 = Point(500, 250)
rect = Rectangle(pt5, pt6)
rect.setFill('green')
rect.draw(win)

cen = Point(390, 175)
cir = Circle(cen, 20)
cir.draw(win)
cir.setOutline('black')
cir.setFill('blue')


flagpt1 = Point(260, 100)
flagpt2 = Point(280, 500)
rect = Rectangle(flagpt1, flagpt2)
rect.setFill('silver')
rect.draw(win)

win.getMouse()


