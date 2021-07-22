from graphics import *
win = GraphWin("labfat", 600, 600)


def bres(x1, y1, x2, y2):
    x=x1
    y=y1
    dx=x2-x1
    dy=y2-y1
    p=(2*dx)-dy
    if dx==0:
        while y <= y2:
            pt1 = Point(x, y)
            pt1.setFill('blue')
            pt1.draw(win)
            y += 1
            if p < 0:
                p = p + 2 * dy
            else:
                p = p + (2 * dy) - (2 * dx)
                y += 1
    else:
        while x <= x2:
            pt1 = Point(x, y)
            pt1.setFill('blue')
            pt1.draw(win)
            x += 1
            if p < 0:
                p = p + 2 * dy
            else:
                p = p + (2 * dy) - (2 * dx)
                y += 1


def main():

    bres(200, 200, 200, 400)
    bres(200, 200, 300, 300)
    bres(200, 200, 100, 300)
    bres(100, 300, 300,300)
    bres(100, 200, 100, 400)
    bres(100, 400, 300, 400)
    bres(300, 400, 300, 200)
    bres(300, 200, 100, 200)

    win.getMouse()


main()

