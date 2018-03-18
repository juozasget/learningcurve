# Problem_1: Overlapping rectangles

#Solution: 2 Rectangles do not overlap if:
#    bot2 is above top2 OR top2 is below bot1
#    OR
#    left2 > right1 OR right2 < left1

from graphics import *
print('Size of the window canvas is 1000x1000')
print('Coordinate imputs will be multiplied x10 for representation')
print('Enter the coordinates of L (TOP LEFT POINT) and R(BOTTOM RIGHT) for rectangles 1 and 2')
# First Rectangle
lx1,ly1 = map(int,input("L1 (BLUE) coordinates: (x,y) ").split(','))
rx1,ry1 = map(int,input("R1 (BLUE) coordinates: (x,y) ").split(','))
# Second Rectangle
lx2,ly2 = map(int,input("L2 (RED) coordinates: (x,y) ").split(','))
rx2,ry2 = map(int,input("R2 (RED) coordinates: (x,y) ").split(','))
# Logic
if ry2 >= ly1 or ly2 <= ry1 or lx2 >= rx1 or rx2 <= lx1:
    print("Rectangles don't overlap")
    answer = "Rectangles don't overlap"
else:
    print('Rectangles overlap')
    answer = 'Rectangles overlap'
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
    label = Text(Point(440, 970), answer)
    rect2.draw(win) #Note:Y axis is inverted
    rect1.draw(win)
    label.draw(win)
    win.getMouse()
    win.close()
main()
