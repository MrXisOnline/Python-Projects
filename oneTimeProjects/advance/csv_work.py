import pandas as pd

# Creating a Dataframe
data_dict = {
	"student":["Suraj","Priya","Prem"],
	"scores":[76,56,65]
}
data = pd.DataFrame(data_dict)
print(data)
data.to_csv("ex.csv")	# save the file with given name and type