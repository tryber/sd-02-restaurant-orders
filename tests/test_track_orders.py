from src.track_orders import TrackOrders


tracker_test = TrackOrders()


class TestTrackOrders:
    def test_init(self):
        assert tracker_test.orders_log == []

    def test_track_orders(self):
        tracker_test.add_new_order("laurolyra", "cuscuz", "segunda-feira")
        tracker_test.add_new_order("laurolyra", "cuscuz", "segunda-feira")
        tracker_test.add_new_order("laurolyra", "macaxeira", "domingo")
        tracker_test.add_new_order("Paula", "strogonoff", "sexta-feira")
        assert tracker_test.orders_log == [
            {"cliente": "laurolyra", "pedido": "cuscuz", "dia": "segunda-feira"},
            {"cliente": "laurolyra", "pedido": "cuscuz", "dia": "segunda-feira"},
            {"cliente": "laurolyra", "pedido": "macaxeira", "dia": "domingo"},
            {"cliente": "Paula", "pedido": "strogonoff", "dia": "sexta-feira"},
        ]

    def test_get_most_ordered_dish_per_costumer(self):
        result = tracker_test.get_most_ordered_dish_per_costumer("laurolyra")
        expected_result = "cuscuz"
        assert result == expected_result

    def test_get_order_frequency_per_costumer(self):
        result = tracker_test.get_order_frequency_per_costumer("laurolyra", "cuscuz")
        expected_result = 2
        assert result == expected_result

        result = tracker_test.get_order_frequency_per_costumer("laurolyra", "strogonoff")
        expected_result = 0
        assert result == expected_result

    def test_get_never_ordered_per_costumer(self):
        result = tracker_test.get_never_ordered_per_costumer("Paula")
        expected_result = {"macaxeira", "cuscuz"}
        assert result == expected_result

    def test_get_days_never_visited_per_costumer(self):
        result = tracker_test.get_days_never_visited_per_costumer("Paula")
        expected_result = {"domingo", "segunda-feira"}
        assert result == expected_result