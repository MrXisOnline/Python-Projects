from turtle import Turtle
import turtle
import random

class Snake:
	"""Create the snake"""
	def __init__(self):
		start_tur = Turtle()
		mid_tur = Turtle()
		last_tur = Turtle()
		self.tur = [start_tur, mid_tur, last_tur]
		pos_x = 0
		for c in self.tur:
			c.color("white")
			c.shape("square")
			c.penup()
			c.setposition(pos_x, 0)
			c.speed(10)
			pos_x += -20

	def move(self):
		for seg in range(len(self.tur)-1,-1,-1):
			if seg == 0:
				self.tur[seg].forward(20)
			else:
				pos = self.tur[seg-1].position()
				self.tur[seg].setposition(*pos)

	def up(self):
		cur_heading = int(self.tur[0].heading())
		if cur_heading == 270:
			pass
		else:
			self.tur[0].setheading(90)

	def down(self):
		cur_heading = int(self.tur[0].heading())
		if cur_heading == 90:
			pass
		else:
			self.tur[0].setheading(270)

	def left(self):
		cur_heading = int(self.tur[0].heading())
		if cur_heading == 0:
			pass
		else:
			self.tur[0].setheading(180)

	def right(self):
		cur_heading = int(self.tur[0].heading())
		if cur_heading == 180:
			pass
		else:
			self.tur[0].setheading(0)

	def check_food(self, food_pos):
		if self.tur[0].distance(*food_pos) < 10:
			self.increse_length()
			return True
		else:
			return False

	def check_wall(self):
		pos = self.tur[0].position()
		if (int(pos[0]) >= 300) or (int(pos[0]) <= -300) or (int(pos[1]) >= 300) or (int(pos[1]) <= -300):
			return True
		else:
			return False
		
	def increse_length(self):
		inc_tur = Turtle()
		inc_tur.color("white")
		inc_tur.shape("square")
		inc_tur.penup()
		lst_ele_pos = self.tur[len(self.tur)-1].position()
		inc_pos = (lst_ele_pos[0]-20,lst_ele_pos[1])
		inc_tur.setposition(*inc_pos)
		inc_tur.speed(10)
		self.tur.append(inc_tur)

	# def body_collision(self):
	# 	head = self.tur[0]
	# 	for t in self.tur[1:]:
	# 		if head.distance(t) < 10 :
	# 			print("body :", t)
	# 			raise Exception("Body Collision")