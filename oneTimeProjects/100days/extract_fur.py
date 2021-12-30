import pandas as pd

dict_data = {"Name" : ["Count"]
}
data = pd.read_csv("squirrel_data.csv")
fur = data["Primary Fur Color"].to_list()
for f in fur:
	if f in dict_data.keys():
		for k in dict_data.keys():
			if f == k:
				dict_data[f][0] = dict_data[f][0] + 1
	else:
		dict_data[f] = [1]

new_data = pd.DataFrame(dict_data)
new_data.to_csv("fur_data.csv")
print(new_data)