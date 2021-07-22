from graphics import *
win = GraphWin("DDA", 1000, 1000)


def midpoint(x1, y1, x2, y2):
    dx=x2-x1
    dy=y2-y1
    d=2*(dy-dx)
    incE=2*dy
    incNE=2*(dy-dx)
    x=x1
    y=y1
    pt1 = Point(x, y)
    pt1.setFill('red')
    pt1.draw(win)
    while x < x2:
        if d <=0:
            d+=incE
            x+=1
        else:
            d+=incNE
            x+=1
            y+=1
        pt2 = Point(x, y)
        pt2.setFill('blue')
        pt2.draw(win)


def main():

    midpoint(200, 200, 200, 400)
    midpoint(200, 200, 300, 300)
    midpoint(200, 200, 100, 100)

    win.getMouse()


main()

