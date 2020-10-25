import csv


def analyse_log(path_to_file):
    orders = get_orders_from_csv_file(path_to_file)

    results = [
        get_most_ordered_dish_maria(orders),
        get_hamburguer_quantity_arnaldo(orders),
        get_never_ordered_joao(orders),
        get_days_never_visited_joao(orders),
    ]

    write_new_file(results)


def get_orders_from_csv_file(path_to_file):
    with open(path_to_file, mode="r") as file:
        data = csv.reader(file, delimiter=",", quotechar='"')

        orders = []
        for row in data:
            orders.append({
                "costumer": row[0],
                "dish": row[1],
                "day": row[2],
            })

    return orders


def get_most_ordered_dish_maria(orders):
    quantity_per_dish = {}
    greatest_quantity = 0

    for order in orders:
        costumer = order["costumer"]
        dish = order["dish"]

        if costumer != "maria":
            pass

        if dish not in quantity_per_dish:
            quantity_per_dish[dish] = 1
        else:
            quantity_per_dish[dish] += 1

        current_quantity = quantity_per_dish[dish]
        if current_quantity > greatest_quantity:
            greatest_quantity = current_quantity
            most_ordered_dish = dish

    return most_ordered_dish


def get_hamburguer_quantity_arnaldo(orders):
    return len([
        order
        for order in orders
        if order["costumer"] == "arnaldo" and order["dish"] == "hamburguer"
    ])


def get_never_ordered_joao(orders):
    all_dishes = set()
    dishes_joao = set()

    for order in orders:
        dish = order["dish"]

        all_dishes.add(dish)

        if order["costumer"] == "joao":
            dishes_joao.add(dish)

    return all_dishes - dishes_joao


def get_days_never_visited_joao(orders):
    all_days = set()
    days_joao = set()

    for order in orders:
        day = order["day"]

        all_days.add(day)

        if order["costumer"] == "joao":
            days_joao.add(day)

    return all_days - days_joao


def write_new_file(lines):
    with open("data/mkt_campaign.txt", mode="w") as new_file:
        for line in lines:
            new_file.write(f"{line}\n")
