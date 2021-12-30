import os
import getopt
import sys

path = "C:\\Windows\\System32\\drivers\\etc"
# path = "C:\\Users\\SG704\\Downloads"
os.chdir(path)

def usage():
	print("weblock.py -l www.google.com")
	print("weblock.py --unlock www.google.com")


def main():
	lock_status = True
	website = ""
	lhost = "127.0.0.1"

	try:
		opts, args = getopt.getopt(sys.argv[1:], "hu:l:", ["help","unlock","lock"])
	except getopt.GetoptError as err:
		print(str(err))
		usage()


	for o,a in opts:
		if o in ("-h","--help"):
			usage()
		elif o in ("-l","--lock"):
			website = str(a)
		elif o in ("-u", "--unlock"):
			lock_status = False
			website = str(a)

	if lock_status:
		if website == "":
			pass
		else:
			file_inc = open("hosts", "a")
			file_inc.write("\n" + lhost + " " + website)
			file_inc.close()
	elif website == "":
		raise Exception("Website Field is Empty!!!")
	else:
		file_inc = open("hosts", "r")
		data = file_inc.read()
		file_inc.close()
		sep_element = data.split("\n")
		if website in data:
			for i in range(len(sep_element)):
				if website in sep_element[i]:
					sep_element.pop(i)
					break

			newdata = "\n".join(sep_element)		
			file_ins = open("hosts", "w")
			file_ins.write(newdata)
			file_ins.close()
		else:
			pass



if __name__ == '__main__':
	main()