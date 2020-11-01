from unittest.mock import patch, mock_open, call
from io import StringIO
from src.analyse_log import (
    analyse_log,
    get_most_ordered_dish_per_costumer,
    get_order_frequency_per_costumer,
    get_never_ordered_per_costumer,
    get_days_never_visited_per_costumer,
)

csv_content = """
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
maria,hamburguer,terça-feira
joao,hamburguer,terça-feira
maria,pizza,terça-feira
maria,coxinha,segunda-feira
arnaldo,misto-quente,terça-feira
jose,hamburguer,sabado
maria,hamburguer,terça-feira"""

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


def test_analyse_log():
    expected_lines = [
        "hamburguer\n",
        "0\n",
        "{'misto-quente', 'pizza', 'coxinha'}\n",
        "{'segunda-feira', 'sabado'}\n",
    ]
    with patch("builtins.open", mock_open(read_data=csv_content)) as mock_file:
        analyse_log(mock_file)
        mock_file.return_value.writelines.assert_called_once_with(
            expected_lines
        )
