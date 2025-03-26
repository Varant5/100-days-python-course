import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()

screen.listen()
screen.onkey(turtle.move, "Up")

car = CarManager()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    car.create_car()
    car.move_cars()

    #Detect collision with car
    for single_car in car.all_cars:
        if turtle.distance(single_car) < 40 and abs(turtle.ycor() - single_car.ycor()) < 20:
            scoreboard.game_over()
            game_is_on = False

    #Detect end
    if turtle.ycor() > 260:
        scoreboard.level_up()
        turtle.finish_line()
        car.increase_speed()

    time.sleep(0.1)
    screen.update()

screen.exitonclick()