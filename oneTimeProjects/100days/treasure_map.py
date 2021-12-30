t_map = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
print(f"{t_map[0]}\n{t_map[1]}\n{t_map[2]}")
position = input("where do you want to put the treasure : ")
t_map[int(position[1])-1][int(position[0])-1] = "X"
print(f"{t_map[0]}\n{t_map[1]}\n{t_map[2]}")