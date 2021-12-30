from threading import Thread, Lock
import time

# # dummy function 
# def square_func():
# 	for i in range(100):
# 		i*i

# threads = []
# num_threads = 10

# for i in range(num_threads):
# 	# create a thread target to specify the work/function
# 	t = Thread(target=square_func) # for arg. we can specify args parameter
# 	threads.append(t)	# saving thread in threads list

# for t in threads:
# 	t.start()	# starting thread

# for t in threads:
# 	t.join()	# joining threads to stop main thread until all thread finish

database_value = 0
def increase(lock):
	global database_value
	lock.acquire() # dont let another thread to change value
	local_copy = database_value
	local_copy += 1
	time.sleep(0.1)
	database_value = local_copy
	lock.release() # release the variable to other thread

lock = Lock()
print("Start value", database_value)
t1 = Thread(target=increase, args=(lock,))
t2 = Thread(target=increase, args=(lock,))
t1.start()
t2.start()

t1.join()
t2.join()
print("End value", database_value)
print("DONE")
