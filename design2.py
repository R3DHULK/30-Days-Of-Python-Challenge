import turtle
import colorsys

t = turtle.Turtle()
turtle.Screen().bgcolor("Black")
t.pensize(2)
t.speed(10)
n = 36
h = 0
for i in range(60):
    c = colorsys.hsv_to_rgb(h, 1, 0.9)
    h += 1/n
    t.pencolor(c)
    t.forward(i*4)
    t.left(100)
    t.forward(i*3 - 20)
    t.left(200)
turtle.done()