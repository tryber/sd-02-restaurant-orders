all_days = {
    "sabado",
    "segunda-feira",
    "terça-feira",
}


class TrackOrders:
    def __init__(self):
        self.list_orders = {}
        self.orders_possible = set()

    def add_new_order(self, costumer, order, day):
        if costumer not in self.list_orders:
            self.list_orders[costumer] = {}
            self.list_orders[costumer]["days"] = {day}
            self.list_orders[costumer][order] = 1
            self.list_orders[costumer]["Most Frequent Value"] = 1
            self.list_orders[costumer]["Food most Frequent"] = order
            self.orders_possible.add(order)
        else:
            self.orders_possible.add(order)
            self.list_orders[costumer]["days"].add(day)

            if order in self.list_orders[costumer]:
                self.list_orders[costumer][order] += 1
            else:
                self.list_orders[costumer][order] = 1

            if (
                self.list_orders[costumer][order]
                > self.list_orders[costumer]["Most Frequent Value"]
            ):
                self.list_orders[costumer][
                    "Most Frequent Value"
                ] = self.list_orders[costumer][order]
                self.list_orders[costumer]["Food most Frequent"] = order

    def get_most_ordered_dish_per_costumer(self, costumer):
        return self.list_orders[costumer]["Food most Frequent"]

    def get_order_frequency_per_costumer(self, costumer, order):
        return (
            self.list_orders[costumer][order]
            if order in self.list_orders[costumer]
            else 0
        )

    def get_never_ordered_per_costumer(self, costumer):
        return self.orders_possible - self.list_orders[costumer].keys()

    def get_days_never_visited_per_costumer(self, costumer):
        return all_days - self.list_orders[costumer]["days"]
