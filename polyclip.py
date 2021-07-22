from graphics import *

win = GraphWin("PolygonClipping", 500, 500)


def weiler(x1, y1, x2, y2, xwmin, ywmin, xwmax, ywmax):
    p1 = -(x2-x1)
    q1 = x1-xwmin
    p2 = x2-x1
    q2 = xwmax-x1
    p3 = -(y2-y1)
    q3 = y1-ywmin
    p4 = y2-y1
    q4 = ywmax-y1

    tmin=0
    tmax=1

    parr = [p1, p2, p3, p4]
    qarr = [q1, q2, q3, q4]

    for i in range(4):
        if parr[i] == 0:

            if qarr[i]<0:
                line1 = Line(Point(x1, y1), Point(x2, y2))
                line1.setFill('white')
                line1.draw(win)
            if qarr[i]>=0:
                line1 = Line(Point(x1, y1), Point(x2, y2))
                line1.setFill('green')
                line1.draw(win)
        else:
            temp = qarr[i] / parr[i]
            if parr[i]<0:
                if tmin<=temp:
                    tmin=temp
            else:
                if tmax>temp:
                    tmax=temp

    if tmin < tmax:
        xx1 = x1+tmin*parr[1]
        xx2 = x1+tmax*parr[1]
        yy1 = y1+tmin*parr[3]
        yy2 = y1+tmax*parr[3]
        pt1 = Point(xx1, yy1)
        pt2 = Point(xx2, yy2)
        line = Line(pt1, pt2)
        line.setFill('green')
        line.draw(win)


def main():
    arr = [[202, 128], [266, 136], [299, 81], [334, 136], [395, 128], [364, 176], [395, 224],[333, 216], [300, 272],
            [262, 216], [203, 224], [232, 176]
            ]
    arr2 =[[219, 99], [376, 99], [376, 242], [219, 242]]

    for i in range(len(arr)):
        k = (i+1) % len(arr)
        ppt1 = Point(arr[i][0], arr[i][1])
        ppt2 = Point(arr[k][0], arr[k][1])
        line = Line(ppt1, ppt2)
        line.setFill('blue')
        line.draw(win)
        win.getMouse()

    for i in range(len(arr2)):
        k = (i+1) % len(arr2)
        ppt1 = Point(arr2[i][0], arr2[i][1])
        ppt2 = Point(arr2[k][0], arr2[k][1])
        line = Line(ppt1, ppt2)
        line.setFill('red')
        line.draw(win)
        win.getMouse()

    for i in range(len(arr)):
        k = (i+1) % len(arr)
        ix = arr[i][0]
        iy = arr[i][1]
        kx = arr[k][0]
        ky = arr[k][1]
        weiler(ix, iy, kx, ky, 219, 99, 376, 242)
        win.getMouse()



main()
