keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
values = []
i = 0
while i < len(keys):
    value = keys[i]*keys[i]
    values.append(value)
    i += 1
dic = dict(zip(keys, values))
print(dic)
