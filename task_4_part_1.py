import functools


def my_decorator(f):
    @functools.wraps(f)
    def wrapper(n):
        if 100 % f(n) == 0:
            print(f"We are OK!")
        else:
            print(f"Bad news guys, we got {100 % f(n)}")
    return wrapper


@my_decorator
def foo(n):
    return n


print(foo(29))
