from graphics import *
win = GraphWin("DDA", 500, 500)


def draw(x, y, x_center, y_center):
    pt1 = Point(x + x_center, y + y_center)
    pt1.setFill('blue')
    pt1.draw(win)
    pt1 = Point(-x + x_center, y + y_center)
    pt1.setFill('blue')
    pt1.draw(win)
    pt1 = Point(x + x_center, -y + y_center)
    pt1.setFill('blue')
    pt1.draw(win)
    pt1 = Point(-x + x_center, -y + y_center)
    pt1.setFill('blue')
    pt1.draw(win)
    pt1 = Point(y + x_center, x + y_center)
    pt1.setFill('blue')
    pt1.draw(win)
    pt1 = Point(-y + x_center, x + y_center)
    pt1.setFill('blue')
    pt1.draw(win)
    pt1 = Point(y + x_center, -x + y_center)
    pt1.setFill('blue')
    pt1.draw(win)
    pt1 = Point(-y + x_center, -x + y_center)
    pt1.setFill('blue')
    pt1.draw(win)


def circledraw(x_center, y_center, r):
    x=0
    y=r

    draw(x, y, x_center, y_center)


    p=1-r

    while x < y:
        x+=1
        if p<0:
            p+=2*x+1
        else:
            y-=1
            p+=2*(x-y)+1
        draw(x, y, x_center, y_center)


def main():
    circledraw(100, 100, 30)
    circledraw(100, 100, 60)
    circledraw(100, 100, 80)
    win.getMouse()

main()