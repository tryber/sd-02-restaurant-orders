from src.analyse_log import format_dict, mais_pedido, dias_pratos


class TrackOrders:
    def __init__(self):
        self.infos = []
        self.format_orders = {}
        self.value_keys = {}

    def add_new_order(self, costumer, order, day):
        new_dict = {"name": costumer, "ingredient": order, "day": day}
        self.infos.append(new_dict)
        self.format_orders, self.value_keys = format_dict(self.infos)

    def get_most_ordered_dish_per_costumer(self, costumer):
        return mais_pedido(
            self.format_orders[costumer], self.value_keys["ingredients"]
            )

    def get_dish_quantity_per_costumer(self, costumer, order):
        return self.format_orders[costumer][order]

    def get_never_ordered_per_costumer(self, costumer):
        return dias_pratos(
            self.format_orders[costumer], self.value_keys["ingredients"]
            )

    def days_format(self):
        dict_days = {
            "segunda-feira": 0,
            "terça-feira": 0,
            "quarta-feira": 0,
            "quinta-feira": 0,
            "sexta-feira": 0,
            "sabado": 0,
            "domingo": 0,
        }

        def add_value(value, people):
            dict_days[value] += int(self.format_orders[people][value])

        for people in self.format_orders:
            add_value("segunda-feira", people)
            add_value("terça-feira", people)
            add_value("quarta-feira", people)
            add_value("quinta-feira", people)
            add_value("sexta-feira", people)
            add_value("sabado", people)
            add_value("domingo", people)
        return dict_days

    def get_busiest_day(self):
        days_count = self.days_format()
        return mais_pedido(days_count, self.value_keys["days"])

    def get_least_busy_day(self):
        days_count = self.days_format()
        menor_valor = -1
        dia_final = ""
        for day in self.value_keys["days"]:
            if days_count[day] < menor_valor or menor_valor == -1:
                dia_final = day
                menor_valor = days_count[day]
        return dia_final
