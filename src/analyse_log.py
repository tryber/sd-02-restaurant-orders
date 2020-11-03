import csv
import sys


def most_ordered_meal(list_param, name):
    filtered_list = [value for value in list_param if value["cliente"] == name]
    count = {}
    most_frequent = filtered_list[0]["pedido"]
    

    for order in filtered_list:
        if order["pedido"] not in count:
            count[order["pedido"]] = 1
        else:
            count[order["pedido"]] += 1
        if count[order["pedido"]] > count[most_frequent]:
            most_frequent = order["pedido"]
    return most_frequent


def meals_from_customer(list_param, name, meal):
    return len([list_param.count(list_item) for list_item in list_param if list_item["pedido"]== meal and list_item["cliente"] == name])


def meals_never_asked(list_param, name):
    all_meals = set()
    customer_meals = set()

    for order in list_param:
        meal = order["pedido"]

        all_meals.add(meal)

        if order["cliente"] == name:
            customer_meals.add(meal)

    return all_meals - customer_meals


def days_never_visited(list_param, name):
    all_days = set()
    customer_days = set()

    for order in list_param:
        day = order["dia"]

        all_days.add(day)

        if order["cliente"] == name:
            customer_days.add(day)

    return all_days - customer_days


def create_orders_log(csv_file):
    with open(csv_file, encoding="utf8", mode="r") as file:
        if not csv_file.endswith(".csv"):
            print("Formato inválido", file=sys.stderr)
            sys.exit(1)
        if not len(csv_file):
            print("Arquivo vazio", file=sys.stderr)
            sys.exit(1)
        orders_log = []
        fieldnames = ["cliente", "pedido", "dia"]
        read_csv = csv.DictReader(file, fieldnames=fieldnames)
        for line in read_csv:
            orders_log.append(line)
        return orders_log


def write_file(txt_file, list_results):
    with open(txt_file, mode="w") as new_file:
        lines = [
            f"{str(result)}\n"
            for result in list_results
        ]

        new_file.writelines(lines)


def analyse_log(csv_file):
    orders_log = create_orders_log(csv_file)
    all_results = [
        most_ordered_meal(orders_log, "maria"),
        meals_from_customer(orders_log, "arnaldo", "hamburguer"),
        meals_never_asked(orders_log, "joao"),
        days_never_visited(orders_log, "joao")
    ]

    # write_file("data/mkt_campaign.txt", all_results)


print(analyse_log("data/orders_1.csv"))
