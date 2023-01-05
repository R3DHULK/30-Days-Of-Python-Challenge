import turtle
import math

hulk= turtle.Turtle()
hulk.speed(500)

window = turtle.Screen()
window.bgcolor("#000000")
hulk.color("yellow")

avenger = 20

hulk.left(90)
hulk.penup()
hulk.goto(-7 * avenger, 0)
hulk.pendown()

for a in range(-7 * avenger, -3 * avenger, 1):
    x = a / avenger
    rel = math.fabs(x)
    y = 1.5 * math.sqrt((-math.fabs(rel - 1)) * math.fabs(3 - rel) / ((rel - 1) * (3 - rel))) * (
                1 + math.fabs(rel - 3) / (rel - 3)) * math.sqrt(1 - (x / 7) ** 2) + (
                    4.5 + 0.75 * (math.fabs(x - 0.5) + math.fabs(x + 0.5)) - 2.75 * (
                        math.fabs(x - 0.75) + math.fabs(x + 0.75))) * (1 + math.fabs(1 - rel) / (1 - rel))
    hulk.goto(a, y * avenger)

for a in range(-3 * avenger, -1 * avenger - 1, 1):
    x = a / avenger
    rel = math.fabs(x)
    y = (2.71052 + 1.5 - 0.5 * rel - 1.35526 * math.sqrt(4 - (rel - 1) ** 2)) * math.sqrt(
        math.fabs(rel - 1) / (rel - 1))
    hulk.goto(a, y * avenger)

hulk.goto(-1 * avenger, 3 * avenger)
hulk.goto(int(-0.5 * avenger), int(2.2 * avenger))
hulk.goto(int(0.5 * avenger), int(2.2 * avenger))
hulk.goto(1 * avenger, 3 * avenger)
print("Batman Logo with Python Turtle")
for a in range(1 * avenger + 1, 3 * avenger + 1, 1):
    x = a / avenger
    rel = math.fabs(x)
    y = (2.71052 + 1.5 - 0.5 * rel - 1.35526 * math.sqrt(4 - (rel - 1) ** 2)) * math.sqrt(
        math.fabs(rel - 1) / (rel - 1))
    hulk.goto(a, y * avenger)

for a in range(3 * avenger + 1, 7 * avenger + 1, 1):
    x = a / avenger
    rel = math.fabs(x)
    y = 1.5 * math.sqrt((-math.fabs(rel - 1)) * math.fabs(3 - rel) / ((rel - 1) * (3 - rel))) * (
                1 + math.fabs(rel - 3) / (rel - 3)) * math.sqrt(1 - (x / 7) ** 2) + (
                    4.5 + 0.75 * (math.fabs(x - 0.5) + math.fabs(x + 0.5)) - 2.75 * (
                        math.fabs(x - 0.75) + math.fabs(x + 0.75))) * (1 + math.fabs(1 - rel) / (1 - rel))
    hulk.goto(a, y * avenger)

for a in range(7 * avenger, 4 * avenger, -1):
    x = a / avenger
    rel = math.fabs(x)
    y = (-3) * math.sqrt(1 - (x / 7) ** 2) * math.sqrt(math.fabs(rel - 4) / (rel - 4))
    hulk.goto(a, y * avenger)

for a in range(4 * avenger, -4 * avenger, -1):
    x = a / avenger
    rel = math.fabs(x)
    y = math.fabs(x / 2) - 0.0913722 * x ** 2 - 3 + math.sqrt(1 - (math.fabs(rel - 2) - 1) ** 2)
    hulk.goto(a, y * avenger)

for a in range(-4 * avenger - 1, -7 * avenger - 1, -1):
    x = a / avenger
    rel = math.fabs(x)
    y = (-3) * math.sqrt(1 - (x / 7) ** 2) * math.sqrt(math.fabs(rel - 4) / (rel - 4))
    hulk.goto(a, y * avenger)

hulk.penup()
hulk.goto(300, 300)
turtle.done()