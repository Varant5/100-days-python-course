import turtle
import pandas

data = pandas.read_csv("50_states.csv")

def correct_turtle(name):
    state = turtle.Turtle()
    state.penup()
    state.color("black")
    state.hideturtle()
    new_x = data.loc[data["state"] == name, "x"].tolist()
    new_y = data.loc[data["state"] == name, "y"].tolist()
    state.goto(new_x[0], new_y[0])
    state.write(name)

point = 0
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

states = data["state"].tolist()
correct_answer = []

turtle.shape(image)

while len(correct_answer) < 50:
    answer_state = screen.textinput(title=f"{point}/50 States correct", prompt="What's another state's name? ")
    if answer_state == "quit":
        missing_states = []

        for s in states:
            if s not in correct_answer:
                missing_states.append(s)

        df = pandas.DataFrame(missing_states)
        df.to_csv("test.csv")
        break

    if answer_state.title() in states:
        correct_answer.append(answer_state.title())
        correct_turtle(answer_state.title())
        states.remove(answer_state.title())
        point += 1

