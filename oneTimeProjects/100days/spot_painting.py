from turtle import Turtle, Screen
import turtle
import random

timmy = Turtle()	 
color_list = [(232, 230, 227), (233, 228, 231), (231, 236, 233), (230, 232, 236), (199, 158, 116), (157, 85, 39), (42, 107, 150), (132, 168, 188), (191, 155, 21), (10, 28, 60), (193, 142, 163), (149, 64, 93), (62, 24, 10), (63, 16, 36), (156, 25, 10), (194, 86, 115), (137, 27, 54), (131, 180, 164), (220, 202, 130), (45, 127, 96)]
timmy.shape("turtle")
dist = 0
inc = 30
turtle.colormode(255)
position = timmy.position()
for _ in range(100):
	if dist >= 500:
		timmy.setx(position[0])
		timmy.sety(inc)
		inc += 30
		dist = 0
	timmy.penup()
	timmy.fd(30)
	timmy.pendown()
	# timmy.pencolor()
	timmy.dot(20, random.choice(color_list))
	dist += 50
	timmy.penup()


screen = Screen()		
screen.exitonclick()	