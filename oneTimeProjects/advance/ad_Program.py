import _thread as thread
import time

# Comprehension
print([i * 2 for i in range(10)])
print((i * 4 for i in range(10)))
print({i * 10 for i in range(10)})
print({i: i * 5 for i in range(10)})
print(i * i for i in range(20) if i % 3 == 0)
print([(x, y) for x in range(1, 20, 3) for y in range(3)])
print([[y * 3 for y in range(10)] for i in range(5)])
print([[[(x, y, z) for x in range(3)] for y in range(3)] for z in range(3)])


# Extended Keyword Argument
def hyper_volume(*lengths):
    i = iter(lengths)
    v = next(i)
    for length in i:
        v *= length
    return v


print(hyper_volume(1, 2, 3, 4, 5, 6))


def print_argv(arg1, arg2, *args):
    print(arg1)
    print(arg2)
    print(args)


print_argv(1, 2, 3, 4, 5, 6)


# Inner Functions/Closure
def outer():
    print("From Outer")

    def inner():
        print("From Inner")

    return inner


I1 = outer()
I1()


# All Classes Are also Objects LOL!
def first(name):
    print(name)


first("Suraj")
second = first
second("Suraj")


# Higher Order Functions
def inc(x):
    return x + 1


def dec(x):
    return x - 1


def operate(func, x):
    result = func(x)
    return result


print(operate(inc, 3))
print(operate(dec, 3))


# Decorators
def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a, b)

    return inner


@smart_divide
def divide(a, b):
    print(a / b)


divide(7, 6)
divide(1, 0)


# Define a function for the thread
def print_time(thread_name):
    for i in range(5):
        time.sleep(1)
        print(thread_name)


# Create two threads as follows
try:
    thread.start_new_thread(print_time, ("Thread-1\n",))
    thread.start_new_thread(print_time, ("Thread-2\n",))
except:
    print("Error")
while 1:
    pass
