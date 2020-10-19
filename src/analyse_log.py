import csv


all_days = {
    "sabado",
    "segunda-feira",
    "terça-feira",
}


def check_file(path_to_file):
    with open(path_to_file, mode="r") as csv_file:
        csvLines = csv.reader(csv_file, delimiter=",")
        orders = set()
        order_by_client = {}
        for name, food, day in csvLines:
            if name not in order_by_client:
                order_by_client[name] = {}
                order_by_client[name]["days"] = {day}
                order_by_client[name][food] = 1
                order_by_client[name]["Most Frequent Value"] = 1
                order_by_client[name]["Food most Frequent"] = food
                orders.add(food)
            else:
                orders.add(food)
                order_by_client[name]["days"].add(day)

                if food in order_by_client[name]:
                    order_by_client[name][food] += 1
                else:
                    order_by_client[name][food] = 1

                if (
                    order_by_client[name][food]
                    > order_by_client[name]["Most Frequent Value"]
                ):
                    order_by_client[name][
                        "Most Frequent Value"
                    ] = order_by_client[name][food]
                    order_by_client[name]["Food most Frequent"] = food
        return order_by_client, orders


def most_frequent_order(order_by_client, name):
    return order_by_client[name]["Food most Frequent"]


def times_specific_order(order_by_client, name, food):
    return order_by_client[name][food] if food in order_by_client[name] else 0


def not_asked_order(order_by_client, name, orders):
    return orders - order_by_client[name].keys()


def days_not_gone(order_by_client, name, all_days):
    return all_days - order_by_client[name]["days"]


def analyse_log(path_file, path_to_write):
    order_by_client, orders = check_file(path_file)
    line1 = most_frequent_order(order_by_client, "maria")
    line2 = times_specific_order(order_by_client, "arnaldo", "hamburguer")
    line3 = not_asked_order(order_by_client, "joao", orders)
    line4 = days_not_gone(order_by_client, "joao", all_days)
    with open(path_to_write, mode="w") as write_file:
        write_file.write(f"{line1}\n")
        write_file.write(f"{line2}\n")
        write_file.write(f"{line3}\n")
        write_file.write(f"{line4}\n")
