from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Score
import turtle
import random
import time


# def up():
# 	mySnake.up()

# def down():
# 	mySnake.down()

# def left():
# 	mySnake.left()

# def right():
# 	mySnake.right()

screen = Screen()
screen.listen()
screen.title("Snake-Arena")
screen.setup(width=640,height=640)
screen.bgcolor("black")
screen.tracer(0)
mySnake = Snake()
screen.onkey(mySnake.up, "Up")
screen.onkey(mySnake.down, "Down")
screen.onkey(mySnake.left, "Left")
screen.onkey(mySnake.right, "Right")
f = Food()
screen.update()
score = 0
b_score = Score(score)
run = True
while run:
	if mySnake.check_food(f.n_pos):
		score += 1
		b_score.update_score(score)
		f.respawn()
	else:
		screen.update()
		time.sleep(0.2)
		mySnake.move()
		if mySnake.check_wall():
			run = False
			b_score.game_over()
		head = mySnake.tur[0]
		for t in mySnake.tur[1:]:
			if head.distance(t) < 10 :
				b_score.game_over()

screen.exitonclick()