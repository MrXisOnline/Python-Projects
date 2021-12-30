import random
import time
import tkinter as tk


def check_get_word(e):
	global job_id
	global start_time
	global total_correct_words
	global total_error
	global cur_word
	if cur_word == None:
		start_time = time.time()
		cur_word = random.choice(words)
		job_id = root.after(1000, update_time)
		return cur_word
	elif time.time() - start_time <= end_time:
		inp = input_word.get()
		if cur_word == inp:
			total_correct_words += 1
			cur_word = random.choice(words)
			word_label.config(text=cur_word)
			input_word.delete(0, "end")
		else:
			total_error += 1
			input_word.delete(0, "end")
	else:
		text = f"Words per Minute : {int(total_correct_words/5)}\nTotal Errors : {total_error}"
		result_label.config(text=text)

def update_time():
	global job_id
	left = end_time - int(time.time() - start_time)
	if left >= 0:
		time_left.config(text=f"Time Left : {left}s")
		job_id = root.after(1000, update_time)
	else:
		if job_id != None:
			root.after_cancel(job_id)
			job_id = None
			check_get_word(0)

with open("words.txt", mode="r") as file:
	words = file.read()
words = words.split(", ")
end_time = 300
job_id = None
cur_word = None
start_time = None
total_correct_words = 0
total_error = 0
root = tk.Tk()
root.title("Typing-Speed-test")
root.minsize(400,200)
time_left = tk.Label(text="Time Left : 300s")
time_left.pack()
word_label = tk.Label(text=check_get_word(0))
word_label.pack()
input_word = tk.Entry(width=30)
input_word.pack()
input_word.focus_set()
result_label = tk.Label(root, text="")
result_label.pack()
root.bind("<Return>", check_get_word)
root.mainloop()