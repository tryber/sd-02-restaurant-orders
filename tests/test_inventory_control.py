from src.inventory_control import InventoryControl
from src.constants import (expected_print_order_1, expected_print_order_2)
from src.main import main


def test_add_new_order():
    inventory = InventoryControl()
    inventory.add_new_order("maria", "hamburguer", "segunda-feira")
    assert inventory.current_inventory == {
        'pao': 49,
        'hamburguer': 34,
        'queijo': 99,
        'molho': 30,
        'presunto': 20,
        'massa': 20,
        'frango': 10,
    }


def test_get_shopping_list():
    inventory = InventoryControl()
    inventory.add_new_order("maria", "hamburguer", "segunda-feira")
    assert inventory.get_shopping_list() == {
        'pao': 1,
        'hamburguer': 1,
        'queijo': 1,
        'molho': 0,
        'presunto': 0,
        'massa': 0,
        'frango': 0,
    }


def test_get_available_dishes_all():
    inventory = InventoryControl()
    inventory.add_new_order("maria", "hamburguer", "segunda-feira")
    assert inventory.get_available_dishes(
    ) == ['hamburguer', 'pizza', 'misto-quente', 'coxinha']


def test_get_available_dishes():
    inventory = InventoryControl()
    for i in range(100):
        inventory.add_new_order("maria", "hamburguer", "segunda-feira")
    assert inventory.get_available_dishes(
    ) == ['coxinha']


def test_main_with_order_1(capsys):
    main("data/orders_1.csv")
    out, err = capsys.readouterr()
    assert out == expected_print_order_1


def test_main_with_order_2(capsys):
    main("data/orders_2.csv")
    out, err = capsys.readouterr()
    assert out == expected_print_order_2
