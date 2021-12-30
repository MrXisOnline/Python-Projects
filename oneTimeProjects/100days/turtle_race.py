from turtle import Turtle, Screen
import random

red = Turtle()
blue = Turtle()
green = Turtle()
yellow = Turtle()
orange = Turtle()
purple = Turtle()
color_list = ["red", "blue", "green", "yellow", "orange", "purple"]
color_in = 0
turtle_list = [red, blue, green, yellow, orange, purple]
screen = Screen()
player = screen.textinput("NIP","Name of the player:")
y = 0
for e in turtle_list:
	e.shape("turtle")
	e.color(color_list[color_in])
	e.penup()
	e.setposition(-280, -150 + y)
	color_in += 1
	y += 50

turtle_turn = 0
run = True
while run:
	if turtle_turn >= 6:
		turtle_turn = 0
	forward_length = random.randint(10,20)
	turtle_list[turtle_turn].forward(forward_length)
	pos = turtle_list[turtle_turn].position()
	if int(pos[0]) > 300:
		run = False
	else:
		turtle_turn += 1
win = color_list[turtle_turn]
if player == win:
	print(f"You Win! Winner is {win}")
else:
	print(f"You Lose! Winner is {win}")

screen.exitonclick()