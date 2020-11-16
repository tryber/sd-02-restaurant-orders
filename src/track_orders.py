from src.services import (get_frequency_report_by,
                          get_fields_by, get_fields_related)


class TrackOrders:
    def __init__(self):
        self.data = []

    def add_new_order(self, costumer, order, day):
        self.data.append({"name": costumer, "order": order, "day": day})

    def get_most_ordered_dish_per_costumer(self, costumer):
        return get_frequency_report_by(
            "name", costumer, "order", self.data)[0][0]

    def get_order_frequency_per_costumer(self, costumer, order):
        return dict(get_frequency_report_by(
            "name", costumer, "order", self.data)).get(order, 0)

    def get_never_ordered_per_costumer(self, costumer):
        orders = get_fields_by("order", self.data)
        costumer_orders = get_fields_related(
            "name", costumer, "order", self.data)
        difference = ", ".join(sorted(orders - costumer_orders))
        return difference

    def get_days_never_visited_per_costumer(self, costumer):
        days = get_fields_by("day", self.data)
        costumer_days = get_fields_related(
            "name", costumer, "day", self.data)
        difference = ", ".join(sorted(days - costumer_days))
        return difference
