from unittest.mock import patch, mock_open
from src.analyse_log import (
    analyse_log,
    get_most_ordered_dish_per_costumer,
    get_order_frequency_per_costumer,
    get_never_ordered_per_costumer,
    get_days_never_visited_per_costumer,
    extract_orders_from_csv,
)

csv_content = """maria,hamburguer,terça-feira
joao,hamburguer,terça-feira
maria,pizza,terça-feira
maria,coxinha,segunda-feira
arnaldo,misto-quente,terça-feira
jose,hamburguer,sabado
maria,hamburguer,terça-feira
maria,hamburguer,terça-feira
joao,hamburguer,terça-feira
maria,pizza,terça-feira
maria,coxinha,segunda-feira
arnaldo,misto-quente,terça-feira
jose,hamburguer,sabado
maria,hamburguer,terça-feira
maria,hamburguer,terça-feira
joao,hamburguer,terça-feira
maria,pizza,terça-feira
maria,coxinha,segunda-feira
arnaldo,misto-quente,terça-feira
jose,hamburguer,sabado
maria,hamburguer,terça-feira
maria,hamburguer,terça-feira
joao,hamburguer,terça-feira
maria,pizza,terça-feira
maria,coxinha,segunda-feira
arnaldo,misto-quente,terça-feira
jose,hamburguer,sabado
maria,hamburguer,terça-feira
maria,hamburguer,terça-feira
joao,hamburguer,terça-feira
maria,pizza,terça-feira
maria,coxinha,segunda-feira
arnaldo,misto-quente,terça-feira
jose,hamburguer,sabado
maria,hamburguer,terça-feira
maria,hamburguer,terça-feira
joao,hamburguer,terça-feira
maria,pizza,terça-feira
maria,coxinha,segunda-feira
arnaldo,misto-quente,terça-feira
jose,hamburguer,sabado
maria,hamburguer,terça-feira
maria,hamburguer,terça-feira
joao,hamburguer,terça-feira
maria,pizza,terça-feira
maria,coxinha,segunda-feira
arnaldo,misto-quente,terça-feira
jose,hamburguer,sabado
maria,hamburguer,terça-feira
maria,hamburguer,terça-feira
joao,hamburguer,terça-feira
maria,pizza,terça-feira
maria,coxinha,segunda-feira
arnaldo,misto-quente,terça-feira
jose,hamburguer,sabado
maria,hamburguer,terça-feira
"""

