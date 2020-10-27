from src.track_orders import TrackOrders


expect_infos = [
    {"name": "maria", "ingredient": "hamburguer", "day": "terça-feira"},
    {"name": "joao", "ingredient": "hamburguer", "day": "terça-feira"},
    {"name": "maria", "ingredient": "pizza", "day": "terça-feira"},
    {"name": "maria", "ingredient": "pizza", "day": "segunda-feira"},
]

expect_format_orders = {
    "joao": ({"terça-feira": 1, "hamburguer": 1}),
    "maria": (
        {
            "terça-feira": 2,
            "hamburguer": 1,
            "pizza": 2,
            "segunda-feira": 1,
        }
    ),
}

expect_value_keys = {
    "days": {"segunda-feira", "terça-feira"},
    "ingredients": {"hamburguer", "pizza"},
    "names": {"joao", "maria"},
}

track_test = TrackOrders()
track_test.add_new_order("maria", "hamburguer", "terça-feira")
track_test.add_new_order("joao", "hamburguer", "terça-feira")
track_test.add_new_order("maria", "pizza", "terça-feira")
track_test.add_new_order("maria", "pizza", "segunda-feira")


def test_add_new_order():
    assert track_test.infos == expect_infos
    assert track_test.format_orders == expect_format_orders
    assert track_test.value_keys == expect_value_keys


def test_get_most_ordered_dish_per_costumer():
    assert track_test.get_most_ordered_dish_per_costumer("maria") == "pizza"


def test_get_dish_quantity_per_costumer():
    assert track_test.get_dish_quantity_per_costumer("maria", "pizza") == 2


def test_get_never_ordered_per_costumer():
    assert track_test.get_never_ordered_per_costumer("joao") == "{'pizza'}"


def test_get_busiest_day():
    assert track_test.get_busiest_day() == "terça-feira"


def test_get_least_busy_day():
    assert track_test.get_least_busy_day() == "segunda-feira"
