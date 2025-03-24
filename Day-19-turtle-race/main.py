from turtle import Turtle, Screen
import random as r

screen = Screen()
width = 500
height = 400
starting_position = -60
screen.setup(width=width,height=height)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? ").lower()
colors = ["red", "green", "pink", "blue", "yellow"]

for turtle_index in range(len(colors)):
    turtle = Turtle(shape="turtle")
    turtle.penup()
    turtle.color(colors[turtle_index])
    turtle.goto(x=-(width/2 - 20), y=starting_position)
    starting_position += 30

still_racing = True

while still_racing:
    for turtle in screen.turtles():
        turtle.forward(r.randint(0,11))
        if turtle.position()[0] >= 250:
            winner = turtle.color()
            still_racing = False
            break

if user_bet == winner[0]:
    print(f"You win! {winner[0].title()} turtle won race!")
else:
    print(f"You lose! :( {winner[0].title()} turtle won race!")

screen.exitonclick()