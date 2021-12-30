from turtle import Turtle

class Ball:
	"""Ball class of breaking-out"""
	def __init__(self):
		self.run = True
		self.b = Turtle()
		self.b.shape("circle")
		self.b.shapesize(1,1)
		self.b.color("red")
		self.b.penup()
		self.a_x = 0.5
		self.a_y = 0.5
		# self.b.speed(1)

	def move_ball(self):
		x = self.b.xcor()
		y = self.b.ycor()
		self.b.setposition(x + self.a_x, y + self.a_y)

	def bar_collision(self,bar):
		if self.b.distance(bar.bar) < (bar.bar.shapesize()[1]/2)*20 and self.b.ycor() > -230:
			self.a_y *= -1

	def ball_wall_collision(self):
		pos = self.b.position()
		if pos[0] < -200 or pos[0] > 200:
			self.a_x *= -1
		elif pos[1] > 240:
			self.a_y *= -1
		elif pos[1] < -240:
			self.run = False
			return False

	def ball_block_collision(self):
		self.a_y *= -1

	

		