import turtle

import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states_names = data["state"]
states_list = states_names.to_list()

guessed_states = []


while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="What's a states name?",
    ).title()
    if answer_state == "Exit":
        states_missed = []
        for state in states_list:
            if state not in guessed_states:
                states_missed.append(state)
        break
    if answer_state in states_list:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())

missing_states = {"Missed States": states_missed}
df = pandas.DataFrame(missing_states)
df.to_csv("States missed")
