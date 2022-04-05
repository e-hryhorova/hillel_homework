data = [

    {'name': 'Viktor', 'city': 'Kiev', 'age': 30},

    {'name': 'Maksim', 'city': 'Dnepr', 'age': 20},

    {'name': 'Vladimir', 'city': 'Lviv', 'age': 32},

    {'name': 'Andrey', 'city': 'Kiev', 'age': 34},

    {'name': 'Artem', 'city': 'Dnepr', 'age': 50},

    {'name': 'Dmitriy', 'city': 'Lviv', 'age': 21}]


def sort_elements_by_age(d):
    return sorted(d, key=lambda i: i['age'])


def group_data_by_city(d):
    list_cities = []
    list_kiev = []
    list_dnepr = []
    list_lviv = []
    for d in data:
        if d['city'] == 'Kiev':
            list_cities.append(d.pop('city'))
            list_kiev.append(d)
        elif d['city'] == 'Dnepr':
            list_cities.append(d.pop('city'))
            list_dnepr.append(d)
        else:
            list_cities.append(d.pop('city'))
            list_lviv.append(d)
    values = [list_kiev, list_dnepr,  list_lviv]
    result = dict(zip(list_cities, values))
    return result


print(sort_elements_by_age(data))
print(group_data_by_city(data))
