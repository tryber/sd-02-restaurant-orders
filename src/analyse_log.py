import csv
import sys


def most_ordered_meal(list, name):
    filtered_list = [value for value in list if value["cliente"] == name]
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


def meals_from_customer(list, name, meal):
    return len([list.count(list_item) for list_item in list if list_item["pedido"]== meal and list_item["cliente"] == name])


def meals_never_asked(list, name):
    filtered_list = [value for value in list if value["cliente"] == name]
    foods_set = set()
    for order in list:
        foods_set.add(order["pedido"])


    for order in filtered_list:
        if order["pedido"] in foods_set:
            foods_set.remove(order["pedido"])
    return foods_set

def days_never_visited(list, name):
    filtered_list = [value for value in list if value["cliente"] == name]
    days_set = set()
    for order in list:
        days_set.add(order["dia"])


    for order in filtered_list:
        if order["dia"] in days_set:
            days_set.remove(order["dia"])
    return days_set
    


def analyse_log(csv_file):
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

        all_results = [
            most_ordered_meal(orders_log, "maria"),
            meals_from_customer(orders_log, "arnaldo", "hamburguer"),
            meals_never_asked(orders_log, "joao"),
            days_never_visited(orders_log, "joao")
        ]

        with open("data/mkt_campaign.txt", mode="w") as new_file:
            lines = [
                f"{str(result)}\n"
                for result in all_results
            ]

            new_file.writelines(lines)


print(analyse_log("data/orders_1.csv"))
