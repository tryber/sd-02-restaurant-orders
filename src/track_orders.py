from src.analyse_log import (
    fill_clients_with_row,
    most_ordered,
    get_order_qt,
    never_ordered,
    week_days_never_visited,
)


class TrackOrders:
    def __init__(self):
        self.clients = {}
        self.all_orders = set()
        self.all_week_days = set()

    def add_new_order(self, costumer, order, day):
        row = [costumer, order, day]
        self.all_orders.add(order)
        self.all_week_days.add(day)

        fill_clients_with_row(
            row,
            self.clients,
            self.all_orders,
            self.all_week_days,
        )

    def get_most_ordered_dish_per_costumer(self, costumer):
        return most_ordered(costumer, self.clients)

    def get_order_frequency_per_costumer(self, costumer, order):
        return get_order_qt(order, costumer, self.clients)

    def get_never_ordered_per_costumer(self, costumer):
        return never_ordered(self.clients, costumer, self.all_orders)

    def get_days_never_visited_per_costumer(self, costumer):
        return week_days_never_visited(
            self.clients,
            costumer,
            self.all_week_days,
        )
