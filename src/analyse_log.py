import csv
from functools import reduce


def fill_clients_with_row(row, clients, all_orders, all_week_days):
    [costumer, order, week_day] = row
    all_orders.add(order)
    all_week_days.add(week_day)

    if costumer not in clients:
        clients[costumer] = {}
        clients[costumer]["orders"] = {}
        clients[costumer]["week_days"] = {}

    if order not in clients[costumer]["orders"]:
        clients[costumer]["orders"][order] = 1
    else:
        clients[costumer]["orders"][order] += 1

    if week_day not in clients[costumer]["week_days"]:
        clients[costumer]["week_days"][week_day] = 1
    else:
        clients[costumer]["week_days"][week_day] += 1


def most_ordered(costumer, clients):
    return list(
        reduce(
            lambda a, b: a if a[1] > b[1] else b,
            clients[costumer]["orders"].items(),
            (0, 0),
        )
    )[0]


def get_order_qt(order, costumer, clients):
    qt = 0
    if order in clients[costumer]["orders"]:
        qt = clients[costumer]["orders"][order]
    return qt


def never_ordered(clients, costumer, all_orders):
    costumer_orders = set(clients[costumer]["orders"].keys())
    return all_orders.difference(costumer_orders)


def week_days_never_visited(clients, costumer, all_week_days):
    week_days = set(clients[costumer]["week_days"].keys())
    return all_week_days.difference(week_days)


def write_resposta(clients, path_to_file, all_orders, all_week_days):
    with open(path_to_file, "w") as file:
        maria_most_ordered = most_ordered("maria", clients)
        file.write(f"{maria_most_ordered}\n")

        hamburguer_qt = get_order_qt("hamburguer", "arnaldo", clients)
        file.write(f"{hamburguer_qt}\n")

        joao_nerver_ordered = never_ordered(clients, "joao", all_orders)
        file.write(f"{joao_nerver_ordered}\n")

        joao_week_days = week_days_never_visited(
            clients,
            "joao",
            all_week_days,
        )
        file.write(f"{joao_week_days}\n")


def analyse_log(path_to_file):
    with open("./data/orders_1.csv") as file:
        status = csv.reader(file, delimiter=";", quotechar='"')
        header, *data = status

        clients = {}
        all_orders = set()
        all_week_days = set()

        for row in data:
            fill_clients_with_row(
                row[0].split(","),
                clients,
                all_orders,
                all_week_days,
            )

        print(all_week_days)

        write_resposta(clients, path_to_file, all_orders, all_week_days)

