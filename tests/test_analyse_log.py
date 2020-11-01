from unittest.mock import patch, mock_open, call
from io import StringIO
from src.analyse_log import analyse_log, get_most_ordered_dish_per_costumer

csv_content = StringIO("""
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
maria,hamburguer,terça-feira
""")

all_orders = [
    {'cliente': 'maria', 'pedido': 'hamburguer', 'dia': 'terça-feira'},
    {'cliente': 'joao', 'pedido': 'hamburguer', 'dia': 'terça-feira'},
    {'cliente': 'maria', 'pedido': 'pizza', 'dia': 'terça-feira'},
    {'cliente': 'maria', 'pedido': 'coxinha', 'dia': 'segunda-feira'},
    {'cliente': 'arnaldo', 'pedido': 'misto-quente', 'dia': 'terça-feira'},
    {'cliente': 'jose', 'pedido': 'hamburguer', 'dia': 'sabado'},
    {'cliente': 'maria', 'pedido': 'hamburguer', 'dia': 'terça-feira'},
    {'cliente': 'maria', 'pedido': 'hamburguer', 'dia': 'terça-feira'},
    {'cliente': 'joao', 'pedido': 'hamburguer', 'dia': 'terça-feira'},
    {'cliente': 'maria', 'pedido': 'pizza', 'dia': 'terça-feira'},
    {'cliente': 'maria', 'pedido': 'coxinha', 'dia': 'segunda-feira'},
    {'cliente': 'arnaldo', 'pedido': 'misto-quente', 'dia': 'terça-feira'},
    {'cliente': 'jose', 'pedido': 'hamburguer', 'dia': 'sabado'},
    {'cliente': 'maria', 'pedido': 'hamburguer', 'dia': 'terça-feira'},
    {'cliente': 'maria', 'pedido': 'hamburguer', 'dia': 'terça-feira'},
    {'cliente': 'joao', 'pedido': 'hamburguer', 'dia': 'terça-feira'},
    {'cliente': 'maria', 'pedido': 'pizza', 'dia': 'terça-feira'},
    {'cliente': 'maria', 'pedido': 'coxinha', 'dia': 'segunda-feira'},
    {'cliente': 'arnaldo', 'pedido': 'misto-quente', 'dia': 'terça-feira'},
    {'cliente': 'jose', 'pedido': 'hamburguer', 'dia': 'sabado'},
    {'cliente': 'maria', 'pedido': 'hamburguer', 'dia': 'terça-feira'},
    {'cliente': 'maria', 'pedido': 'hamburguer', 'dia': 'terça-feira'},
    {'cliente': 'joao', 'pedido': 'hamburguer', 'dia': 'terça-feira'},
    {'cliente': 'maria', 'pedido': 'pizza', 'dia': 'terça-feira'},
    {'cliente': 'maria', 'pedido': 'coxinha', 'dia': 'segunda-feira'},
    {'cliente': 'arnaldo', 'pedido': 'misto-quente', 'dia': 'terça-feira'},
    {'cliente': 'jose', 'pedido': 'hamburguer', 'dia': 'sabado'},
    {'cliente': 'maria', 'pedido': 'hamburguer', 'dia': 'terça-feira'},
    {'cliente': 'maria', 'pedido': 'hamburguer', 'dia': 'terça-feira'},
    {'cliente': 'joao', 'pedido': 'hamburguer', 'dia': 'terça-feira'},
    {'cliente': 'maria', 'pedido': 'pizza', 'dia': 'terça-feira'},
    {'cliente': 'maria', 'pedido': 'coxinha', 'dia': 'segunda-feira'},
    {'cliente': 'arnaldo', 'pedido': 'misto-quente', 'dia': 'terça-feira'},
    {'cliente': 'jose', 'pedido': 'hamburguer', 'dia': 'sabado'},
    {'cliente': 'maria', 'pedido': 'hamburguer', 'dia': 'terça-feira'},
    {'cliente': 'maria', 'pedido': 'hamburguer', 'dia': 'terça-feira'},
    {'cliente': 'joao', 'pedido': 'hamburguer', 'dia': 'terça-feira'},
    {'cliente': 'maria', 'pedido': 'pizza', 'dia': 'terça-feira'},
    {'cliente': 'maria', 'pedido': 'coxinha', 'dia': 'segunda-feira'},
    {'cliente': 'arnaldo', 'pedido': 'misto-quente', 'dia': 'terça-feira'},
    {'cliente': 'jose', 'pedido': 'hamburguer', 'dia': 'sabado'},
    {'cliente': 'maria', 'pedido': 'hamburguer', 'dia': 'terça-feira'},
    {'cliente': 'maria', 'pedido': 'hamburguer', 'dia': 'terça-feira'},
    {'cliente': 'joao', 'pedido': 'hamburguer', 'dia': 'terça-feira'},
    {'cliente': 'maria', 'pedido': 'pizza', 'dia': 'terça-feira'},
    {'cliente': 'maria', 'pedido': 'coxinha', 'dia': 'segunda-feira'},
    {'cliente': 'arnaldo', 'pedido': 'misto-quente', 'dia': 'terça-feira'},
    {'cliente': 'jose', 'pedido': 'hamburguer', 'dia': 'sabado'},
    {'cliente': 'maria', 'pedido': 'hamburguer', 'dia': 'terça-feira'},
    {'cliente': 'maria', 'pedido': 'hamburguer', 'dia': 'terça-feira'},
    {'cliente': 'joao', 'pedido': 'hamburguer', 'dia': 'terça-feira'},
    {'cliente': 'maria', 'pedido': 'pizza', 'dia': 'terça-feira'},
    {'cliente': 'maria', 'pedido': 'coxinha', 'dia': 'segunda-feira'},
    {'cliente': 'arnaldo', 'pedido': 'misto-quente', 'dia': 'terça-feira'},
    {'cliente': 'jose', 'pedido': 'hamburguer', 'dia': 'sabado'},
    {'cliente': 'maria', 'pedido': 'hamburguer', 'dia': 'terça-feira'}
]


def test_get_most_ordered_dish_per_costumer():
    result = get_most_ordered_dish_per_costumer(all_orders, 'maria')
    expected_result = "hamburguer"
    assert result == expected_result


# def test_analyse_log():
#     # expected_lines = [
#     #         f"{str('hamburguer')}\n",
#     #         f"{str(0)}\n",
#     #         f"{str({'misto-quente', 'pizza', 'coxinha'})}\n",
#     #         f"{str({'segunda-feira', 'sabado'})}\n",
#     #     ]
#     with patch("builtins.open", mock_open(read_data=csv_content)) as file:
#         analyse_log(csv_content)
#         file.return_value.writelines.asset_has_calls([
#             call("hamburguer\n")
#         ])
    