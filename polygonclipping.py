from graphics import *

win = GraphWin("PolygonClipping", 500, 500)


def x_intersect(x1, y1, x2, y2, x3, y3, x4, y4):
    num = (x1*y2 - y1*x2) * (x3-x4) - (x1-x2) * (x3*y4 - y3*x4)
    den = (x1-x2) * (y3-y4) - (y1-y2) * (x3-x4)
    return (num/den)


def y_intersect(x1, y1, x2, y2, x3, y3, x4, y4):
    num = (x1*y2 - y1*x2) * (y3-y4) - (y1-y2) * (x3*y4 - y3*x4)
    den = (x1-x2) * (y3-y4) - (y1-y2) * (x3-x4)
    return (num/den)


def clip(poly_points, poly_size, x1, y1, x2, y2):
    new_points=[]
    print("start")
    print(new_points)
    print(poly_points)
    new_poly_size = 0
    for i in range(0, poly_size):
        k = (i+1) % poly_size
        ix = poly_points[i][0]
        iy = poly_points[i][1]
        kx = poly_points[k][0]
        ky = poly_points[k][1]

        i_pos = (x2-x1) * (iy-y1) - (y2-y1) * (ix-x1)

        k_pos = (x2-x1) * (ky-y1) - (y2-y1) * (kx-x1)

        if i_pos < 0 and k_pos < 0:
            new_points.append([kx, ky])
            new_poly_size += 1

        elif i_pos >=0 and k_pos < 0:
            new_points.append([x_intersect(x1, y1, x2, y2, ix, iy, kx, ky), y_intersect(x1, y1, x2, y2, ix, iy, kx, ky)])
            new_poly_size += 1

            new_points.append([kx, ky])
            new_poly_size += 1

        elif i_pos < 0 and k_pos >=0:
            new_points.append([x_intersect(x1, y1, x2, y2, ix, iy, kx, ky), y_intersect(x1, y1, x2, y2, ix, iy, kx, ky)])
            new_poly_size += 1

    if new_poly_size != 0:
        poly_size = new_poly_size
        poly_points.clear()
        for i in range(poly_size):
            poly_points.append([new_points[i][0], new_points[i][1]])
    print(poly_points)
    print("end of iteration")


def sutherlandclip(poly_points, poly_size, clipper_points, clipper_size):
    for i in range(0,clipper_size):
        k = (i+1) % clipper_size

        # pt1 = Point(clipper_points[i][0], clipper_points[i][1])
        # pt2 = Point(clipper_points[k][0], clipper_points[k][1])
        # line = Line(pt1, pt2)
        # line.setFill('red')
        # line.draw(win)
        # win.getMouse()

        clip(poly_points, poly_size, clipper_points[i][0], clipper_points[i][1],
             clipper_points[k][0], clipper_points[k][1])

    # print(poly_points)
    # for i in range(poly_size):
    #     k = (i + 1) % poly_size
    #
    #     ppt1 = Point(poly_points[i][0], poly_points[i][1])
    #     ppt2 = Point(poly_points[k][0], poly_points[k][1])
    #     line = Line(ppt1, ppt2)
    #     line.setFill('green')
    #     line.draw(win)
    #     win.getMouse()
    for i in range(0, poly_size):
        print(poly_points[i][0] + "," + poly_points[i][1])


def main():
    poly_size = 3
    poly_points = [[100, 150], [200, 250], [300, 200]]

    # for i in range(poly_size):
        # k = (i + 1) % poly_size
        # ppt1 = Point(poly_points[i][0], poly_points[i][1])
        # ppt2 = Point(poly_points[k][0], poly_points[k][1])
        # line = Line(ppt1, ppt2)
        # line.setFill('blue')
        # line.draw(win)
        # win.getMouse()

    clipper_size = 4

    clipper_points = [[150, 150], [150, 200], [200, 200], [200, 150]]

    sutherlandclip(poly_points, poly_size, clipper_points, clipper_size)

main()



