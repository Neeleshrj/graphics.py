from graphics import *
win = GraphWin("missile", 500, 500)

poly1 = Polygon(Point(200, 50), Point(180, 150), Point(120, 180), Point(180, 180), Point(180, 400), Point(120, 430),
                Point(180, 430), Point(200, 430), Point(280, 430), Point(220, 400), Point(220, 180), Point(280, 180),
                Point(220, 150))
poly1.setFill('grey')
poly1.draw(win)

win.getMouse()