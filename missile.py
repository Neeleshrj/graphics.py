from graphics import *
win = GraphWin("missile", 500, 500)

poly1 = Polygon(Point(200, 50), Point(180, 150), Point(220, 150))
poly1.setFill('grey')
poly1.draw(win)

poly2 = Polygon(Point(180, 150), Point(180, 400), Point(220, 400), Point(220, 150))
poly2.setFill('white')
poly2.draw(win)

poly3 = Polygon(Point(180, 150), Point(120, 180), Point(180, 180))
poly3.setFill('yellow')
poly3.draw(win)

poly4 = Polygon(Point(220, 150), Point(280, 180), Point(220, 180))
poly4.setFill('yellow')
poly4.draw(win)

poly5 = Polygon(Point(180, 400), Point(120, 430), Point(180, 430))
poly5.setFill('grey')
poly5.draw(win)


win.getMouse()