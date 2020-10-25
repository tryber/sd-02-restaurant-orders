# Crie uma suíte de testes para o método analyse_log
# Obtenha, no mínimo, 90% de cobertura

from unittest.mock import patch, mock_open
from src.analyse_log import (
    analyse_log,
    get_orders_from_csv_file,
    get_most_ordered_dish_maria,
    get_hamburguer_quantity_arnaldo,
    get_never_ordered_joao,
    get_days_never_visited_joao,
    write_new_file,
)


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

orders_mock = [
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
    def test_get__mock_from_csv_file(self):
        expected = orders_mock

        with patch("builtins.open", mock_open(read_data=file_content_mock)):
            returned = get_orders_from_csv_file("dummy.csv")
            assert expected == returned

    def test_get_most_ordered_dish_maria(self):
        expected = "hamburguer"
        returned = get_most_ordered_dish_maria(orders_mock)

        assert expected == returned

    def test_get_hamburguer_quantity_arnaldo(self):
        expected = 0
        returned = get_hamburguer_quantity_arnaldo(orders_mock)

        assert expected == returned

    def test_get_never_ordered_joao(self):
        expected = set(["pizza", "misto-quente", "coxinha"])
        returned = get_never_ordered_joao(orders_mock)

        assert expected == returned

    def test_get_days_never_visited_joao(self):
        expected = set(["segunda-feira", "sabado"])
        returned = get_days_never_visited_joao(orders_mock)

        assert expected == returned

    def test_write_new_file(self):
        write_new_file_arg = [
            "hamburguer",
            0,
            {"misto-quente", "pizza", "coxinha"},
            {"segunda-feira", "sabado"},
        ]
        expected_writelines_arg = [
            f"{str('hamburguer')}\n",
            f"{str(0)}\n",
            f"{str({'misto-quente', 'pizza', 'coxinha'})}\n",
            f"{str({'segunda-feira', 'sabado'})}\n",
        ]

        with patch("builtins.open", mock_open()) as mocked_file:
            write_new_file(write_new_file_arg)

            mocked_file.return_value.writelines.assert_called_once_with(
                expected_writelines_arg
            )

    @patch("src.analyse_log.get_orders_from_csv_file")
    @patch("src.analyse_log.get_most_ordered_dish_maria")
    @patch("src.analyse_log.get_hamburguer_quantity_arnaldo")
    @patch("src.analyse_log.get_never_ordered_joao")
    @patch("src.analyse_log.get_days_never_visited_joao")
    @patch("src.analyse_log.write_new_file")
    def test_analyse_log_calls(
        self,
        write_new_file_mock,
        get_days_never_visited_joao_mock,
        get_never_ordered_joao_mock,
        get_hamburguer_quantity_arnaldo_mock,
        get_most_ordered_dish_maria_mock,
        get_orders_from_csv_file_mock,
    ):
        path_to_file_mock = "dummy.csv"
        get_orders_from_csv_file_mock.return_value = orders_mock
        get_most_ordered_dish_maria_mock.return_value = "hamburguer"
        get_hamburguer_quantity_arnaldo_mock.return_value = 0
        get_never_ordered_joao_mock.return_value = {
            "misto-quente",
            "pizza",
            "coxinha",
        }
        get_days_never_visited_joao_mock.return_value = {
            "segunda-feira",
            "sabado",
        }
        results_mock = [
            "hamburguer",
            0,
            {"misto-quente", "pizza", "coxinha"},
            {"segunda-feira", "sabado"},
        ]

        analyse_log(path_to_file_mock)

        get_orders_from_csv_file_mock.assert_called_once_with(
            path_to_file_mock
        )
        get_most_ordered_dish_maria_mock.assert_called_once_with(orders_mock)
        get_hamburguer_quantity_arnaldo_mock.assert_called_once_with(
            orders_mock,
        )
        get_never_ordered_joao_mock.assert_called_once_with(orders_mock)
        get_days_never_visited_joao_mock.assert_called_once_with(orders_mock)
        write_new_file_mock.assert_called_once_with(results_mock)
