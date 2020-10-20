class TrackOrders:

    def __init__(self):
        self.dict_orders = {}
        self.days = {
            'segunda-feira',
            'terça-feira',
            'quarta-feira',
            'quinta-feira',
            'sexta-feira',
            'sabado',
            'domingo',
        }
        self.count_days = {
            'segunda-feira': 0,
            'terça-feira': 0,
            'quarta-feira': 0,
            'quinta-feira': 0,
            'sexta-feira': 0,
            'sabado': 0,
            'domingo': 0
            }
        self.orders = {
            'hamburguer',
            'pizza',
            'coxinha',
            'misto-quente',
        }

    def create_count_days(self, day):
        self.count_days[day] += 1

    def add_new_order(self, costumer, order, day):
        if(costumer not in self.dict_orders):
            self.dict_orders[costumer] = {
                'Orders': [],
                'Days': [],
            }
        self.create_count_days(day)
        self.dict_orders[costumer]['Orders'].append(order)
        self.dict_orders[costumer]['Days'].append(day)

    def get_most_ordered_dish_per_costumer(self, costumer):
        data = self.dict_orders[costumer]
        dict_resp = {}
        most_frequent = data['Orders'][0]
        for values in data['Orders']:
            if(values not in dict_resp):
                dict_resp[values] = 1
            else:
                dict_resp[values] += 1
            if(dict_resp[values] > dict_resp[most_frequent]):
                most_frequent = values
        return most_frequent

    def get_order_frequency_per_costumer(self, costumer, order):
        count_order = 0
        data = self.dict_orders[costumer]
        for values in data['Orders']:
            if(values == order):
                count_order += 1
        return count_order

    def get_never_ordered_per_costumer(self, costumer):
        data = self.dict_orders[costumer]['Orders']
        meals = set(data)
        return self.orders.difference(meals)

    def get_days_never_visited_per_costumer(self, costumer):
        data = self.dict_orders[costumer]['Days']
        cur_days = set(data)
        return self.days.difference(cur_days)

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
