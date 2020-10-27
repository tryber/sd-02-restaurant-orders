import csv
import sys


def get_most_ordered_by_maria(orders):
    maria_orders = {
        order["pedido"]: orders.count(order)
        for order in orders
        if order["cliente"] == "maria"
    }
    return max(maria_orders, key=maria_orders.get)


def get_hambuguer_frequency_by_arnaldo(orders):
    return [
        orders.count(order)
        for order in orders
        if order["pedido"] == "misto-quente" and order["cliente"] == "arnaldo"
    ][0]


def get_never_ordered_by_joao(orders):
    all_products = set([order["pedido"] for order in orders])
    joao_orders_products = set(
        [order["pedido"] for order in orders if order["cliente"] == "joao"]
    )
    return all_products.difference(joao_orders_products)


def get_days_never_visited_by_joao(orders):
    days = set([order["dia"] for order in orders])
    joao_orders_days = set(
        [order["dia"] for order in orders if order["cliente"] == "joao"]
    )
    return days.difference(joao_orders_days)


def analyse_log(path_to_file):
    all_orders = []
    try:
        with open(path_to_file, newline="") as file:
            fieldnames = ["cliente", "pedido", "dia"]
            news_reader = csv.DictReader(file, fieldnames=fieldnames)
            for row in news_reader:
                all_orders.append(row)
    except FileNotFoundError:
        print(f"Arquivo {path_to_file} não encontrado", file=sys.stderr)
    else:
        most_ordered_by_maria = get_most_ordered_by_maria(all_orders)
        hambuguer_frequency_by_arnaldo = str(
            get_hambuguer_frequency_by_arnaldo(all_orders)
        )
        never_ordered_by_joao = get_never_ordered_by_joao(all_orders)
        days_never_visited_by_joao = get_days_never_visited_by_joao(all_orders)
        with open("mkt_campaign.txt", "w") as file:
            lines = [
                f"{most_ordered_by_maria}\n",
                f"{hambuguer_frequency_by_arnaldo}\n",
                f"{never_ordered_by_joao}\n",
                f"{days_never_visited_by_joao}\n",
            ]
            file.writelines(lines)
