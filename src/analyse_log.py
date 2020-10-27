import csv


def check_path_and_format(file_name, file_ext):
    if not file_name.endswith(file_ext):
        print("Formato inválido")
        return True
    return False


def most_requested_food(data):
    dict_resp = {}
    most_frequent = data['Orders'][0]
    for values in data['Orders']:
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


def never_requested_meal(all_meals, data):
    meals = set(data)
    return all_meals.difference(meals)


def days_that_wasnt_in_place(all_days, data):
    cur_days = set(data)
    return all_days.difference(cur_days)


def import_csv(path_to_file):
    if(check_path_and_format(path_to_file, '.csv')):
        return True
    all_days = set()
    all_meals = set()
    data = ''
    resp = {}
    with open(path_to_file) as file:
        data = csv.reader(file, delimiter=",")
        for customer, order, day in data:
            if(customer not in resp):
                resp[customer] = {
                    'Orders': [],
                    'Days': [],
                }
            resp[customer]['Orders'].append(order)
            resp[customer]['Days'].append(day)
            all_days.add(day)
            all_meals.add(order)
    return resp, all_days, all_meals


def analyse_log(path_to_file):
    resp, all_days, all_meals = import_csv(path_to_file)
    if(resp is True):
        return True
    with open('output.txt', 'w+') as file:
        file.write(f"{most_requested_food(resp['maria'])}\n")
        file.write(
            f"{most_type_food('hamburguer', resp['arnaldo']['Orders'])}\n")
        file.write(
            f"{never_requested_meal(all_meals, resp['joao']['Orders'])}\n"
            )
        file.write(
            f"{days_that_wasnt_in_place(all_days, resp['joao']['Days'])}"
            )
