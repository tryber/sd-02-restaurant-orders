class TrackOrders:
    def __init__(self, orders=[]):
        self.orders = orders

    def add_new_order(self, costumer, order, day):
        self.orders.append({
            "costumer": costumer,
            "dish": order,
            "day": day
        })

    def get_most_ordered_dish_per_costumer(self, costumer):
        quantity_per_dish = {}
        greatest_quantity = 0

        for order in self.orders:
            dish = order["dish"]

            if order["costumer"] != costumer:
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

    def get_order_frequency_per_costumer(self, costumer, order):
        return len([
            order
            for order in self.orders
            if order["costumer"] == costumer and order["dish"] == order
        ])

    def get_dish_quantity_per_costumer(self, costumer, order):
        return len([
            order
            for order in self.orders
            if order["costumer"] == costumer and order["dish"] == order
        ])

    def get_never_ordered_per_costumer(self, costumer):
        all_dishes = set()
        costumer_dishes = set()

        for order in self.orders:
            dish = order["dish"]

            all_dishes.add(dish)

            if order["costumer"] == costumer:
                costumer_dishes.add(dish)

        return all_dishes - costumer_dishes

    def get_busiest_day(self):
        quantity_per_day = {}
        greatest_quantity = 0

        for order in self.orders:
            day = order["day"]

            if day not in quantity_per_day:
                quantity_per_day[day] = 1
            else:
                quantity_per_day[day] += 1

            current_quantity = quantity_per_day[day]
            if current_quantity > greatest_quantity:
                greatest_quantity = current_quantity
                busiest_day = day

        return busiest_day

    def get_least_busy_day(self):
        quantity_per_day = {}

        for order in self.orders:
            day = order["day"]

            if day not in quantity_per_day:
                quantity_per_day[day] = 1
            else:
                quantity_per_day[day] += 1

        least_quantity = len(self.orders) + 1
        for key, value in quantity_per_day.items():
            if value < least_quantity:
                least_quantity = value
                least_busy_day = key

        return least_busy_day

    def get_days_never_visited_per_costumer(self, costumer):
        all_days = set()
        costumer_days = set()

        for order in self.orders:
            day = order["day"]

            all_days.add(day)

            if order["costumer"] == costumer:
                costumer_days.add(day)

        return all_days - costumer_days
