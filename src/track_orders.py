class TrackOrders:
    def __init__(self):
        self.all_sales = {}
        self.days = set()
        self.orders = set()

    def add_new_order(self, costumer, order, day):
        self.orders.add(order)
        self.days.add(day)
        if costumer not in self.all_sales:
            self.all_sales[costumer] = {"order": {}, "days": {}}
        self.all_sales[costumer]["order"][order] = (
            self.all_sales[costumer]["order"].get(order, 0)+1)
        self.all_sales[costumer]["days"][day] = (
            self.all_sales[costumer]["days"].get(day, 0)+1)

    def get_most_ordered_dish_per_costumer(self, costumer):
        return max(
            self.all_sales[costumer]["order"],
            key=self.all_sales[costumer]["order"].get
        )

    def get_order_frequency_per_costumer(self, costumer, order):
        pass

    def get_never_ordered_per_costumer(self, costumer):
        pass

    def get_days_never_visited_per_costumer(self, costumer):
        pass
