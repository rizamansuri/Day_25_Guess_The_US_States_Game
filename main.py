# BismillahirRahmanirRahim
import pandas as pd
import turtle

COUNT = 0

screen = turtle.Screen()
screen.title("Riza's Guess - U.S. States Game")
image = "blank_states_img.gif"
screen.addshape("blank_states_img.gif")
turtle.shape(image)

data = pd.read_csv("50_states.csv")
states = data.state.to_list()
states_guessed = []

while COUNT <= 50:
    # Keep track of count
    answer_text = screen.textinput(title=f"{COUNT}/50 States Correct", prompt="Enter another state's names?").title()
    if answer_text == "Exit":
        not_guessed = [state for state in states if state not in states_guessed]
        # for state in states:
        #     if state not in states_guessed:
        #         not_guessed.append(state)
        missing_states = pd.DataFrame(not_guessed)
        missing_states.to_csv("States_to_learn.csv")
        break
    # Check if the state exist
    if answer_text in states:
        COUNT += 1
        states_guessed.append(answer_text)
        state_data = data[data.state == answer_text]
        # Create turtle
        tim = turtle.Turtle()
        tim.penup()
        tim.hideturtle()
        tim.goto(int(state_data.x), int(state_data.y))
        tim.write(answer_text)





