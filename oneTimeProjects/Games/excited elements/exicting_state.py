from turtle import Turtle, Screen
import time
import random


class Electron(Turtle):
	def __init__(self):
		super(Electron, self).__init__()
		self.penup()
		self.color("red")
		self.shape("circle")
		self.charge = "negative"
		self.force = 20
		self.setposition(random.randint(-300, 300), random.randint(-300, 300))
		# self.force_attract = 

	def collision(self, particle):
		if self.distance(particle) < 10:
			# if particle.charge == "positive":
			self.force, particle.force = -self.force, -particle.force
			self.set_heading_collision()
			particle.set_heading_collision()

	def move_particle(self):
		self.setposition(self.xcor() + self.force/2, self.ycor() + self.force/2)

	def set_heading_collision(self, particle=True):
		head = self.heading()
		n_head = head + 180 if particle else head + 60
		if n_head >= 360:
			n_head = n_head - 360

	def wall_collision(self):
		if self.xcor() >= 130 or self.xcor() <= -130 or self.ycor() >= 130 or self.ycor() >= -130:
			self.force = -self.force
			self.set_heading_collision(particle=False)

class Proton(Electron):
	def __init__(self):
		super(Proton, self).__init__()
		self.color("white")
		self.charge = "positive"
		self.shapesize(2, 2, 1)

screen = Screen()
screen.screensize(300, 300)
screen.bgcolor("black")
e = Electron()
p = Proton()
start = time.time()
run = True
try:		
	while run:
		if time.time() - start > 0.06:
			e.move_particle()
			# print(e.xcor(130))
			p.move_particle()
			start = time.time()
		e.wall_collision()
		p.wall_collision()
		e.collision(p)
		p.collision(e)
except KeyboardInterrupt:
	run = False

screen.exitonclick()