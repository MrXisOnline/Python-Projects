from turtle import Turtle
import random

colors = ["red", "yellow", "white", "green", "purple", "pink", "magenta"]
class Ship:
	def __init__(self, row):
		self.all_ships = []
		self.cur_ship_rows = row
		self.max_ship_rows = 5
		self.create_ships()

	def create_ships(self):
		y = 200
		if self.cur_ship_rows <= self.max_ship_rows:
			for _ in range(0, self.cur_ship_rows):
				row = []
				x = -230
				while x < 230:
					t = Turtle()
					row.append(t)
					t.shape("turtle")
					t.shapesize(1,1)
					t.setheading(270)
					t.color(random.choice(colors))
					t.penup()
					t.setposition(x, y)
					x += 30
				y -= 40
				self.all_ships.append(row)

	def check_ships(self):
		flag = 0
		for r in self.all_ships:
			if len(r) == 0:
				flag += 1
		if flag == self.cur_ship_rows:
			self.all_ships.clear()
			return True
		return False

	# def move_ships_left(self):
	# 	while self.all_ships[0][0].xcor() > -230:
	# 		for r in self.all_ships:
	# 			for s in r:
	# 				if s.xcor() < -230:
	# 					break
	# 				else:
	# 					x = s.xcor() - 10
	# 					s.setposition(x, s.ycor())

	# def move_ships_right(self):
	# 	while self.all_ships[0][len(self.all_ships[0])-1].xcor() < 230:
	# 		for r in self.all_ships:
	# 			e = reversed(r)
	# 			for _ in r:
	# 				try:
	# 					s = next(e)
	# 				except StopIteration:
	# 					break
	# 				if s.xcor() > 230:
	# 					break
	# 				else:
	# 					x = s.xcor() + 10
	# 					s.setposition(x, s.ycor())

	# def move(self):
	# 	# for r in self.all_ships:
	# 	# 	if len(r) > 0:
	# 	if self.all_ships[0][len(self.all_ships[0])-1].xcor() < 230:
	# 		self.move_ships_right()
	# 	else:
	# 		self.move_ships_left()


# scr = Screen()
# scr.bgcolor("black")
# scr.setup(width=500,height=500)
# scr.tracer(0)
# s = Ship()
# scr.update()
# scr.exitonclick()