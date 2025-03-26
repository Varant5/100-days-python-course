from turtle import Turtle

class Ball(Turtle):
    def __init__(self, speed):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.move_y = 10
        self.move_x = 10
        self.movement_speed = speed

    def move(self):
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(new_x, new_y)

    def bounce_wall(self):
        self.move_y *= -1
        self.movement_speed *= 0.95

    def bounce_paddle(self):
        self.move_x *= -1
        self.movement_speed *= 0.95

    def reset_ball(self, speed):
        self.move_x *= -1
        self.movement_speed = speed
        self.goto(0,0)