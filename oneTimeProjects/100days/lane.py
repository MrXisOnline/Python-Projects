from turtle import Turtle
import random
car_colors = ["red", "orange", "purple", "yellow", "blue", "green"]

class Lane:
	"""Lane for Turtle crossing"""
	def __init__(self):
		self.lane = []
		self.run = True
		self.creater()

	def lane_handler(self):
		x = random.randint(25,50)
		for c in self.lane:
			pos_c = c.position()
			c.setposition(int(pos_c[0])-x, int(pos_c[1]))

	def creater(self):
		r = random.randint(1,6)
		if r == 1:
			y = random.randint(-230,230)
			car = Turtle()
			self.lane.append(car)
			car.color(random.choice(car_colors))
			car.penup()
			car.shape("square")
			car.shapesize(stretch_wid=1, stretch_len=2)
			car.setposition(380,y)

	def start_car(self):
		self.creater()
		self.lane_handler()

	def garbage_collection(self):
		for g in range(50):
			self.lane.pop(0)