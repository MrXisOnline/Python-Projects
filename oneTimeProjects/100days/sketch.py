timmy = Turtle()	 
color_list = ["red","blue","green","brown","purple","orange"]
timmy.shape("turtle")	

def w_press():
	timmy.forward(20)

def s_press():
	timmy.backward(20)

def a_press():
	timmy.left(10)

def d_press():
	timmy.right(10)

def c_press():
	timmy.clear()

screen = Screen()
screen.listen()
screen.onkey(key="w", fun=w_press)
screen.onkey(key="s", fun=s_press)
screen.onkey(key="a", fun=a_press)
screen.onkey(key="d", fun=d_press)
screen.onkey(key="c", fun=c_press)
screen.exitonclick()	