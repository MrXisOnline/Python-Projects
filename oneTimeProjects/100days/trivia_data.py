import requests
import html

class Question:
	def __init__(self, q, ans):
		self.question = self.format_question(q)
		self.answer = ans

	def check_ans(self, ans):
		if self.answer == ans:
			return True
		else:
			return False

	def format_question(self,ques):
		text = ques
		new_text=""
		des = 0
		for char in range(len(text)):

			if des <= 15:
				new_text += text[char]
				des += 1
			elif text[char] == " ":
				new_text += text[char]+"\n"
				des = 0
			else:
				new_text += text[char]
				des += 1
		return new_text


class Questions:
	def __init__(self):
		self.ques_index = 0
		self.score=0
		parameters = {
			"amount":20,
			"type":"boolean"
		}
		url = "https://opentdb.com/api.php"
		response = requests.get(url,params=parameters)
		response.raise_for_status()
		data = response.json()["results"]
		self.questions = []
		for i in data:
			ques = html.unescape(i["question"])
			ans = i["correct_answer"]
			self.questions.append(Question(ques,ans))

	def give_question(self):
		if self.ques_index >= len(self.questions):
			self.ques_index = 0
		return self.questions[self.ques_index]

	def check_ans(self,ans):
		if self.questions[self.ques_index].check_ans(ans):
			self.score += 1
			self.ques_index += 1
			return True
		else:
			self.ques_index += 1
			return False
