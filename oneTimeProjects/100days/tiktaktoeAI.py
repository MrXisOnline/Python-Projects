import random

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


def enter_pos(user_pos):
    if user_pos in board_pos.keys():
        ind = board_pos[user_pos]
        if ind in pos_check():
            board[ind[0]][ind[1]] = user
            return ind
        else:
            print("Position Taken!")
            return "ff", "ff"
    else:
        print("Position Doesn\'t Exits")
        return "ff", "ff"


def change_user():
    global user
    if user == "X":
        user = "O"
    else:
        user = "X"


def check_win(row, col):
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
        if board[j[0]][j[1]] == user:
            pass
        else:
            flag = False
            break
    if flag:
        print(f"{user} Wins")
        return True
    flag = True
    for j in col_items:
        if board[j[0]][j[1]] == user:
            pass
        else:
            return False
    if flag:
        print(f"{user} Wins")
        return True


def diagonal_check():
    if board[0][0] == user and board[1][2] == user and board[2][4] == user:
        print(f"{user} Wins")
        return True
    elif board[0][4] == user and board[1][2] == user and board[2][0] == user:
        print(f"{user} Wins")
        return True
    else:
        return False


while True:
    x = int(input("Enter Pos: "))
    pos_in = enter_pos(x)
    print_board()
    if check_win(*pos_in) or diagonal_check():
        break
    change_user()
    if len(pos_check()) == 0:
        print("It\'s a DRAW")
        break
