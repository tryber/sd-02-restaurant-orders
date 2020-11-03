# Crie uma suíte de testes para o método analyse_log
# Obtenha, no mínimo, 90% de cobertura
from unittest.mock import (
    patch,
    mock_open,
    call,
)

from src.analyse_log import (
    analyse_log,
    write_file,
    create_orders_log,
    days_never_visited,
    meals_from_customer,
    meals_never_asked,
    most_ordered_meal,
)

empty_csv_mock = ""

csv_mock = """maria,hamburguer,terça-feira
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

orders_log_mock = [
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

mkt_campaign_mock = """hamburguer
0
{'misto-quente', 'pizza', 'coxinha'}
{'segunda-feira', 'sabado'}
"""

def test_read_csv_if_return_correct():
    mock_opened = mock_open(read_data=csv_mock)
    with patch("builtins.open", mock_opened):
        result = create_orders_log('dummy.csv')
        assert orders_log_mock == result

def test_full_pass_analyse_log():
    mock_opened = mock_open(read_data=csv_mock)
    with patch("builtins.open", mock_opened) as mocked_file:
        analyse_log(mocked_file)
        mocked_file.return_value.write.assert_has_calls([
            call("hamburguer\n"),
            call("0\n"),
        ])

def test_analyse_log_file_null():
    mock_opened = mock_open(read_data=empty_csv_mock)
    with patch("builtins.open", mock_opened) as mocked_file:
        result = analyse_log(mocked_file)
        assert "Arquivo vazio" in result

def test_food_most_eaten_by_if_return_correct():
    result = most_ordered_meal(orders_log_mock, "maria")
    assert 'hamburguer' == result

def test_times_most_eaten_by_if_return_correct():
    result = meals_from_customer(orders_log_mock, 'maria', 'hamburguer')
    assert 3 == result

def test_save_log_if_saves_to_file_correct():
    mock_opened = mock_open(read_data=csv_mock)
    with patch("builtins.open", mock_opened) as mocked_file:
        all_results_mock = [
            most_ordered_meal(orders_log_mock, "maria"),
            meals_from_customer(orders_log_mock, "arnaldo", "hamburguer"),
            meals_never_asked(orders_log_mock, "joao"),
            days_never_visited(orders_log_mock, "joao")
        ]
        write_file(all_results_mock)
        mocked_file.return_value.write.assert_has_calls([
            call("hamburguer\n"),
            call("0\n"),
            call("{'coxinha', 'pizza', 'misto-quente'}\n"),
            call("{'segunda-feira', 'sabado'}\n")
        ])