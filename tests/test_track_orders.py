from src.track_orders import TrackOrders


def test_track_orders_add_new_order():
    track = TrackOrders()
    track.add_new_order("maria", "hamburguer", "terça-feira")
    assert track.data == [
        {"name": "maria", "order": "hamburguer", "day": "terça-feira"}]


def test_track_orders_get_most_ordered_dish_per_costumer():
    track = TrackOrders()
    track.add_new_order("maria", "hamburguer", "terça-feira")
    track.add_new_order("maria", "hamburguer", "segunda-feira")
    track.add_new_order("joão", "hamburguer", "quarta-feira")
    track.add_new_order("maria", "hamburguer", "quarta-feira")
    assert track.get_most_ordered_dish_per_costumer("maria") == "hamburguer"


def test_track_orders_get_order_frequency_per_costumer():
    track = TrackOrders()
    track.add_new_order("maria", "hamburguer", "terça-feira")
    track.add_new_order("maria", "hamburguer", "segunda-feira")
    track.add_new_order("joão", "hamburguer", "quarta-feira")
    track.add_new_order("maria", "hamburguer", "quarta-feira")
    assert track.get_order_frequency_per_costumer("maria", "hamburguer") == 3


def test_track_orders_get_order_frequency_per_costumer_0():
    track = TrackOrders()
    track.add_new_order("maria", "hamburguer", "terça-feira")
    track.add_new_order("maria", "hamburguer", "segunda-feira")
    track.add_new_order("joão", "peixe", "quarta-feira")
    track.add_new_order("maria", "hamburguer", "quarta-feira")
    assert track.get_order_frequency_per_costumer("maria", "peixe") == 0


def test_track_orders_get_never_ordered_per_costumer():
    track = TrackOrders()
    track.add_new_order("maria", "hamburguer", "terça-feira")
    track.add_new_order("maria", "coxinha", "segunda-feira")
    track.add_new_order("joão", "peixe", "quarta-feira")
    assert track.get_never_ordered_per_costumer("maria") == "peixe"


def test_get_days_never_visited_per_costumer():
    track = TrackOrders()
    track.add_new_order("maria", "hamburguer", "terça-feira")
    track.add_new_order("maria", "coxinha", "segunda-feira")
    track.add_new_order("joão", "peixe", "quarta-feira")
    assert track.get_days_never_visited_per_costumer("maria") == "quarta-feira"
