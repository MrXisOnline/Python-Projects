from turtle import Turtle
import random

class OBullet:
	def __init__(self, player):
		self.all_bullet = []
		self.ref = player

	def make_bullet(self):
		if self.Bullet_restriction():
			self.remove_waste_caps()
			x = 1
			for r in self.ref.all_ships:
				if x == 1:
					for s in r:
						if random.randint(1,6) == 6:
							b = Turtle()
							self.all_bullet.append(b)
							b.penup()
							b.color("red")
							b.shape("circle")
							b.setheading(270)
							b.shapesize(0.5,0.5)
							player_pos = s.position()
							b.setposition(player_pos[0], player_pos[1])
					x = 0

	def move_bullet(self):
		if len(self.all_bullet) != 0:
			for b in self.all_bullet:
				y_pos = b.ycor() - 10
				b.setposition(b.xcor(), y_pos)

	def Bullet_restriction(self):
		flag = True
		for b in self.all_bullet:
			if b.ycor() < -230:
				pass
			else:
				flag = False
				break
		return flag

	def remove_waste_caps(self):
		if len(self.all_bullet) > 100:
			for i in range(50):
				self.all_bullet.pop(0)

	def check_ship_collision(self, opp):
		for b in self.all_bullet:
			if b.distance(opp.player) < 20:
				b.hideturtle()
				self.all_bullet.pop(self.all_bullet.index(b))
				return True
		return False

	def check_barrier_collision(self, barrier):
		for b in self.all_bullet:
			for bar in barrier.all_barrier:
				if b.distance(bar) < 30:
					b.hideturtle()
					self.all_bullet.pop(self.all_bullet.index(b))
					bar_index = barrier.all_barrier.index(bar)
					barrier.barrier_health[bar_index] -= 10

	def bullet_to_bullet_collision(self, op_bullet):
		for b in self.all_bullet:
			for o in op_bullet.all_bullet:
				if b.distance(o) < 10:
					b.hideturtle()
					self.all_bullet.pop(self.all_bullet.index(b))
					o.hideturtle()
					op_bullet.all_bullet.pop(op_bullet.all_bullet.index(o))