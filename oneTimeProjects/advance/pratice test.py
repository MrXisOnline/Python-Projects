def separator(l):
    text = ""
    for i in range(len(l)):
        if i == (len(l) - 1):
            text = text + " and " + str(l[i])
        elif i == 0:
            text = text + str(l[i])
        else:
            text = text + ", " + str(l[i])
    print(text)


spam = ['apples', 'bananas', 'tofu', 'cats']
separator(spam)

grid = [['.', '.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.']]


def print_img():
    del grid[0]
    del grid[len(grid) - 1]
    for x in range(len(grid) - 1):
        for y in range(len(grid)):
            print(grid[y][x], end="")
        print()


print_img()
