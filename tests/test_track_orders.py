from src.track_orders import TrackOrders

order_client = {
    "pedro": {
        "days": {"domingo", "sabado"},
        "couve": 3,
        "hamburguer": 1,
        "Most Frequent Value": 3,
        "Food most Frequent": "couve",
    },
    "isabela": {
        "days": {"segunda"},
        "hamburguer": 1,
        "Most Frequent Value": 1,
        "Food most Frequent": "hamburguer",
    },
}
orders_possible = {"couve", "hamburguer"}


def test_if_adds_new_order_get_a_correct_list_order():
    track = TrackOrders()
    track.add_new_order("pedro", "couve", "domingo")
    track.add_new_order("pedro", "couve", "domingo")
    track.add_new_order("pedro", "couve", "sabado")
    track.add_new_order("pedro", "hamburguer", "domingo")
    track.add_new_order("isabela", "hamburguer", "segunda")
    assert track.list_orders == order_client


def test_if_adds_new_order_get_a_correct_order_possible():
    track = TrackOrders()
    track.add_new_order("pedro", "couve", "domingo")
    track.add_new_order("pedro", "couve", "domingo")
    track.add_new_order("pedro", "couve", "sabado")
    track.add_new_order("pedro", "hamburguer", "domingo")
    track.add_new_order("isabela", "hamburguer", "segunda")
    assert track.orders_possible == orders_possible


def test_if_get_most_dish_correctly():
    track = TrackOrders()
    track.add_new_order("pedro", "couve", "domingo")
    track.add_new_order("pedro", "couve", "domingo")
    track.add_new_order("pedro", "couve", "sabado")
    track.add_new_order("pedro", "hamburguer", "domingo")
    track.add_new_order("isabela", "hamburguer", "segunda")
    assert track.get_most_ordered_dish_per_costumer("pedro") == "couve"


def test_times_specific_order_returns_correct():
    track = TrackOrders()
    track.add_new_order("pedro", "couve", "domingo")
    track.add_new_order("pedro", "couve", "domingo")
    track.add_new_order("pedro", "couve", "sabado")
    track.add_new_order("pedro", "hamburguer", "domingo")
    track.add_new_order("isabela", "hamburguer", "segunda")
    assert track.get_order_frequency_per_costumer("pedro", "couve") == 3


def test_not_asked_dish_return_correct():
    track = TrackOrders()
    track.add_new_order("pedro", "couve", "domingo")
    track.add_new_order("pedro", "couve", "domingo")
    track.add_new_order("pedro", "couve", "sabado")
    track.add_new_order("pedro", "hamburguer", "domingo")
    track.add_new_order("isabela", "hamburguer", "segunda")
    assert track.get_never_ordered_per_costumer("isabela") == {"couve"}


def test_get_days_never_visited_per_costumer_return_correct():
    track = TrackOrders()
    track.add_new_order("pedro", "couve", "domingo")
    track.add_new_order("pedro", "couve", "domingo")
    track.add_new_order("pedro", "couve", "sabado")
    track.add_new_order("pedro", "hamburguer", "domingo")
    track.add_new_order("isabela", "hamburguer", "segunda")
    assert track.get_days_never_visited_per_costumer("isabela") == {
        "segunda-feira",
        "terça-feira",
        "sabado",
    }
