from turtle import Turtle

class PBullet:
	def __init__(self, player):
		self.all_bullet = []
		self.ref = player

	def make_bullet(self):
		if self.Bullet_restriction():
			self.remove_waste_caps()
			b = Turtle()
			self.all_bullet.append(b)
			b.penup()
			b.color("white")
			b.shape("circle")
			b.setheading(90)
			b.shapesize(0.5,0.5)
			player_pos = self.ref.player.position()
			b.setposition(player_pos[0], player_pos[1])

	def move_bullet(self):
		if len(self.all_bullet) != 0:
			for b in self.all_bullet:
				y_pos = b.ycor() + 10
				b.setposition(b.xcor(), y_pos)

	def Bullet_restriction(self):
		flag = True
		for b in self.all_bullet:
			if b.ycor() > 230:
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
			for r in opp.all_ships:
				for s in r:
					if b.distance(s) < 20:
						b.hideturtle()
						s.hideturtle()
						opp.all_ships[opp.all_ships.index(r)].pop(r.index(s))
						self.all_bullet.pop(self.all_bullet.index(b))
						return True
		return False