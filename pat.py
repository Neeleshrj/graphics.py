from graphics import *
win = GraphWin("Circle", 500, 500)


def draw1(x, y, x_center, y_center):
    pt1 = Point(-y + x_center, x + y_center)
    pt1.setFill('red')
    pt1.draw(win)
    pt1 = Point(-y + x_center, -x + y_center)
    pt1.setFill('red')
    pt1.draw(win)


def draw2(x, y, x_center, y_center):
    pt1 = Point(y + x_center, x + y_center)
    pt1.setFill('red')
    pt1.draw(win)
    pt1 = Point(y + x_center, -x + y_center)
    pt1.setFill('red')
    pt1.draw(win)



def circledraw(x_center, y_center, r):
    x=0
    y=r

    draw1(x, y, x_center, y_center)


    p=1-r

    while x < y:
        x+=1
        if p<0:
            p+=2*x+1
        else:
            y-=1
            p+=2*(x-y)+1
        draw1(x, y, x_center, y_center)


def circledraw2(x_center, y_center, r):
    x=0
    y=r

    draw2(x, y, x_center, y_center)


    p=1-r

    while x < y:
        x+=1
        if p<0:
            p+=2*x+1
        else:
            y-=1
            p+=2*(x-y)+1
        draw2(x, y, x_center, y_center)


def main():
    print('Enter center of Circle 1 X co-ordinate')
    x1 = int(input())
    print('Enter center of Circle 1 Y co-ordinate')
    y1 = int(input())
    print("Enter radius of circle")
    r = int(input())

    circledraw(x1, y1, r)
    circledraw2((x1//10)-((r//2)//10), y1, r)
    print((x1//10)-((r//2)//10))
    win.getMouse()

main()