# Crie uma suíte de testes para a classe TrackOrders
# Obtenha, no mínimo, 90% de cobertura

from src.track_orders import TrackOrders

orders_mock = [
    {"costumer": "maria", "dish": "hamburguer", "day": "terça-feira"},
    {"costumer": "joao", "dish": "hamburguer", "day": "terça-feira"},
    {"costumer": "maria", "dish": "pizza", "day": "terça-feira"},
    {"costumer": "maria", "dish": "coxinha", "day": "segunda-feira"},
    {"costumer": "arnaldo", "dish": "misto-quente", "day": "terça-feira"},
    {"costumer": "jose", "dish": "hamburguer", "day": "sabado"},
    {"costumer": "maria", "dish": "hamburguer", "day": "terça-feira"},
    {"costumer": "maria", "dish": "hamburguer", "day": "terça-feira"},
    {"costumer": "joao", "dish": "hamburguer", "day": "terça-feira"},
    {"costumer": "maria", "dish": "pizza", "day": "terça-feira"},
    {"costumer": "maria", "dish": "coxinha", "day": "segunda-feira"},
    {"costumer": "arnaldo", "dish": "misto-quente", "day": "terça-feira"},
    {"costumer": "jose", "dish": "hamburguer", "day": "sabado"},
    {"costumer": "maria", "dish": "hamburguer", "day": "terça-feira"},
    {"costumer": "maria", "dish": "hamburguer", "day": "terça-feira"},
    {"costumer": "joao", "dish": "hamburguer", "day": "terça-feira"},
    {"costumer": "maria", "dish": "pizza", "day": "terça-feira"},
    {"costumer": "maria", "dish": "coxinha", "day": "segunda-feira"},
    {"costumer": "arnaldo", "dish": "misto-quente", "day": "terça-feira"},
    {"costumer": "jose", "dish": "hamburguer", "day": "sabado"},
    {"costumer": "maria", "dish": "hamburguer", "day": "terça-feira"},
    {"costumer": "maria", "dish": "hamburguer", "day": "terça-feira"},
    {"costumer": "joao", "dish": "hamburguer", "day": "terça-feira"},
    {"costumer": "maria", "dish": "pizza", "day": "terça-feira"},
    {"costumer": "maria", "dish": "coxinha", "day": "segunda-feira"},
    {"costumer": "arnaldo", "dish": "misto-quente", "day": "terça-feira"},
    {"costumer": "jose", "dish": "hamburguer", "day": "sabado"},
    {"costumer": "maria", "dish": "hamburguer", "day": "terça-feira"},
    {"costumer": "maria", "dish": "hamburguer", "day": "terça-feira"},
    {"costumer": "joao", "dish": "hamburguer", "day": "terça-feira"},
    {"costumer": "maria", "dish": "pizza", "day": "terça-feira"},
    {"costumer": "maria", "dish": "coxinha", "day": "segunda-feira"},
    {"costumer": "arnaldo", "dish": "misto-quente", "day": "terça-feira"},
    {"costumer": "jose", "dish": "hamburguer", "day": "sabado"},
    {"costumer": "maria", "dish": "hamburguer", "day": "terça-feira"},
    {"costumer": "maria", "dish": "hamburguer", "day": "terça-feira"},
    {"costumer": "joao", "dish": "hamburguer", "day": "terça-feira"},
    {"costumer": "maria", "dish": "pizza", "day": "terça-feira"},
    {"costumer": "maria", "dish": "coxinha", "day": "segunda-feira"},
    {"costumer": "arnaldo", "dish": "misto-quente", "day": "terça-feira"},
    {"costumer": "jose", "dish": "hamburguer", "day": "sabado"},
    {"costumer": "maria", "dish": "hamburguer", "day": "terça-feira"},
    {"costumer": "maria", "dish": "hamburguer", "day": "terça-feira"},
    {"costumer": "joao", "dish": "hamburguer", "day": "terça-feira"},
    {"costumer": "maria", "dish": "pizza", "day": "terça-feira"},
    {"costumer": "maria", "dish": "coxinha", "day": "segunda-feira"},
    {"costumer": "arnaldo", "dish": "misto-quente", "day": "terça-feira"},
    {"costumer": "jose", "dish": "hamburguer", "day": "sabado"},
    {"costumer": "maria", "dish": "hamburguer", "day": "terça-feira"},
    {"costumer": "maria", "dish": "hamburguer", "day": "terça-feira"},
    {"costumer": "joao", "dish": "hamburguer", "day": "terça-feira"},
    {"costumer": "maria", "dish": "pizza", "day": "terça-feira"},
    {"costumer": "maria", "dish": "coxinha", "day": "segunda-feira"},
    {"costumer": "arnaldo", "dish": "misto-quente", "day": "terça-feira"},
    {"costumer": "jose", "dish": "hamburguer", "day": "sabado"},
    {"costumer": "maria", "dish": "hamburguer", "day": "terça-feira"},
]


class TestTrackOrders:
    def test___init___without_arg(self):
        class_instance = TrackOrders()
        expected_orders = []

        assert class_instance.orders == expected_orders

    def test___init___with_arg(self):
        class_instance = TrackOrders(orders_mock)
        expected_orders = orders_mock

        assert class_instance.orders == expected_orders

    def test_add_new_order(self):
        class_instance = TrackOrders()
        class_instance.add_new_order("maria", "hamburguer", "terça-feira")
        expected_orders = [
            {"costumer": "maria", "dish": "hamburguer", "day": "terça-feira"},
        ]

        assert class_instance.orders == expected_orders

    def test_get_most_ordered_dish_per_costumer(self):
        class_instance = TrackOrders(orders_mock)
        expected = "hamburguer"
        returned = class_instance.get_most_ordered_dish_per_costumer("maria")

        assert returned == expected

    def test_get_order_frequency_per_costumer(self):
        class_instance = TrackOrders(orders_mock)
        expected = 0
        returned = class_instance.get_order_frequency_per_costumer(
            "arnaldo",
            "hamburguer"
        )

        assert returned == expected

    def test_get_dish_quantity_per_costumer(self):
        class_instance = TrackOrders(orders_mock)
        expected = 0
        returned = class_instance.get_dish_quantity_per_costumer(
            "arnaldo",
            "hamburguer"
        )

        assert returned == expected

    def test_get_never_ordered_per_costumer(self):
        class_instance = TrackOrders(orders_mock)
        expected = {"pizza", "misto-quente", "coxinha"}
        returned = class_instance.get_never_ordered_per_costumer("joao")

        assert returned == expected

    def test_get_busiest_day(self):
        class_instance = TrackOrders(orders_mock)
        expected = "terça-feira"
        returned = class_instance.get_busiest_day()

        assert returned == expected

    def test_get_least_busy_day(self):
        class_instance = TrackOrders(orders_mock)
        expected = "segunda-feira"
        returned = class_instance.get_least_busy_day()

        assert returned == expected

    def test_get_days_never_visited_per_costumer(self):
        class_instance = TrackOrders(orders_mock)
        expected = {"segunda-feira", "sabado"}
        returned = class_instance.get_days_never_visited_per_costumer("joao")

        assert returned == expected
