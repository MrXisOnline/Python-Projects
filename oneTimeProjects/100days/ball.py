from turtle import Turtle

class Ball:
	"""Creates the ball for ping pong"""
	def __init__(self):
		self.run = True
		self.b = Turtle()
		self.b.shape("circle")
		self.b.shapesize(1,1)
		self.b.color("red")
		self.b.penup()
		self.a_x = 100
		self.a_y = 100

	def move_ball(self):
		x = self.b.xcor()
		y = self.b.ycor()
		self.b.setposition(x + self.a_x, y + self.a_y)

	def ball_wall_collision(self):
		pos = self.b.position()
		if (pos[1] < -280) or (pos[1] > 280):
			self.a_y *= -1 
		elif (pos[0] < -380) or (pos[0] > 380):
			self.run = False
			return False
	
	def bar_collision(self,bar1,bar2):
		# print(self.b.distance(bar1.bar))
		if self.b.distance(bar2.bar) < 50 and self.b.xcor() > 340:
			self.a_x *= -1
			return "r"
		elif self.b.distance(bar1.bar) < 50 and self.b.xcor() < -340:
			self.a_x *= -1
			return "l"
		