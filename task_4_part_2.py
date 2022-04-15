import functools


def my_decorator2(f):
    @functools.wraps(f)
    def inner_decorator(n):
        if type(n) is int:
            print(f(n))
        else:
            raise ValueError("string type is not supported")

    return inner_decorator


@my_decorator2
def foo(n):
    return n * 2


print(foo(34))
print(foo('hello'))
