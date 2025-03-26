from turtle import Turtle
import random as r

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.level_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        if r.randint(1,6) == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(1, 3)
            new_car.color(r.choice(COLORS))
            new_car.goto(320, r.randint(-250, 251))
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.level_speed)

    def increase_speed(self):
        self.level_speed += MOVE_INCREMENT

