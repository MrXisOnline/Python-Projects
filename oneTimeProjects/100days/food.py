import turtle
import random
pos = [-280, -260, -240, -220, -200, -180, -160, -140, -120, -100, -80, -60, -40, -20, 0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280]

class Food:
	"""Spawns Food"""
	def __init__(self):
		self.food = turtle.Turtle()
		self.food.penup()
		self.food.color("red")
		self.food.shape("circle")
		self.respawn()

	def respawn(self):
		self.n_pos = (random.choice(pos), random.choice(pos))
		self.food.setposition(*self.n_pos)
		