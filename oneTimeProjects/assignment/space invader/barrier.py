from turtle import Turtle

# colors = ["red", "yellow", "white", "green", "purple", "pink", "magenta"]

class Barrier:
	def __init__(self):
		self.all_barrier = []
		self.barrier_health = [100 for _ in range(12)]
		self.make_barrier()

	def make_barrier(self):
		y = 0
		for _ in range(2):
			x = -200
			while x < 230:
				b = Turtle()
				self.all_barrier.append(b)
				b.penup()
				b.shape("square")
				b.shapesize(2,3)
				b.color("red")
				b.setposition(x, y)
				x += 80
			y += 50

	def check_health(self):
		for bar_h in self.barrier_health:
			if bar_h <= 0:
				bar_in = self.barrier_health.index(bar_h)
				self.all_barrier[bar_in].hideturtle()
				self.barrier_health.pop(bar_in)
				self.all_barrier.pop(bar_in)


# scr = Screen()
# scr.bgcolor("black")
# scr.setup(width=500,height=500)
# scr.tracer(0)
# s = Barrier()
# scr.update()
# scr.exitonclick()

