import pandas

student_data = {
	"student":["Angela","James","Lily"],
	"score":[56,76,98]
}
student_df = pandas.DataFrame(student_data)
for (index,row) in student_df.iterrows():
	print(row)