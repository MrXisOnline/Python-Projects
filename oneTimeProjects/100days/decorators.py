import time
import functools

def delay_decorator(func):
	@functools.wraps(func) # will preserve the func info.
	def wrapper_func():
		time.sleep(2)
		func()
	return wrapper_func

@delay_decorator
def print_hi():
	print("HI")

@delay_decorator
def print_bye():
	print("BYE")

def print_greet():
	print("How are you?")

# func = delay_decorator(print_greet)
# func()
print_greet()