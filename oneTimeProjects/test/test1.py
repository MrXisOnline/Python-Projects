def highlighter(text):
    def cover_func(*args, **kwargs):
        print('**********')
        text(*args, **kwargs)
        print('**********')
    return cover_func


@highlighter
def greet(greeting, emoji=':)'):
    print(greeting, emoji)


greet('heyy')