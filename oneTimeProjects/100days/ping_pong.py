from turtle import Turtle, Screen
from bars import Bar
from ball import Ball
from pongscore import Score
import time

screen = Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.listen()
screen.tracer(0)
score = Score()
bar1 = Bar(-380)
bar2 = Bar(380)
ball = Ball()
screen.update()
screen.onkey(key="w", fun=bar1.move_up)
screen.onkey(key="s", fun=bar1.move_down)
screen.onkey(key="Up", fun=bar2.move_up)
screen.onkey(key="Down", fun=bar2.move_down)

while ball.run:
	ball.move_ball()
	time.sleep(0.1)
	screen.update()
	g = ball.ball_wall_collision()
	if g == False:
		score.game_over()
	s = ball.bar_collision(bar1,bar2)
	if s == "r":
		l = score.score_l
		r = score.score_r
		score.prep(l,r+1)
	elif s == "l":
		l = score.score_l
		r = score.score_r
		score.prep(l+1,r)

screen.exitonclick()
