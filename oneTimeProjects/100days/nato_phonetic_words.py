import pandas

data = pandas.read_csv("nato_alp.csv")
data_dict = {row.letter:row.code for (index,row) in data.iterrows()}
name = input("Enter Your Name : ").upper()
# try:
string = [data_dict[i] for i in name if i in data_dict.keys()]
# except KeyError:
# 	print("Only enter letters")

print(string)
