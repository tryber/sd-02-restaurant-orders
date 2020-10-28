from analyse_log import (
    get_most_ordered_dish_per_costumer,
    get_order_frequency_per_costumer,
    get_never_ordered_per_costumer,
    get_days_never_visited_per_costumer
)


class TrackOrders:
    def __init__(self):
        self.orders = []

    def add_new_order(self, costumer, order, day):
        self.orders.append({"cliente": costumer, "pedido": order, "dia": day})

    def get_most_ordered_dish_per_costumer(self, costumer):
        return get_most_ordered_dish_per_costumer(self.orders, costumer)

    def get_order_frequency_per_costumer(self, costumer, order):
        return get_order_frequency_per_costumer(self.orders, costumer, order)

    def get_never_ordered_per_costumer(self, costumer):
        return get_never_ordered_per_costumer(self.orders, costumer)

    def get_days_never_visited_per_costumer(self, costumer):
        return get_days_never_visited_per_costumer(self.orders, costumer)
