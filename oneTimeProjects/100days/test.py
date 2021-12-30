import time

start_min = time.localtime(time.time()).tm_min
start_sec = time.localtime(time.time()).tm_sec
end_min = time.localtime(time.time()).tm_min + 1
end_sec = time.localtime(time.time()).tm_sec
while ((start_min*60)+start_sec) < ((end_min*60)+end_sec):
	t = ((end_min*60)+end_sec) - ((start_min*60)+start_sec)
	sec = t%60
	mins = t//60
	print(f"{mins}:{sec}")
	time.sleep(1)
	start_min = time.localtime(time.time()).tm_min
	start_sec = time.localtime(time.time()).tm_sec
else:
	# dis_text.config(text=f"{start_min}:{start_sec}")
	print("works")