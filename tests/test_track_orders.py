from src.track_orders import TrackOrders
import unittest
from unittest.mock import patch, mock_open, call

csv_parsed = [
    ['maria', 'pizza', 'terça-feira'],
    ['maria', 'hamburguer', 'terça-feira'],
    ['joao', 'hamburguer', 'terça-feira'],
    ['maria', 'coxinha', 'segunda-feira'],
    ['arnaldo', 'misto-quente', 'terça-feira'],
    ['jose', 'hamburguer', 'sabado'],
    ['maria', 'hamburguer', 'terça-feira'],
    ['maria', 'hamburguer', 'terça-feira'],
    ['joao', 'hamburguer', 'terça-feira']
]


class MyTest(unittest.TestCase):
    def test_class_init_correct(self):
        test = TrackOrders()
        assert {} == test.sales
        assert {} == test.orders_by_day
        assert set() == test.all_days
        assert set() == test.all_orders

    def test_add_new_order_in_class_correct(self):
        test = TrackOrders()
        test.add_new_order('johnatas', 'frango', 'domingo')
        assert {'johnatas': {'days': {'domingo': 1},
                             'foods': {'frango': 1}}} == test.sales
        assert {'domingo': 1} == test.orders_by_day
        assert set({'frango'}) == test.all_orders
        assert set({'domingo'}) == test.all_days

    def test_add_many_new_orders_in_class_correct(self):
        test = TrackOrders()
        for name, food, day in csv_parsed:
            test.add_new_order(name, food, day)
        assert {
            'arnaldo': {'days': {'terça-feira': 1},
                        'foods': {'misto-quente': 1}},
            'joao': {'days': {'terça-feira': 2}, 'foods': {'hamburguer': 2}},
            'jose': {'days': {'sabado': 1}, 'foods': {'hamburguer': 1}},
            'maria': {'days': {'segunda-feira': 1, 'terça-feira': 4},
                      'foods': {'coxinha': 1, 'hamburguer': 3, 'pizza': 1}}
        } == test.sales
        assert {
            'sabado': 1, 'segunda-feira': 1, 'terça-feira': 7
        } == test.orders_by_day
        self.assertEqual(set(
            {'coxinha', 'hamburguer', 'misto-quente', 'pizza'}
        ), test.all_orders)
        self.assertEqual(
            set({'segunda-feira', 'sabado', 'terça-feira'}), test.all_days)

    def test_get_most_ordered_dish_per_costumer_correct(self):
        test = TrackOrders()
        for name, food, day in csv_parsed:
            test.add_new_order(name, food, day)
        result = test.get_most_ordered_dish_per_costumer('maria')
        assert 'hamburguer' == result

    def test_get_order_frequency_per_costumer_correct(self):
        test = TrackOrders()
        for name, food, day in csv_parsed:
            test.add_new_order(name, food, day)
        result = test.get_order_frequency_per_costumer('maria', 'hamburguer')
        assert 3 == result

    def test_get_never_ordered_per_costumer_correct(self):
        test = TrackOrders()
        for name, food, day in csv_parsed:
            test.add_new_order(name, food, day)
        result = test.get_never_ordered_per_costumer('joao')
        self.assertEqual(
            set({'coxinha', 'misto-quente', 'pizza'}), result)

    def test_get_days_never_visited_per_costumer_correct(self):
        test = TrackOrders()
        for name, food, day in csv_parsed:
            test.add_new_order(name, food, day)
        result = test.get_days_never_visited_per_costumer('joao')
        self.assertEqual(
            set({'sabado', 'segunda-feira'}), result)

    def test_get_busiest_day_correct(self):
        test = TrackOrders()
        for name, food, day in csv_parsed:
            test.add_new_order(name, food, day)
        result = test.get_busiest_day()
        self.assertEqual('terça-feira', result)

    def test_get_least_busy_day_correct(self):
        test = TrackOrders()
        for name, food, day in csv_parsed:
            test.add_new_order(name, food, day)
            result = test.get_least_busy_day()
        self.assertEqual('segunda-feira', result)
