from turtle import Turtle, Screen, colormode
import heroes
import villains
import random

timmy = Turtle()
timmy.color("cyan3")

def random_color():
    levels = range(32,256,32)
    return tuple(random.choice(levels) for _ in range(3))

def set_color():
    tup = random_color()
    colormode(255)
    timmy.pencolor(tup)

# square
def square():
    for _ in range(4):
        timmy.forward(100)
        timmy.right(90)

def diff_shapes(num):
    set_color()
    for _ in range(num):
        timmy.forward(50)
        timmy.right(360/num)
        pass

# def dashed_line():
#     for _ in range(10):
#         timmy.pendown()
#         timmy.forward(10)
#         timmy.penup()
#         timmy.forward(10)

#square()

def random_walk():
    while True:
        set_color()
        direction = [0, 90, 180, 270]
        timmy.setheading(random.choice(direction))
        timmy.forward(50)

def draw_circle():
    timmy.circle(150)

# for i in range(3,11):
#     diff_shapes(i)
timmy.speed(11)

for _ in range(51):
    set_color()
    draw_circle()
    timmy.left(360/50)

# timmy.width(5)
# timmy.speed(7)
# random_walk()



screen = Screen()
screen.exitonclick()