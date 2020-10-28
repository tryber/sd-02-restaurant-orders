from src.track_orders import TrackOrders
import unittest
from unittest.mock import patch, mock_open, call

mock_csv = [
    ['eduarda', 'pizza', 'sexta-feira'],
    ['eduarda', 'rocambole', 'sexta-feira'],
    ['joao', 'rocambole', 'sexta-feira'],
    ['eduarda', 'coxinha', 'segunda-feira'],
    ['arnaldo', 'misto-quente', 'sexta-feira'],
    ['jose', 'rocambole', 'sabado'],
    ['eduarda', 'rocambole', 'sexta-feira'],
    ['eduarda', 'rocambole', 'sexta-feira'],
    ['joao', 'rocambole', 'sexta-feira']
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
            'arnaldo': {'days': {'sexta-feira': 1},
                        'order': {'misto-quente': 1}},
            'joao': {'days': {'sexta-feira': 2}, 'order': {'rocambole': 2}},
            'jose': {'days': {'sabado': 1}, 'order': {'rocambole': 1}},
            'eduarda': {'days': {'segunda-feira': 1, 'sexta-feira': 4},
                        'order': {'coxinha': 1, 'rocambole': 3, 'pizza': 1}}
        } == track.all_sales
        assert {
            'sabado', 'segunda-feira', 'sexta-feira'
        } == track.days
        self.assertEqual(set(
            {'coxinha', 'rocambole', 'misto-quente', 'pizza'}
        ), track.orders)

# Obtenha, no mínimo, 90% de cobertura
