import pandas as pd

class Data:
	"""data worker for flash card program"""
	def __init__(self):
		self.df = pd.read_csv("flashcard_csv_data.csv")
		self.row_index=0
		self.rows=[]
		self.add_to_pre = []
		for (index,row) in self.df.iterrows():
			self.rows.append(row.to_list())
		self.check_previous_cards()
	
	def load_card(self,lang):
		try:
			if lang == "fr":
				word = self.rows[self.row_index][0]
			elif lang == "en":
				word = self.rows[self.row_index][1]
				self.row_index += 1
		except IndexError:
			self.row_index = 0
			if lang == "fr":
				word = self.rows[self.row_index][0]
			elif lang == "en":
				word = self.rows[self.row_index][1]
				self.row_index += 1
		finally:
			return word

	def check_previous_cards(self):
		cards = pd.read_csv("flashcard_pre.csv")
		pre_card = [row.to_list() for (index,row) in cards.iterrows()]
		for p in pre_card:
			self.add_to_pre.append(p)
			if p in self.rows:
				self.rows.pop(self.rows.index(p))

	def send_to_pre(self):
		self.add_to_pre.append(self.rows[self.row_index-1])
		pre_french = [i[0] for i in self.add_to_pre]
		pre_english = [i[1] for i in self.add_to_pre]
		pre_dict = {
		"french" : pre_french,
		"english" : pre_english
		}
		dtf = pd.DataFrame(pre_dict)
		dtf.to_csv("flashcard_pre.csv",index=False)
