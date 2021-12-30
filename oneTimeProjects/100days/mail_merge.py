with open("mail_names.txt") as n:
	names = n.read()

with open("mail.docx") as m:
	mail = m.read()

name_list = names.split("\n")
mail_con = mail.split("\n")
for name in name_list:
	mail_con[0] = f"Dear {name},"
	str_mail = "\n".join(mail_con)
	file_name = f"\\mail_{name}.docx"
	file_path = "C:\\Users\\SG704\\PythonProjects\\oneTimeProjects\\100days\\mail_send" + file_name
	with open(file_path, "w") as file:
		file.write(str_mail)
