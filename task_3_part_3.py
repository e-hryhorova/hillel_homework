def most_frequent(list_var):
    result = {elem: list_var.count(elem) for elem in list_var}
    return max(result, key=result.get)


print(most_frequent(['ty', 'ty', 'ty', 'a', 'a', 'bi', 'bi', 'bi', 'ty']))
