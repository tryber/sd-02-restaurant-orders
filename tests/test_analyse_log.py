# Crie uma suíte de testes para o método analyse_log
# Obtenha, no mínimo, 90% de cobertura
from unittest.mock import (
    patch,
    mock_open,
    call,
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

# def test_read_csv_if_return_correct():
#     mock_opened = mock_open(read_data=csv_mock)
#     with patch("builtins.open", mock_opened):
#         result = sys.path.create_orders_log('dummy.csv')
#         assert orders_log_mock == result
