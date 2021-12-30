import turtle

class Score:
	def __init__(self, score):
		self.score_tur = turtle.Turtle()
		self.score_tur.color("white")
		with open("snake_high.txt", "r") as file:
			high = file.read()
		self.high_score = int(high)
		self.score_tur.speed(10)
		self.score_tur.penup()
		self.score_tur.setposition(-100,290)
		self.score_tur.hideturtle()
		self.score_tur.write(f"Score :{score} High-Score :{self.high_score}", align="left", font=("Arial",20,"normal"))

	def update_score(self,score):
		self.reset_high_score(score)
		self.score_tur.clear()
		self.score_tur.write(f"Score :{score} High-Score :{self.high_score}", align="left", font=("Arial",20,"normal"))

	def game_over(self):
		self.score_tur.setposition(-100, 0)
		self.score_tur.write("GAME-OVER!", align="left", font=("Arial",20,"normal"))

	def reset_high_score(self, score):
		if score > self.high_score:
			self.high_score = score
			with open("snake_high.txt", "w") as file:
				file.write(str(self.high_score))