all_orders = [
    {"cliente": "maria", "pedido": "hamburguer", "dia": "terça-feira"},
    {"cliente": "joao", "pedido": "hamburguer", "dia": "terça-feira"},
    {"cliente": "maria", "pedido": "pizza", "dia": "terça-feira"},
    {"cliente": "maria", "pedido": "coxinha", "dia": "segunda-feira"},
    {"cliente": "arnaldo", "pedido": "misto-quente", "dia": "terça-feira"},
    {"cliente": "jose", "pedido": "hamburguer", "dia": "sabado"},
    {"cliente": "maria", "pedido": "hamburguer", "dia": "terça-feira"},
    {"cliente": "maria", "pedido": "hamburguer", "dia": "terça-feira"},
    {"cliente": "joao", "pedido": "hamburguer", "dia": "terça-feira"},
    {"cliente": "maria", "pedido": "pizza", "dia": "terça-feira"},
    {"cliente": "maria", "pedido": "coxinha", "dia": "segunda-feira"},
    {"cliente": "arnaldo", "pedido": "misto-quente", "dia": "terça-feira"},
    {"cliente": "jose", "pedido": "hamburguer", "dia": "sabado"},
    {"cliente": "maria", "pedido": "hamburguer", "dia": "terça-feira"},
    {"cliente": "maria", "pedido": "hamburguer", "dia": "terça-feira"},
    {"cliente": "joao", "pedido": "hamburguer", "dia": "terça-feira"},
    {"cliente": "maria", "pedido": "pizza", "dia": "terça-feira"},
    {"cliente": "maria", "pedido": "coxinha", "dia": "segunda-feira"},
    {"cliente": "arnaldo", "pedido": "misto-quente", "dia": "terça-feira"},
    {"cliente": "jose", "pedido": "hamburguer", "dia": "sabado"},
    {"cliente": "maria", "pedido": "hamburguer", "dia": "terça-feira"},
    {"cliente": "maria", "pedido": "hamburguer", "dia": "terça-feira"},
    {"cliente": "joao", "pedido": "hamburguer", "dia": "terça-feira"},
    {"cliente": "maria", "pedido": "pizza", "dia": "terça-feira"},
    {"cliente": "maria", "pedido": "coxinha", "dia": "segunda-feira"},
    {"cliente": "arnaldo", "pedido": "misto-quente", "dia": "terça-feira"},
    {"cliente": "jose", "pedido": "hamburguer", "dia": "sabado"},
    {"cliente": "maria", "pedido": "hamburguer", "dia": "terça-feira"},
    {"cliente": "maria", "pedido": "hamburguer", "dia": "terça-feira"},
    {"cliente": "joao", "pedido": "hamburguer", "dia": "terça-feira"},
    {"cliente": "maria", "pedido": "pizza", "dia": "terça-feira"},
    {"cliente": "maria", "pedido": "coxinha", "dia": "segunda-feira"},
    {"cliente": "arnaldo", "pedido": "misto-quente", "dia": "terça-feira"},
    {"cliente": "jose", "pedido": "hamburguer", "dia": "sabado"},
    {"cliente": "maria", "pedido": "hamburguer", "dia": "terça-feira"},
    {"cliente": "maria", "pedido": "hamburguer", "dia": "terça-feira"},
    {"cliente": "joao", "pedido": "hamburguer", "dia": "terça-feira"},
    {"cliente": "maria", "pedido": "pizza", "dia": "terça-feira"},
    {"cliente": "maria", "pedido": "coxinha", "dia": "segunda-feira"},
    {"cliente": "arnaldo", "pedido": "misto-quente", "dia": "terça-feira"},
    {"cliente": "jose", "pedido": "hamburguer", "dia": "sabado"},
    {"cliente": "maria", "pedido": "hamburguer", "dia": "terça-feira"},
    {"cliente": "maria", "pedido": "hamburguer", "dia": "terça-feira"},
    {"cliente": "joao", "pedido": "hamburguer", "dia": "terça-feira"},
    {"cliente": "maria", "pedido": "pizza", "dia": "terça-feira"},
    {"cliente": "maria", "pedido": "coxinha", "dia": "segunda-feira"},
    {"cliente": "arnaldo", "pedido": "misto-quente", "dia": "terça-feira"},
    {"cliente": "jose", "pedido": "hamburguer", "dia": "sabado"},
    {"cliente": "maria", "pedido": "hamburguer", "dia": "terça-feira"},
    {"cliente": "maria", "pedido": "hamburguer", "dia": "terça-feira"},
    {"cliente": "joao", "pedido": "hamburguer", "dia": "terça-feira"},
    {"cliente": "maria", "pedido": "pizza", "dia": "terça-feira"},
    {"cliente": "maria", "pedido": "coxinha", "dia": "segunda-feira"},
    {"cliente": "arnaldo", "pedido": "misto-quente", "dia": "terça-feira"},
    {"cliente": "jose", "pedido": "hamburguer", "dia": "sabado"},
    {"cliente": "maria", "pedido": "hamburguer", "dia": "terça-feira"},
]


def test_get_most_ordered_dish_per_costumer():
    result = get_most_ordered_dish_per_costumer(all_orders, "maria")
    expected_result = "hamburguer"
    assert result == expected_result


def test_get_order_frequency_per_costumer():
    result = get_order_frequency_per_costumer(
        all_orders, "arnaldo", "hamburguer"
    )
    expected_result = 0
    assert result == expected_result


def test_get_never_ordered_per_costumer():
    result = get_never_ordered_per_costumer(all_orders, "joao")
    expected_result = {"pizza", "coxinha", "misto-quente"}
    assert result == expected_result


def test_get_days_never_visited_per_costumer():
    result = get_days_never_visited_per_costumer(all_orders, "joao")
    expected_result = {"segunda-feira", "sabado"}
    assert result == expected_result


def test_extract_orders_from_csv():
    with patch("builtins.open", mock_open(read_data=csv_content)):
        result = extract_orders_from_csv("file.csv")
        assert all_orders == result


def test_analyse_log():
    with patch(
        "src.analyse_log.extract_orders_from_csv", return_value=all_orders
    ), patch("builtins.open", mock_open()) as file:
        analyse_log("file.csv")
        file.return_value.write.assert_any_call("hamburguer\n")
        file.return_value.write.assert_any_call("0\n")
