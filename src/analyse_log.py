import sys
import csv
from os import path


def open_orders(file):
    orders_list = []

    with open(file, "r") as csv_orders:
        orders = csv.reader(csv_orders, delimiter=",")
        for order in orders:
            orders_list.append({
                "client": order[0],
                "meal": order[1],
                "day": order[2],
            })
    return orders_list


def maria_orders(file):
    all_orders = open_orders(file)
    maria_orders = []
    repeated_value = {}

    for order in all_orders:
        if order["client"] == "maria":
            maria_orders.append(order)
    for order in maria_orders:
        if order["meal"] not in repeated_value:
            repeated_value[order["meal"]] = 1
        elif order["meal"] in repeated_value:
            repeated_value[order["meal"]] += 1
    more_requested = max(repeated_value, key=repeated_value.get)
    return more_requested


def arnaldo_orders(file):
    all_orders = open_orders(file)
    arnaldo_count = 0

    for order in all_orders:
        if order["client"] == "arnaldo" and order["meal"] == "hamburguer":
            arnaldo_count += 1
    return arnaldo_count


def joao_orders(file):
    all_orders = open_orders(file)
    requests = set()
    joao_delivered = set()

    for order in all_orders:
        if order["meal"] not in requests:
            requests.add(order["meal"])
    
    for order in all_orders:
        if order["client"] == "joao":
            joao_delivered.add(order["meal"])
    return requests.difference(joao_delivered)


def analyse_log(path_to_file):
    exist = path.exists(path_to_file) or path.exists(f"./{path_to_file}")

    if not exist:
        print(f"Arquivo {path_to_file} não existe", file=sys.stderr)
        return
    if not path_to_file.endswith(".csv"):
        print("Formato Inválido", file=sys.stderr)
        return

    organized_orders = [
        maria_orders(path_to_file),
        arnaldo_orders(path_to_file),
        joao_orders(path_to_file),
    ]
    return organized_orders


print(analyse_log("./data/orders_1.csv"))
