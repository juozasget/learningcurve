# Problem_1: Overlapping rectangles //


#Solution: 2 Rectangles do not overlap if:
#    bot2 is above top2 OR top2 is below bot1
#    OR
#    left2 > right1 OR right2 < left1

from graphics import *
# Pirmas Staciakampis
lx1,ly1 = map(int,input("L1 koordinates: (x,y) ").split(','))
rx1,ry1 = map(int,input("R1 koordinates: (x,y) ").split(','))
# Antras Staciakampis
lx2,ly2 = map(int,input("L2 koordinates: (x,y) ").split(','))
rx2,ry2 = map(int,input("R2 koordinates: (x,y) ").split(','))
# Salygos tikrinimas
if ry2 > ly1 or ly2 < ry1 or lx2 > rx1 or rx2 < lx1:
    print('Nepersikloja')
else:
    print('Persikloja')
def t(x):
    return x * 10
def main ():
    win = GraphWin("Rectangle Problem", 1000, 1000)
    win.setBackground(color_rgb(223, 243, 253))
    rect1 = Rectangle(Point(t(lx1), t(ly1)), Point(t(rx1), t(ry1)))
    rect1.setOutline('black')
    rect1.setFill('blue')
    rect2 = Rectangle(Point(t(lx2), t(ly2)), Point(t(rx2), t(ry2)))
    rect2.setOutline('black')
    rect2.setFill('red')
    rect1.draw(win)
    rect2.draw(win)
    win.getMouse()
    win.close()
main()