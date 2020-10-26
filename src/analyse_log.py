import sys
import csv
from os import path


def define_orders(file):
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
    all_orders = define_orders(file)
    print(all_orders)


def analyse_log(path_to_file):
    exist = path.exists(path_to_file) or path.exists(f"./{path_to_file}")

    if not exist:
        print(f"Arquivo {path_to_file} não existe", file=sys.stderr)
        return
    if not path_to_file.endswith(".csv"):
        print("Formato Inválido", file=sys.stderr)
        return
    
    organized_orders = [
        maria_orders(path_to_file)
    ]
    return organized_orders


print(analyse_log("./data/orders_1.csv"))
