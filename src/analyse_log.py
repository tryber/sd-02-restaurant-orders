import csv


def most_requested_food(data):
    dict_resp = {}
    most_frequent = data['Foods'][0]
    for values in data['Foods']:
        if(values not in dict_resp):
            dict_resp[values] = 1
        else:
            dict_resp[values] += 1
        if(dict_resp[values] > dict_resp[most_frequent]):
            most_frequent = values
    return most_frequent


def most_type_food(food, data):
    count_food = 0
    for values in data:
        if(values == food):
            count_food += 1
    return count_food


def never_requested_meal(data):
    all_meals = {
        'hamburguer': 0,
        'pizza': 0,
        'coxinha': 0,
        'misto-quente': 0,
    }
    meals = set()
    for meal in data:
        all_meals[meal] += 1
    for not_meals, count in all_meals.items():
        if (count == 0):
            meals.add(not_meals)
    return meals


def days_that_wasnt_in_place(data):
    days = {
        'segunda-feira': 0,
        'terça-feira': 0,
        'quarta-feira': 0,
        'quinta-feira': 0,
        'sexta-feira': 0,
        'sabado': 0,
        'domingo': 0,
    }
    not_days = set()
    for day in data:
        days[day] += 1
    for day, count in days.items():
        if(count == 0):
            not_days.add(day)
    return not_days


def import_csv(path_to_file):
    data = ''
    resp = {}
    with open(path_to_file) as file:
        data = csv.reader(file, delimiter=",")
        for values in data:
            if(values[0] not in resp):
                resp[values[0]] = {
                    'Foods': [],
                    'Days': [],
                }
            resp[values[0]]['Foods'].append(values[1])
            resp[values[0]]['Days'].append(values[2])
    return resp


def analyse_log(path_to_file):
    resp = import_csv(path_to_file)
    with open('output.txt', 'w+') as file:
        file.write(f"{most_requested_food(resp['maria'])}\n")
        file.write(
            f"{most_type_food('hamburguer', resp['arnaldo']['Foods'])}\n")
        file.write(f"{never_requested_meal(resp['joao']['Foods'])}\n")
        file.write(f"{days_that_wasnt_in_place(resp['joao']['Days'])}")


analyse_log('data/orders_1.csv')
