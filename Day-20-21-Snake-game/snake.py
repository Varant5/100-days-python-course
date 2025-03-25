from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.starting_position = [(0, 0), (-20, 0), (-40, 0)]
        self.__make_snake()
        self.head = self.segments[0]

    def __make_snake(self):
        for position in self.starting_position:
            self.add_segment(position)

    def add_segment(self, position):
        new_segments = Turtle(shape="square")
        new_segments.color("white")
        new_segments.penup()
        new_segments.width(20)
        new_segments.goto(position)
        self.segments.append(new_segments)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment - 1].xcor()
            new_y = self.segments[segment - 1].ycor()
            self.segments[segment].goto(new_x,new_y)
        self.head.forward(20)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)