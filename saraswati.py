import turtle
turtle.bgcolor("gold")
turtle.title("Durga")
def pos(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
#For Bindi
pos(0,200)
turtle.color("red")
turtle.begin_fill()
turtle.circle(40)
turtle.end_fill()

#for Left Eyebrow
pos(-30,200)
turtle.color("black")
turtle.begin_fill()
turtle.right(45)
for i in range(20):
    turtle.left(3)
    turtle.back(10)
for i in range(10):
    turtle.right(3)
    turtle.back(10)
turtle.right(18)
for i in range(13):
    turtle.left(3)
    turtle.forward(10)
for i in range(20):
    turtle.right(2)
    turtle.forward(10)
turtle.end_fill()


#For Right Eyebrow
turtle.left(80)
pos(30,200)
turtle.color("black")
turtle.begin_fill()
for i in range(20):
    turtle.right(3)
    turtle.forward(10)
for i in range(10):
    turtle.left(3)
    turtle.forward(10)
turtle.left(18)
for i in range(13):
    turtle.right(3)
    turtle. back(10)
for i in range(20):
    turtle. left(2)
    turtle. back(10)
turtle.end_fill()

#For Left Eye
pos(40,150)
turtle.pensize(15)
turtle.left(10)
for i in range(20):
    turtle.right(3)
    turtle. forward(10)
for i in range(10):
    turtle.left(3)
    turtle.forward(5)
turtle.right(3)
for i in range(10):
    turtle.left(3)
    turtle.back(5)
for i in range(20):
    turtle.right(3)
    turtle.back(10)
turtle.pensize(1)
pos(130,130)
turtle.begin_fill()
turtle.circle(40)
turtle.end_fill()
turtle.color("white")
turtle.begin_fill()
pos(115,175)
turtle. circle(10)
turtle. end_fill()


#For Right Eye
pos(-40,150)
turtle.color("black")
turtle.pensize(15)
turtle.right(25)
for i in range(20):
    turtle.left(3)
    turtle.back(10)
for i in range(10):
    turtle.right(3)
    turtle.back(5)
turtle.left(3)
for i in range(10):
    turtle.right(3)
    turtle.forward(5)
for i in range(20):
    turtle.left(3)
    turtle.forward(10)
turtle.pensize(1)
pos(-130,130)
turtle.begin_fill()
turtle.circle(40)
turtle.end_fill()
turtle.color("white")
turtle.begin_fill()
pos(-155,175)
turtle.circle(10)
turtle.end_fill()

#For Nose
turtle.color("black")
pos(-60,10)
turtle.right(70)
for i in range(5,12):
    turtle.pensize(i)
    turtle.left(7)
    turtle.forward(10)
for i in range(12,5,-1):
    turtle.pensize(i)
    turtle.left(7)
    turtle.forward(10)

#for Upper lip
turtle.begin_fill()
pos(-130,-90)
turtle.color("red")
turtle.pensize(1)
turtle.begin_fill()
turtle.right(60)
for i in range(3):
    turtle.left(3)
    turtle.forward(5)
for i in range(10):
    turtle.left(4)
    turtle.forward(6)
for i in range(10):
    turtle.right(10)
    turtle.forward(7)
turtle.left(135)
for i in range(10):
    turtle.right(10)
    turtle.forward(7)
turtle.right(2)
for i in range(10):
    turtle.left(4)
    turtle.forward(6)
for i in range(3):
    turtle.left(3)
    turtle.forward(5)
turtle.right(160)
for i in range(12):
    turtle.right(3)
    turtle.forward(7.2)
turtle.left(44)
for i in range(15):
    turtle.right(5.5)
    turtle. forward(7)
turtle.left(44)
for i in range(12):
    turtle.right(3)
    turtle.forward(7)
turtle.end_fill()

#For lower Lip
turtle.begin_fill()
turtle.left(175)
for i in range(14):
    turtle.left(2)
    turtle.forward(5)
turtle.right(45)
for i in range(14):
    turtle.left(7)
    turtle.forward(10)
turtle.right(45)
for i in range(14):
    turtle.left(3)
    turtle.forward(5)
turtle.right(185)
for i in range(7):
    turtle.left(3)
    turtle.forward(10)
turtle.right(.6)
for i in range(18):
    turtle.right(6)
    turtle.forward(10)
turtle.right(8)
for i in range(7):
    turtle.left(3)
    turtle.forward(10)
turtle.end_fill()
#For Nosering
turtle.pensize(12)
turtle.color("yellow")
pos(30,0)
turtle.left(120)
for i in range(47):
    turtle.right(7)
    turtle.back(10)
turtle.hideturtle()
turtle.exitonclick()
