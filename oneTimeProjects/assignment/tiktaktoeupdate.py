import random

def change_user(user):
    if user == "X":
        return "O"
    else:
        return "X"

def print_board():
    for r in board:
        for c in r:
            print(c, end="")
        print()

def pos_check():
    pos = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "_" or board[i][j] == " ":
                pos.append((i, j))
    return pos

def check_win(row, col, cur_user):
    flag = True
    row_items = []
    col_items = []
    for i in list(board_pos.values()):
        if row == i[0]:
            row_items.append(i)
        elif col == i[1]:
            col_items.append(i)
    if len(row_items) == 0 or len(col_items) == 0:
        return False
    for j in row_items:
        if board[j[0]][j[1]] == cur_user:
            pass
        else:
            flag = False
            break
    if flag:
        print(f"{cur_user} Wins")
        return True
    flag = True
    for j in col_items:
        if board[j[0]][j[1]] == cur_user:
            pass
        else:
            return False
    if flag:
        print(f"{cur_user} Wins")
        return True

def diagonal_check(cur_user):
    if board[0][0] == cur_user and board[1][2] == cur_user and board[2][4] == cur_user:
        print(f"{cur_user} Wins")
        return True
    elif board[0][4] == cur_user and board[1][2] == cur_user and board[2][0] == cur_user:
        print(f"{cur_user} Wins")
        return True
    else:
        return False

board = [
    ["_", " | ", "_", " | ", "_"],
    ["_", " | ", "_", " | ", "_"],
    [" ", " | ", " ", " | ", " "]
]
board_pos = {
    1: (0, 0), 2: (0, 2), 3: (0, 4),
    4: (1, 0), 5: (1, 2), 6: (1, 4),
    7: (2, 0), 8: (2, 2), 9: (2, 4)
}
user = random.choice(["X", "O"])
another_user = change_user(user)

class Player:
	"""Tik-tak-toe Player"""
	def __init__(self, user):
		self.player = user

	def play_a_move(self, move):
		if move in board_pos.keys():
			ind = board_pos[move]
			if ind in pos_check():
				board[ind[0]][ind[1]] = self.player
				return ind
			else:
				print("Position Taken!")
				return "ff", "ff"
		else:
			print("Position Doesn\'t Exits")
			return "ff", "ff"

	def is_win(self, move):
		if check_win(*pos_in, self.player) or diagonal_check(self.player):
			return True
		else:
			return False

class GeniusPlayer(Player):
	def __init__(self, user):
		super(GeniusPlayer, self).__init__(user)
		self.player = user

	def get_a_move(self):
		self_win = self.check_self_wins()
		if self_win == None:
			opp_win = self.check_opp_wins()
			if opp_win == None:
				random_move = random.choice(pos_check())
				return random_move
			else:
				return opp_win
		else:
			return self_win

	def play_a_move(self):
		ind = self.get_a_move()
		board[ind[0]][ind[1]] = self.player
		return ind

	def check_all_wins(self, user):
		row, col = self.get_empty_rowcol()
		for r in row:
			e = 0
			r_c = None
			for c in [0,2,4]:
				if board[r][c] == user:
					e += 1
				elif board[r][c] == " " or board[r][c] == "_":
					r_c = (r, c)
			if e == 2:
				return r_c
		for c in col:
			e = 0
			for r in [0,1,2]:
				if board[r][c] == user:
					e += 1
				elif board[r][c] == " " or board[r][c] == "_":
					r_c = (r, c)
			if e == 2:
				return r_c
		d_win = self.check_diagonal_wins(user)
		if d_win != None:
			return d_win
		return None

	def check_self_wins(self):
		self_win = self.check_all_wins(self.player)
		return self_win

	def check_opp_wins(self):
		opp_win = self.check_all_wins(change_user(self.player))
		return opp_win

	def get_empty_rowcol(self):
		all_pos = pos_check()
		row, col = [], []
		for p in all_pos:
			if p[0] not in row:
				row.append(p[0])
			elif p[1] not in col:
				col.append(p[1])
		return row, col

	def check_diagonal_wins(self, user):
		diagonal1 = [(0,0), (1,2), (2,4)]
		diagonal2 = [(0,4), (1,2), (2,0)]
		e = 0
		r_c = None
		for d in [diagonal1, diagonal2]:
			for c in d:
				if board[c[0]][c[1]] == user:
					e += 1
				elif board[c[0]][c[1]] == " " or board[c[0]][c[1]] == "_":
					r_c = c
			if e == 2:
				return r_c
		return None
	
player1 = Player(user)
player2 = GeniusPlayer(another_user)
run = True
while run:
	for player in [player1,player2]:
		if type(player) == Player:
			move = int(input("Your move: "))
			pos_in = player.play_a_move(move)
		else:
			pos_in = player.play_a_move()
		print(f"{player.player}'s Move")
		print_board()
		if player.is_win(pos_in):
			run = False
			break
		if len(pos_check()) == 0:
			print("It\'s a DRAW")
			run = False
			break
