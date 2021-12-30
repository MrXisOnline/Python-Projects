from turtle import Screen
from state import State
from state_data import Data

screen = Screen()
screen.bgpic("stateimage.gif")
screen.title("US-States")
screen.setup(740, 550)
screen.tracer(0)
state_writer = State()
data = Data()
run = True
while data.cor_state < 50:
	screen.update()
	state = screen.textinput(f"{data.cor_state}/50 States Correct", "Name of State:")
	if state == "exit":
		break
		data.append_gamedata()
	elif data.check_state(state):
		pos = data.give_position(state)
		state_writer.writer(state, pos)
else:
	print("Hey You got all the names")
screen.exitonclick()