from turtle import Screen
from walls import Wall
from bars import Bar
from ball import Ball
from scoreboard import Writer

screen = Screen()
screen.setup(width=450, height=500)
screen.tracer(0)
screen.listen()
wall = Wall()
bar = Bar()
ball = Ball()
writer = Writer()
score = 0
screen.title(f"Breaking-Out | Score : {score}")
screen.onkey(key="Left", fun=bar.move_left)
screen.onkey(key="Right", fun=bar.move_right)
screen.update()
while True:
	ball.move_ball()
	ball.bar_collision(bar)
	ball_pos = ball.b.position()
	if wall.ball_collision(ball_pos):
		ball.ball_block_collision()
		score += 1
		screen.title(f"Breaking-Out | Score : {score}")
	check_win = wall.win()
	if check_win == "win":
		writer.win()
		break
	check = ball.ball_wall_collision()
	if check == False:
		writer.game_over()
		break
	screen.update()
screen.update()
screen.exitonclick()