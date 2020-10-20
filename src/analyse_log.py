import csv
import os


def check_path_and_format(file_name, file_ext):
    if not os.path.exists(file_name):
        print(f"Arquivo {file_name} não econtrado")
        return True
    if not file_name.endswith(file_ext):
        print("Formato inválido")
        return True
    return False


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
        'hamburguer',
        'pizza',
        'coxinha',
        'misto-quente',
    }
    meals = set(data)
    return all_meals.difference(meals)


def days_that_wasnt_in_place(data):
    all_days = {
        'segunda-feira',
        'terça-feira',
        'quarta-feira',
        'quinta-feira',
        'sexta-feira',
        'sabado',
        'domingo',
    }
    cur_days = set(data)
    return all_days.difference(cur_days)


def import_csv(path_to_file):
    if(check_path_and_format(path_to_file, '.csv')):
        return True
    data = ''
    resp = {}
    with open(path_to_file) as file:
        data = csv.reader(file, delimiter=",")
        for name, food, day in data:
            if(name not in resp):
                resp[name] = {
                    'Foods': [],
                    'Days': [],
                }
            resp[name]['Foods'].append(food)
            resp[name]['Days'].append(day)
    return resp


def analyse_log(path_to_file):
    resp = import_csv(path_to_file)
    if(resp is True):
        return True
    with open('output.txt', 'w+') as file:
        file.write(f"{most_requested_food(resp['maria'])}\n")
        file.write(
            f"{most_type_food('hamburguer', resp['arnaldo']['Foods'])}\n")
        file.write(f"{never_requested_meal(resp['joao']['Foods'])}\n")
        file.write(f"{days_that_wasnt_in_place(resp['joao']['Days'])}")


analyse_log('data/orders_1.csv')
