from turtle import Screen
import turtle
from ships import Ship
from barrier import Barrier
from player import PlayerShip
from player_bullet import PBullet
from oppenent_bullet import OBullet

score = 0
row = 2
def main():
	global score
	global row
	p_life = 3
	screen = Screen()
	screen.setup(500,500)
	screen.title(f"Space Invader | Score : {score} | Life: {p_life}")
	screen.bgcolor("black")
	screen.tracer(0)
	screen.listen()
	opp_ships = Ship(row)
	obt = OBullet(opp_ships)
	barrier = Barrier()
	player = PlayerShip()
	pbt = PBullet(player)
	screen.onkey(key="Left", fun=player.move_left)
	screen.onkey(key="Right", fun=player.move_right)
	screen.onkey(key="x", fun=pbt.make_bullet)
	# screen.onclick(pbt.make_bullet)
	while True:
		if p_life != 0:
			if obt.check_ship_collision(player):
				p_life -= 1
		else:
			screen.title(f"Space Invader | Score : {score} | Game Over")
			break

		if pbt.check_ship_collision(opp_ships):
			score += 20
			screen.title(f"Space Invader | Score : {score} | Life: {p_life}")

		if opp_ships.check_ships():
			row += 1
			score += 100
			screen.title(f"Space Invader | Score : {score} | Life: {p_life}")
			screen.clear()
			main()
			# opp_ships.create_ships()
		obt.check_barrier_collision(barrier)
		obt.make_bullet()
		pbt.move_bullet()
		obt.bullet_to_bullet_collision(pbt)
		obt.move_bullet()
		barrier.check_health()
		screen.update()
	screen.exitonclick()

if __name__ == '__main__':
	main()