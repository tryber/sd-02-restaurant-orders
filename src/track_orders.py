from src.analyse_log import (
    most_requested_food,
    most_type_food,
    never_requested_meal,
    days_that_wasnt_in_place
)


class TrackOrders:

    def __init__(self):
        self.dict_orders = {}
        self.days = set()
        self.count_days = {}
        self.orders = set()

    def add_new_order(self, costumer, order, day):
        if(costumer not in self.dict_orders):
            self.dict_orders[costumer] = {
                'Orders': [],
                'Days': [],
            }
        self.count_days[day] = self.count_days.get(day, 0) + 1
        self.dict_orders[costumer]['Orders'].append(order)
        self.dict_orders[costumer]['Days'].append(day)
        self.days.add(day)
        self.orders.add(order)

    def get_most_ordered_dish_per_costumer(self, costumer):
        return most_requested_food(self.dict_orders[costumer])

    def get_order_frequency_per_costumer(self, costumer, order):
        return most_type_food(order, self.dict_orders[costumer]['Orders'])

    def get_never_ordered_per_costumer(self, costumer):
        return never_requested_meal(
            self.orders, self.dict_orders[costumer]['Orders']
        )

    def get_days_never_visited_per_costumer(self, costumer):
        return days_that_wasnt_in_place(
            self.days, self.dict_orders[costumer]['Days']
        )

    def get_busiest_day(self):
        max_tuple = max(self.count_days.items(), key=lambda x: x[1])
        busiest_days = [
            day
            for day, count in self.count_days.items()
            if count == max_tuple[1]
        ]
        return busiest_days

    def get_least_busy_day(self):
        min_tuple = min(self.count_days.items(), key=lambda x: x[1])
        least_busy_days = [
            day
            for day, count in self.count_days.items()
            if count == min_tuple[1]
        ]
        return least_busy_days
