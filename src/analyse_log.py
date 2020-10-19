import csv


def read_csv(path_to_file):
    result = []
    with open(path_to_file, 'r', encoding='utf8') as csv_file:
        csv_readed = csv.reader(csv_file)
        for line in csv_readed:
            result.append(line)
    return result


def food_most_eaten_by(customer, data):
    food_count = {}
    most_frequent = ''
    for line in data:
        if line[0] == customer:
            if (most_frequent == ''):
                most_frequent = line[1]
            if line[1] in food_count:
                food_count[line[1]] += 1
            else:
                food_count[line[1]] = 1
            if food_count[line[1]] > food_count[most_frequent]:
                most_frequent = line[1]
    return most_frequent


def times_most_eaten(customer, food, data):
    times_eaten = 0
    for line in data:
        if (line[0] == customer and line[1] == food):
            times_eaten += 1
    return times_eaten


def discover_items(data, *, column):
    all_items = set()
    for line in data:
        all_items.add(line[column])
    return all_items


def items_that_was_not_asked(customer, data, all_items, *, column):
    customer_items = set()
    for line in data:
        if (line[0] == customer):
            customer_items.add(line[column])
    return all_items.difference(customer_items)


def save_log(data):
    with open("data/mkt_campaign.txt", "w") as txt_file:
        for line in data:
            txt_file.write(f'{line}\n')


def analyse_log(path_to_file):
    data = read_csv(path_to_file)
    if not len(data):
        return 'Arquivo vazio'
    all_foods = (discover_items(data, column=1))
    all_days = (discover_items(data, column=2))
    line_1 = food_most_eaten_by('maria', data)
    line_2 = times_most_eaten('arnaldo', 'hamburguer', data)
    line_3 = items_that_was_not_asked('joao', data, all_foods, column=1)
    line_4 = items_that_was_not_asked('joao', data, all_days, column=2)
    save_log([line_1, line_2, line_3, line_4])


if __name__ == '__main__':
    analyse_log('./data/orders_1.csv')
