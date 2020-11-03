import csv


def extract_orders_from_csv(orders):
    all_orders = []
    with open(orders, newline="") as file:
        fieldnames = ["cliente", "pedido", "dia"]
        news_reader = csv.DictReader(file, fieldnames=fieldnames)
        for row in news_reader:
            all_orders.append(row)
    return all_orders


def get_most_ordered_dish_per_costumer(orders, costumer):
    maria_orders = {
        order["pedido"]: orders.count(order)
        for order in orders
        if order["cliente"] == costumer
    }
    return max(maria_orders, key=maria_orders.get)


def get_order_frequency_per_costumer(orders, costumer, order):
    orders_count = {
        order: orders.count(item)
        for item in orders
        if item["pedido"] == order and item["cliente"] == costumer
    }
    if not orders_count:
        return int()
    return orders_count[order]


def get_never_ordered_per_costumer(orders, costumer):
    all_products = set([order["pedido"] for order in orders])
    joao_orders_products = set(
        [order["pedido"] for order in orders if order["cliente"] == costumer]
    )
    return all_products.difference(joao_orders_products)


def get_days_never_visited_per_costumer(orders, costumer):
    days = set([order["dia"] for order in orders])
    joao_orders_days = set(
        [order["dia"] for order in orders if order["cliente"] == costumer]
    )
    return days.difference(joao_orders_days)


def analyse_log(path_to_file):
    orders = extract_orders_from_csv(path_to_file)
    most_ordered_by_maria = get_most_ordered_dish_per_costumer(orders, "maria")
    hambuguer_frequency_by_arnaldo = get_order_frequency_per_costumer(
        orders, "arnaldo", "hamburguer"
    )
    never_ordered_by_joao = get_never_ordered_per_costumer(orders, "joao")
    days_never_visited_by_joao = get_days_never_visited_per_costumer(
        orders, "joao"
    )
    with open("mkt_campaign.txt", "w") as file:
        lines = [
            f"{most_ordered_by_maria}\n",
            f"{hambuguer_frequency_by_arnaldo}\n",
            f"{never_ordered_by_joao}\n",
            f"{days_never_visited_by_joao}\n",
        ]
        [file.write(line) for line in lines]
        # file.writelines(lines)
