from graphics import *
win = GraphWin("jumping", 600, 600)


def moveall(shapelist, dx, dy):
    for shape in shapelist:
        shape.move(dx, dy)


def movelimbsup(lh, rh, lleg, rleg):

    lh.undraw()
    ptLH = Point(170, 160)
    lh = Line(Point(240, 200), ptLH)
    lh.draw(win)

    rh.undraw()
    ptRH = Point(310, 160)
    rh = Line(Point(240, 200), ptRH)
    rh.draw(win)

    lleg.undraw()
    ptLL = Point(170, 210)
    lleg = Line(Point(240, 250), ptLL)
    lleg.draw(win)

    rleg.undraw()
    ptRL = Point(310, 210)
    rleg = Line(Point(240, 250), ptRL)
    rleg.draw(win)

    shapelist = [lh, rh, rleg, lleg]
    return shapelist


def movelimbsdown(lh, rh, lleg, rleg):
    lh.undraw()
    ptLH = Point(310, 440)
    lh = Line(Point(380, 400), ptLH)
    lh.draw(win)

    rh.undraw()
    ptRH = Point(450, 440)
    rh = Line(Point(380, 400), ptRH)
    rh.draw(win)

    lleg.undraw()
    ptLL = Point(310, 490)
    lleg = Line(Point(380, 450), ptLL)
    lleg.draw(win)

    rleg.undraw()
    ptRL = Point(450, 490)
    rleg = Line(Point(380, 450), ptRL)
    rleg.draw(win)

    shapelist = [lh, rh, rleg, lleg]
    return shapelist


def main():
    pt = Point(100, 300)
    cir1 = Circle(pt, 50)
    cir1.setFill('grey')

    pt2 = Point(100, 350)
    pt3 = Point(100, 450)
    line = Line(pt2, pt3)

    ptLL = Point(30, 450)
    lleg = Line(pt3, ptLL)
    lleg.draw(win)

    ptRL = Point(170, 450)
    rleg = Line(pt3, ptRL)
    rleg.draw(win)

    ptLH = Point(30, 400)
    lh = Line(Point(100, 400), ptLH)
    lh.draw(win)

    ptRH = Point(170, 400)
    rh = Line(Point(100, 400), ptRH)
    rh.draw(win)

    line.draw(win)
    cir1.draw(win)
    shapelist = [line, cir1, lh, rh, rleg, lleg]

    for i in range(20):
        moveall(shapelist, 7, -10)
        time.sleep(0.08)

    limbs = movelimbsup(lh, rh, lleg, rleg)
    shapelist = shapelist+limbs
    print(shapelist)
    for i in range(20):
        moveall(shapelist, 7, 10)
        time.sleep(0.08)

    for shape in limbs:
        shape.undraw()
    movelimbsdown(lh, rh, lleg, rleg)
    win.getMouse()


main()
