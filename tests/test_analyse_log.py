# Crie uma suíte de testes para o método analyse_log
# Obtenha, no mínimo, 90% de cobertura
from unittest.mock import (
    patch,
    mock_open,
)

from src.analyse_log import (
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
{"pizza", "coxinha", "misto-quente"}
{"sabado", "segunda-feira"}
"""


def test_create_orders_log():
    load_mock = mock_open(read_data=csv_mock)
    with patch("builtins.open", load_mock):
        result = create_orders_log('dummy.csv')
        assert orders_log_mock == result


def test_most_ordered_meal():
    result = most_ordered_meal(orders_log_mock, "maria")
    assert 'hamburguer' == result


def test_meals_from_customer():
    result = meals_from_customer(orders_log_mock, 'arnaldo', 'hamburguer')
    assert 0 == result


# @pytest.mark.parametrize("id,expected", [
# # (0, 'hamburger\n'),
# (1, 0),
# (2, {'coxinha', 'misto-quente', 'pizza'}),
# (3, {'sabado', 'segunda-feira'})
# ]) - iteração sobre os testes
def test_write_file():  # se for iterar, usar (id, expected)
    load_mock = mock_open(read_data=csv_mock)
    with patch("builtins.open", load_mock) as mocked_file:
        line_1 = most_ordered_meal(orders_log_mock, "maria")
        line_2 = meals_from_customer(orders_log_mock, "arnaldo", "hamburguer")
        line_3 = meals_never_asked(orders_log_mock, "joao")
        line_4 = days_never_visited(orders_log_mock, "joao")
        write_file([line_1, line_2, line_3, line_4])
        # assert eval
        # (mocked_file.return_value.writelines.mock_calls[0].args[0][id])
        # == expected
        # - iteração sobre os testes
        a, b, c, d = mocked_file.return_value.writelines.mock_calls[0].args[0]
        assert a == 'hamburguer\n'
        assert b == '0\n'
        assert eval(c) == {'coxinha', 'misto-quente', 'pizza'}
        assert eval(d) == {'sabado', 'segunda-feira'}
