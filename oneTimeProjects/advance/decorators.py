def decorator_func(original_func):
    def wrapper_func():
        print("wrapper function executed before {} function".format(original_func.__name__))
        return original_func()

    return wrapper_func


def display():
    print("display function running...")


decorated_func = decorator_func(display)
decorated_func()
