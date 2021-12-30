from prettytable import PrettyTable
table = PrettyTable()

name = ["Bulbasur", "Charmander", "Pikachu"]
type_p = ["Water", "Fire", "Electric"]
table.add_column("Name", name)
table.add_column("Type", type_p)
table.align = "l"
print(table)