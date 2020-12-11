import turtle
import pandas

screen = turtle.Screen()
image = "blank_states_img.gif"
screen.title("U.S. sate Quiz")

screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data["state"].tolist()
num_states = len(data.state)
guessed_states = 0
guessed_states_arr = []


def check_answer(answer):
    global guessed_states
    if answer in states:
        checked_answer = data[data["state"] == answer]
        guessed_states_arr.append(answer)
        xcor = int(checked_answer.x)
        ycor = int(checked_answer.y)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(xcor, ycor)
        t.write(answer)
        guessed_states += 1


while guessed_states < num_states:
    input_answer = screen.textinput(title=f"Guess the state{guessed_states}/50",
                                    prompt="What's another state name").title()
    if input_answer == "Exit":
        break
    check_answer(input_answer)

missed_states = []

for state in states:
    print(state)
    if state not in guessed_states_arr:
        missed_states.append(state)

missed_data = {"Missed States": missed_states}

df = pandas.DataFrame(missed_data)
df.to_csv("missed_states.csv")

screen.exitonclick()
