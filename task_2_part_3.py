d1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
d2 = {'a': 6, 'b': 7, 'z': 2, 'x': 40}
for key in d1.keys():
    if key in d2.keys():
        print(key)
    else:
        pass
