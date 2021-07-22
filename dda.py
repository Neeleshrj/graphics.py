from graphics import *
win = GraphWin("breshnam", 500, 500)


def dda(x1, y1, x2, y2):
    dx = x2-x1
    dy = y2-y1
    n = max(abs(dx), abs(dy))
    dt = n
    dxdt = dx//dt
    dydt = dy//dt
    x = x1
    y = y1
    while n != 0:
        pt1 = Point(round(x), round(y))
        pt1.setFill('blue')
        pt1.draw(win)
        n = n - 1
        x = x + dxdt
        y = y + dydt


def main():
    #all values multiplied by 10 for better visibility
    dda(200, 200, 200, 400)
    dda(200, 200, 300, 300)
    dda(200, 200, 100, 300)
    dda(100, 300, 300,300)
    dda(100, 200, 100, 400)
    dda(100, 400, 300, 400)
    dda(300, 400, 300, 200)
    dda(300, 200, 100, 200)

    win.getMouse()


main()
