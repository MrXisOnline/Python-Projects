import pandas as pd

class Data:
	"""Data extractor class for us states"""
	def __init__(self):
		self.data = pd.read_csv("50_states.csv")
		self.states = self.data["state"].to_list()
		self.gamedata = "us_state_gamedata.csv"
		self.get_gamedata()
		self.cor_state = len(self.entered_state)
	
	def give_position(self, st):
		self.cor_state = self.cor_state + 1
		row = self.data[self.data["state"] == st]
		x_cord = int(row["x"])
		y_cord = int(row["y"])
		return (x_cord, y_cord)

	def check_state(self, st):
		if st in self.states and st not in self.entered_state:
			self.entered_state.append(st)
			return True
		else:
			return False
		
	def get_gamedata(self):
		g_data = pd.read_csv(self.gamedata)
		self.entered_state = g_data["cur_state"].to_list()

	def append_gamedata(self):
		game_dict = {
		"cur_state": self.entered_state
		}
		n_data = pd.DataFrame(game_dict)
		n_data.to_csv(self.gamedata)

