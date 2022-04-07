def cache_decorator(f):
    cache = {}

    def inner_decorator(*args):
        inner_decorator.ncalls += 1
        if args not in cache and f(*args):
            i = f(*args)
            cache[args] = i
            return i
        else:
            print(f"Function executed with counter = {inner_decorator.ncalls}, function result = {f(*args)}")
            return cache[args]

    inner_decorator.ncalls = 0
    return inner_decorator


@cache_decorator
def foo(n, m):
    return n ** 32 + m ** 10


foo(200, 180)
foo(200, 180)
