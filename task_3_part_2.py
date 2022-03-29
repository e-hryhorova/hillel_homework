data = [

    {'name': 'Viktor', 'city': 'Kiev', 'age': 30},

    {'name': 'Maksim', 'city': 'Dnepr', 'age': 20},

    {'name': 'Vladimir', 'city': 'Lviv', 'age': 32},

    {'name': 'Andrey', 'city': 'Kiev', 'age': 34},

    {'name': 'Artem', 'city': 'Dnepr', 'age': 50},

    {'name': 'Dmitriy', 'city': 'Lviv', 'age': 21}]


def sort_elements_by_age(d):
    return sorted(d, key=lambda i: i['age'])


print(sort_elements_by_age(data))
