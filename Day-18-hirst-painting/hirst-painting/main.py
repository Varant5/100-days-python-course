import colorgram
from turtle import Turtle, Screen, colormode
import random

# ex_colors = colorgram.extract('image.jpg', 30)
#
# colors = []
#
# for i in range(len(ex_colors)):
#     temp = []
#     temp.append(ex_colors[i].rgb.r)
#     temp.append(ex_colors[i].rgb.g)
#     temp.append(ex_colors[i].rgb.b)
#     colors.append(tuple(temp))

COLORS = [(249, 248, 243), (250, 245, 248), (243, 250, 246), (241, 246, 250), (234, 225, 83), (195, 8, 69), (231, 54, 132), (194, 164, 15), (112, 178, 214), (199, 77, 15), (216, 162, 101), (34, 187, 112), (29, 104, 167), (14, 23, 64), (20, 29, 168), (212, 136, 175), (231, 224, 7), (197, 34, 130), (15, 181, 210), (231, 167, 197), (126, 189, 163), (10, 48, 29), (40, 131, 75), (141, 217, 203), (61, 22, 10), (60, 13, 27), (108, 91, 210), (235, 64, 34), (131, 217, 230), (183, 17, 9)]

def draw_point():
    cursor.dot(20, random.choice(COLORS))

cursor = Turtle()
cursor.speed(11)
colormode(255)

cursor.hideturtle()
cursor.penup()
cursor.goto(-250, -200)

number_of_row = 11
number_of_columns = 11

for i in range(1, number_of_row):
    for j in range(1, number_of_columns):
        draw_point()
        cursor.forward(50)
    cursor.goto(-250, -200 + (i * 40))

screen = Screen()
screen.exitonclick()