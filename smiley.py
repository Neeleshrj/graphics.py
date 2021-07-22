from graphics import *
from arc import *
win = GraphWin("smiley", 500, 500)

pt = Point(250, 250)

cir = Circle(pt, 100)
cir.setOutline('black')
cir.setFill('yellow')

cir.draw(win)

eye1 = Point(200, 220)
cir2 = Circle(eye1, 30)
cir2.setFill('white')
cir2.draw(win)

eye2 = Point(300, 220)
cir3 = Circle(eye2, 30)
cir3.setFill('white')
cir3.draw(win)

eye1ball = Point(200, 220)
cir4 = Circle(eye1ball, 20)
cir4.setFill('black')
cir4.draw(win)

eye2ball = Point(300, 220)
cir5 = Circle(eye2ball, 20)
cir5.setFill('black')
cir5.draw(win)

arc = Arc(Point(220, 300), Point(280, 280), -180)
arc.setFill("red")
arc.draw(win)


win.getMouse()
