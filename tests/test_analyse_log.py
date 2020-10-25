# Crie uma suíte de testes para o método analyse_log
# Obtenha, no mínimo, 90% de cobertura

from unittest.mock import patch, mock_open
from src.analyse_log import (
    get_orders_from_csv_file,
    get_most_ordered_dish_maria,
    get_hamburguer_quantity_arnaldo,
    get_never_ordered_joao,
    get_days_never_visited_joao,
    write_new_file,
)
import os


orders = [
    {"costumer": "maria", "dish": "hamburguer", "day": "terça-feira"},
    {"costumer": "joao", "dish": "hamburguer", "day": "terça-feira"},
    {"costumer": "maria", "dish": "pizza", "day": "terça-feira"},
    {"costumer": "maria", "dish": "coxinha", "day": "segunda-feira"},
    {"costumer": "arnaldo", "dish": "misto-quente", "day": "terça-feira"},
    {"costumer": "jose", "dish": "hamburguer", "day": "sabado"},
    {"costumer": "maria", "dish": "hamburguer", "day": "terça-feira"},
    {"costumer": "maria", "dish": "hamburguer", "day": "terça-feira"},
    {"costumer": "joao", "dish": "hamburguer", "day": "terça-feira"},
    {"costumer": "maria", "dish": "pizza", "day": "terça-feira"},
    {"costumer": "maria", "dish": "coxinha", "day": "segunda-feira"},
    {"costumer": "arnaldo", "dish": "misto-quente", "day": "terça-feira"},
    {"costumer": "jose", "dish": "hamburguer", "day": "sabado"},
    {"costumer": "maria", "dish": "hamburguer", "day": "terça-feira"},
    {"costumer": "maria", "dish": "hamburguer", "day": "terça-feira"},
    {"costumer": "joao", "dish": "hamburguer", "day": "terça-feira"},
    {"costumer": "maria", "dish": "pizza", "day": "terça-feira"},
    {"costumer": "maria", "dish": "coxinha", "day": "segunda-feira"},
    {"costumer": "arnaldo", "dish": "misto-quente", "day": "terça-feira"},
    {"costumer": "jose", "dish": "hamburguer", "day": "sabado"},
    {"costumer": "maria", "dish": "hamburguer", "day": "terça-feira"},
    {"costumer": "maria", "dish": "hamburguer", "day": "terça-feira"},
    {"costumer": "joao", "dish": "hamburguer", "day": "terça-feira"},
    {"costumer": "maria", "dish": "pizza", "day": "terça-feira"},
    {"costumer": "maria", "dish": "coxinha", "day": "segunda-feira"},
    {"costumer": "arnaldo", "dish": "misto-quente", "day": "terça-feira"},
    {"costumer": "jose", "dish": "hamburguer", "day": "sabado"},
    {"costumer": "maria", "dish": "hamburguer", "day": "terça-feira"},
    {"costumer": "maria", "dish": "hamburguer", "day": "terça-feira"},
    {"costumer": "joao", "dish": "hamburguer", "day": "terça-feira"},
    {"costumer": "maria", "dish": "pizza", "day": "terça-feira"},
    {"costumer": "maria", "dish": "coxinha", "day": "segunda-feira"},
    {"costumer": "arnaldo", "dish": "misto-quente", "day": "terça-feira"},
    {"costumer": "jose", "dish": "hamburguer", "day": "sabado"},
    {"costumer": "maria", "dish": "hamburguer", "day": "terça-feira"},
    {"costumer": "maria", "dish": "hamburguer", "day": "terça-feira"},
    {"costumer": "joao", "dish": "hamburguer", "day": "terça-feira"},
    {"costumer": "maria", "dish": "pizza", "day": "terça-feira"},
    {"costumer": "maria", "dish": "coxinha", "day": "segunda-feira"},
    {"costumer": "arnaldo", "dish": "misto-quente", "day": "terça-feira"},
    {"costumer": "jose", "dish": "hamburguer", "day": "sabado"},
    {"costumer": "maria", "dish": "hamburguer", "day": "terça-feira"},
    {"costumer": "maria", "dish": "hamburguer", "day": "terça-feira"},
    {"costumer": "joao", "dish": "hamburguer", "day": "terça-feira"},
    {"costumer": "maria", "dish": "pizza", "day": "terça-feira"},
    {"costumer": "maria", "dish": "coxinha", "day": "segunda-feira"},
    {"costumer": "arnaldo", "dish": "misto-quente", "day": "terça-feira"},
    {"costumer": "jose", "dish": "hamburguer", "day": "sabado"},
    {"costumer": "maria", "dish": "hamburguer", "day": "terça-feira"},
    {"costumer": "maria", "dish": "hamburguer", "day": "terça-feira"},
    {"costumer": "joao", "dish": "hamburguer", "day": "terça-feira"},
    {"costumer": "maria", "dish": "pizza", "day": "terça-feira"},
    {"costumer": "maria", "dish": "coxinha", "day": "segunda-feira"},
    {"costumer": "arnaldo", "dish": "misto-quente", "day": "terça-feira"},
    {"costumer": "jose", "dish": "hamburguer", "day": "sabado"},
    {"costumer": "maria", "dish": "hamburguer", "day": "terça-feira"},
]


class TestAnalyseLog:
    def test_get_orders_from_csv_file(self):
        expected = orders

        file_content_mock = """maria,hamburguer,terça-feira
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

        with patch(
            "builtins.open", mock_open(read_data=file_content_mock)
        ):
            assert get_orders_from_csv_file("dummy.csv") == expected

    def test_get_most_ordered_dish_maria(self):
        expected = "hamburguer"
        returned = get_most_ordered_dish_maria(orders)

        assert expected == returned

    def test_get_hamburguer_quantity_arnaldo(self):
        expected = 0
        returned = get_hamburguer_quantity_arnaldo(orders)

        assert expected == returned

    def test_get_never_ordered_joao(self):
        expected = set(["pizza", "misto-quente", "coxinha"])
        returned = get_never_ordered_joao(orders)

        assert expected == returned

    def test_get_days_never_visited_joao(self):
        expected = set(["segunda-feira", "sabado"])
        returned = get_days_never_visited_joao(orders)

        assert expected == returned

    def test_write_new_file(self):
        expected_content = (
            "hamburguer\n"
            + "0\n"
            + "{'misto-quente', 'pizza', 'coxinha'}\n"
            + "{'segunda-feira', 'sabado'}\n"
        )

        write_new_file([
            "hamburguer",
            "0",
            "{'misto-quente', 'pizza', 'coxinha'}",
            "{'segunda-feira', 'sabado'}",
        ])

        new_file_path = "data/mkt_campaign.txt"
        with open(new_file_path) as new_file:
            file_content = new_file.read()
        os.remove(new_file_path)

        assert expected_content == file_content
