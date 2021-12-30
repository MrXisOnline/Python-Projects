from multiprocessing import Process, Value, Lock, Pool
import os
import time

# # dummy function
# def square_num():
# 	for i in range(100):
# 		i*i

# if __name__ == "__main__":
# 	processes = []
# 	num_process = os.cpu_count()

# 	for i in range(num_process):
# 		# all of the things are same as creating are thread
# 		process = Process(target=square_num)
# 		processes.append(process)

# 	for p in processes:
# 		p.start()

# 	for p in processes:
# 		p.join()

# 	print("DONE")

# def add_100(num, lock):
# 	with lock:
# 		for _ in range(100):
# 			time.sleep(0.01)
# 			num.value += 1

# if __name__ == '__main__':
# 	shared_value = Value("i", 0) # in Value we give type and value
# 	lock = Lock()
# 	print("Num at start", shared_value.value)
# 	p1 = Process(target=add_100, args=(shared_value, lock))
# 	p2 = Process(target=add_100, args=(shared_value, lock))

# 	p1.start()
# 	p2.start()

# 	p1.join()
# 	p2.join()

# 	print("Num at end", shared_value.value)

def cube(num):
	return num**3

if __name__ == '__main__':
	start = time.time()
	pool = Pool()
	number = range(100000)
	result = pool.map(cube, number) # map function and args. in pool obj.
	pool.close()
	pool.join()

	print(time.time() - start)
	start = time.time()
	for i in number:
		cube(i)
	print(time.time() - start)