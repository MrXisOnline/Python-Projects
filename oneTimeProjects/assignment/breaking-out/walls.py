from turtle import Turtle, Screen
import random
import turtle

part_colors = ["red", "orange", "purple", "yellow", "blue", "green"]

class Wall:
	"""Create Walls in breaking out"""
	def __init__(self):
		self.wall_parts = []
		self.run = True
		self.wall_height = 3
		self.max_wall_height=7
		self.create_wall()

	def create_wall(self):
		y = 200
		for _ in range(0,self.wall_height):
			x = -200
			part_width = random.randint(1,4)
			n_x = x + (part_width/2)*20
			while x<=200:
				if x > 150:
					t = Turtle()
					self.wall_parts.append(t)
					t.color(random.choice(part_colors))
					t.penup()
					t.shape("square")
					h = (200-x)/20
					if h != 0:
						t.shapesize(1,h)
						n_x = x + (h/2)*20
						t.setposition(n_x,y)
					x = 201
				else:
					t = Turtle()
					self.wall_parts.append(t)
					t.color(random.choice(part_colors))
					t.penup()
					t.shape("square")
					t.shapesize(1,part_width)
					t.setposition(n_x,y)
					part_width = random.randint(1,4)
					x = n_x + (part_width/2)*20
					n_x = x + (part_width/2)*20
			y -= 20

	def ball_collision(self,ball_pos):
		for p in self.wall_parts:
			if p.isvisible():
				if p.distance(*ball_pos) < (p.shapesize()[1]/2)*20:
					p.hideturtle()
					self.wall_parts.pop(self.wall_parts.index(p))
					return True

	def win(self):
		if len(self.wall_parts) == 0:
			self.wall_height += 1
			if self.wall_height > self.max_wall_height:
				return "win"
			self.create_wall()

# check = Screen()
# check.setup(450,500)
# check.tracer(0)
# w = Wall()
# check.update()
# check.exitonclick()