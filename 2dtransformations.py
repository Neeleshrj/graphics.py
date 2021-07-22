from graphics import *
import math

win = GraphWin("transformations", 600, 600)


def translation(xt, yt, ptarr):
    print(ptarr)
    for i in range(len(ptarr)):
        new_x = ptarr[i].getX() + xt
        new_y = ptarr[i].getY() + yt
        ptarr[i] = Point(new_x, new_y)

    print(ptarr)
    new_poly = Polygon(ptarr)
    new_poly.setFill('green')
    new_poly.setOutline('black')
    new_poly.draw(win)

    win.getMouse()


def rotation(theta, ptarr):

    theta = math.radians(theta)
    cosang, sinang = math.cos(theta), math.sin(theta)

    points = ptarr
    n = len(points)
    cx = sum(p.getX() for p in points) / n
    cy = sum(p.getY() for p in points) / n

    new_points = []
    for p in points:
        x, y = p.getX(), p.getY()
        tx, ty = x-cx, y-cy
        new_x = ( tx*cosang + ty*sinang) + cx
        new_y = (-tx*sinang + ty*cosang) + cy
        new_points.append(Point(new_x, new_y))
        new_poly = Polygon(new_points)
        new_poly.setFill('green')
        new_poly.setOutline('black')
        new_poly.draw(win)

    win.getMouse()


def scale(sx, sy, ptarr):
    new_points = []
    for i in range(len(ptarr)):
        x_new = ptarr[i].getX() * sx
        y_new = ptarr[i].getY() * sy
        new_points.append(Point(x_new, y_new))
    print(new_points)
    new_poly = Polygon(new_points)
    new_poly.setFill('green')
    new_poly.setOutline('black')
    new_poly.draw(win)
    win.getMouse()


def main():

    x1 = 100
    y1 = 250
    x2 = 200
    y2 = 250
    x3 = 220
    y3 = 180
    x4 = 80
    y4 = 220
    pt1 = Point(x1, y1)
    pt2 = Point(x2, y2)
    pt3 = Point(x3, y3)
    pt4 = Point(x4, y4)
    ptarr = [pt1, pt2, pt3, pt4]

    poly1 = Polygon(pt1, pt2, pt3, pt4)
    poly1.setFill('blue')
    poly1.setOutline('red')
    poly1.draw(win)
    win.getMouse()

    print('Enter 1 for translation, 2 for rotation, 3 for scaling')
    x = int(input())
    if x == 1:
        print("Enter x-offset for moving the points")
        xt = int(input())
        print("Enter y-offset for moving the points")
        yt = int(input())
        translation(xt, yt, ptarr)
    elif x == 2:
        print("Enter angle of rotation")
        theta = int(input())
        rotation(theta, ptarr)
    elif x == 3:
        print("Enter scaling factor of x")
        Sx = int(input())
        print("Enter scaling factor of y")
        Sy = int(input())
        scale(Sx, Sy, ptarr)


main()