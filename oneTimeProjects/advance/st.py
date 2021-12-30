def print_table(list2d):
    print("".rjust(49, "-"))
    for row in list2d:
        print("|", end="")
        for col in row:
            print(col.center(10), "|", end="")
        print()
    print("".rjust(49, "-"))


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
print_table(tableData)
