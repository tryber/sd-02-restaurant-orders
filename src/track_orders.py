from src.analyse_log import (
    days_never_visited,
    meals_from_customer,
    meals_never_asked,
    most_ordered_meal,
)


class TrackOrders:
    def __init__(self):
        self.orders_log = []


    def add_new_order(self, costumer, order, day):
        self.orders_log.append({"cliente": costumer, "pedido": order, "dia": day})

    def get_most_ordered_dish_per_costumer(self, costumer):
        return most_ordered_meal(self.orders_log, costumer)

    def get_order_frequency_per_costumer(self, costumer, order):
        return meals_from_customer(self.orders_log, costumer, order)

    def get_never_ordered_per_costumer(self, costumer):
        return meals_never_asked(self.orders_log, costumer)

    def get_days_never_visited_per_costumer(self, costumer):
        return days_never_visited(self.orders_log, costumer)
