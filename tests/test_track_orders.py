from src.track_orders import TrackOrders


class TestTrackOrders:
    def fill_add_new_order(self):
        tracker = TrackOrders()
        tracker.clients = {
            "joao": {"orders": {"hamburguer": 8}, "week_days": {
                "terça-feira": 8,
                }},
            "maria": {
                "orders": {"pizza": 8, "coxinha": 8, "hamburguer": 15},
                "week_days": {"terça-feira": 23, "segunda-feira": 8},
            },
            "arnaldo": {"orders": {"misto-quente": 8}, "week_days": {
                "terça-feira": 8,
                }},
            "jose": {"orders": {"hamburguer": 8}, "week_days": {"sabado": 8}},
        }
        tracker.all_orders = {"misto-quente", "pizza", "hamburguer", "coxinha"}
        tracker.all_week_days = {"terça-feira", "sabado", "segunda-feira"}
        return tracker

    def test_add_new_order(self):
        # arrange
        expected = {
            "maria": {"orders": {"hamburguer": 1}, "week_days": {
                "terça-feira": 1,
                }}
        }
        tracker = TrackOrders()

        # act
        tracker.add_new_order("maria", "hamburguer", "terça-feira")

        #  assert
        assert tracker.clients == expected

    def test_get_most_ordered_dish_per_costumer(self):
        # arrange
        tracker = TestTrackOrders.fill_add_new_order(self)
        expected = "hamburguer"

        # act
        received = tracker.get_most_ordered_dish_per_costumer("maria")

        # assert
        assert received == expected

    def test_get_order_frequency_per_costumer(self):
        # arrange
        tracker = TestTrackOrders.fill_add_new_order(self)
        expected = 0

        # act
        received = tracker.get_order_frequency_per_costumer(
            "arnaldo",
            "hamburguer",
        )

        # assert
        assert received == expected

    def test_get_never_ordered_per_costumer(self):
        # arrange
        tracker = TestTrackOrders.fill_add_new_order(self)
        expected = {"coxinha", "misto-quente", "pizza"}

        # act
        received = tracker.get_never_ordered_per_costumer("joao")

        # assert
        assert received == expected

    def test_get_days_never_visited_per_costumer(self):
        # arrange
        tracker = TestTrackOrders.fill_add_new_order(self)
        expected = {"sabado", "segunda-feira"}

        # act
        received = tracker.get_days_never_visited_per_costumer("joao")

        # assert
        assert received == expected
