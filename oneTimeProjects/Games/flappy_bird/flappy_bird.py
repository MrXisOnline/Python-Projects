import turtle
from turtle import Turtle, Screen
from bars import Bar
from bird import Bird
import time

screen = Screen()
screen.listen()
screen.tracer(0)


bird = Bird()
bar = Bar()
start = time.time()
bar_start = time.time()
screen.onkey(bird.jump, "w")
screen.onkey(bird.down, "s")
while True:
	if time.time()-start > 0.1:
		bar.pass_bar()
		if bird.player.ycor() > -200:
			bird.player.setposition(bird.player.xcor(), bird.player.ycor()-3)
		start = time.time()
	elif bird.player.ycor() <= -200:
		break
	elif time.time()-bar_start > 2:
		bar.make_vertical_bar()
		bar_start = time.time()
	elif bar.check_bar_collision(bird):
		break
	screen.update()
screen.exitonclick()