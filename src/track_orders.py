class TrackOrders:
    def __init__(self):
        self.sales = {}
        self.all_days = set()
        self.all_orders = set()
        self.orders_by_day = {}

    def add_new_order(self, costumer, order, day):
        self.all_days.add(day)
        self.all_orders.add(order)
        if costumer not in self.sales:
            self.sales[costumer] = {'foods': {}, 'days': {}}
        self.sales[costumer]['foods'][order] = (self.sales[costumer]
                                                ['foods'].get(order, 0)+1)
        self.sales[costumer]['days'][day] = (self.sales
                                             [costumer]['days'].get(day, 0)+1)
        self.orders_by_day[day] = self.orders_by_day.get(day, 0)+1

    def get_most_ordered_dish_per_costumer(self, costumer):
        foods = self.sales[costumer]['foods']
        return max(foods, key=foods.get)

    def get_order_frequency_per_costumer(self, costumer, order):
        return self.sales[costumer]['foods'].get(order, 0)

    def get_never_ordered_per_costumer(self, costumer):
        return self.all_orders.difference(self.sales[costumer]['foods'])

    def get_days_never_visited_per_costumer(self, costumer):
        return self.all_days.difference(self.sales[costumer]['days'])

    def get_busiest_day(self):
        foods = self.orders_by_day
        return max(foods, key=foods.get)

    def get_least_busy_day(self):
        foods = self.orders_by_day
        return min(foods, key=foods.get)
