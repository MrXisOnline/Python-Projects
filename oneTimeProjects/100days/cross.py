class Cross:
	"""Crossing Map"""
	def __init__(self):
		self.l = Turtle()
		self.l.color("white")
		self.l.hideturtle()

	def liner(self, start, end):
		self.l.penup()
		self.l.setposition(*start)
		self.l.pendown()
		self.l.setposition(*end)

	def create_map(self):
		prog = True
		x = 250
		y = -200
		while prog:
			for i in range(4):
				start = (x,y)
				x_a = random.randint(25, 75)
				x -= x_a
				end = (x,y)
				self.liner(start, end)
				x -= 100
			x = 250
			y += 100
			if y > 250:
				prog = False