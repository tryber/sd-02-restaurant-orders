from src.track_orders import TrackOrders
import unittest
from unittest.mock import patch, mock_open, call

mock_csv = [
    ["eduarda", "pizza", "sexta-feira"],
    ["eduarda", "rocambole", "sexta-feira"],
    ["joao", "rocambole", "sexta-feira"],
    ["eduarda", "coxinha", "segunda-feira"],
    ["arnaldo", "misto-quente", "sexta-feira"],
    ["jose", "rocambole", "sabado"],
    ["eduarda", "rocambole", "sexta-feira"],
    ["eduarda", "rocambole", "sexta-feira"],
    ["joao", "rocambole", "sexta-feira"]
]


class Testing_TrackOrders(unittest.TestCase):
    def test_init(self):
        track = TrackOrders()
        assert {} == track.all_sales
        assert set() == track.days
        assert set() == track.orders

    def test_add_new_order(self):
        track = TrackOrders()
        for name, meal, day in mock_csv:
            track.add_new_order(name, meal, day)
        assert {
            "arnaldo": {"days": {"sexta-feira": 1},
                        "order": {"misto-quente": 1}},
            "joao": {"days": {"sexta-feira": 2}, "order": {"rocambole": 2}},
            "jose": {"days": {"sabado": 1}, "order": {"rocambole": 1}},
            "eduarda": {"days": {"segunda-feira": 1, "sexta-feira": 4},
                        "order": {"coxinha": 1, "rocambole": 3, "pizza": 1}}
        } == track.all_sales
        assert {
            "sabado", "segunda-feira", "sexta-feira"
        } == track.days
        self.assertEqual(set(
            {"coxinha", "rocambole", "misto-quente", "pizza"}
        ), track.orders)

    def test_get_most_ordered_dish_per_costumer(self):
        track = TrackOrders()
        for name, meal, day in mock_csv:
            track.add_new_order(name, meal, day)
        result = track.get_most_ordered_dish_per_costumer("eduarda")
        assert result == "rocambole"

    def test_get_order_frequency_per_costumer(self):
        track = TrackOrders()
        for name, meal, day in mock_csv:
            track.add_new_order(name, meal, day)
        result1 = track.get_order_frequency_per_costumer(
            "eduarda", "rocambole")
        result2 = track.get_order_frequency_per_costumer("eduarda", "jiló")
        assert result1 == 3
        assert result2 == 0

    def test_get_never_orderes_per_costumer(self):
        track = TrackOrders()
        for name, meal, day in mock_csv:
            track.add_new_order(name, meal, day)
        result = track.get_never_ordered_per_costumer("eduarda")
        assert result == {"misto-quente"}

    def test_get_days_never_visited_per_costumer(self):
        track = TrackOrders()
        for name, meal, day in mock_csv:
            track.add_new_order(name, meal, day)
        result = track.get_days_never_visited_per_costumer("eduarda")
        assert result == {"sabado"}

# Obtenha, no mínimo, 90% de cobertura
