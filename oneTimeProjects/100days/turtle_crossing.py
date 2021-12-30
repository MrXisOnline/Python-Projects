from turtle import Screen
from player import Player
from lane import Lane
from level import Level
import time

def car_collision():
	global runner
	for e in lane.lane:
		if player.p.distance(e) < 30:
			runner = False
			level.game_over()


screen = Screen()
screen.setup(800,600)
screen.listen()
screen.tracer(0)
lane = Lane()
player = Player()
level = Level()
runner = True
t = 0.3
screen.onkey(key="Up",fun=player.up)
while runner:
	if len(lane.lane) >= 100:
		lane.garbage_collection()
	lane.start_car()
	screen.update()
	car_collision()
	l = player.pass_level()
	if l == True:
		l = False
		level.level += 1
		level.update_level()
		t = round(t - 0.05, 2)
		player.p.setposition(0,-275)
		player.p.setheading(90)
	elif round(t, 2) == 0.0:
		l = False
		level.game_over()
	time.sleep(t)
screen.exitonclick()
