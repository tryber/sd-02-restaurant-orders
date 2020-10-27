from src.analyse_log import (
    format_dict,
    mais_pedido,
    comida_por_pessoa,
    analyse_log
)
from unittest.mock import patch, mock_open, call

mock_data = """maria,pizza,terça-feira
maria,hamburguer,terça-feira
joao,hamburguer,terça-feira
maria,coxinha,segunda-feira
arnaldo,misto-quente,terça-feira
jose,hamburguer,sabado
maria,hamburguer,terça-feira
maria,hamburguer,terça-feira
joao,hamburguer,terça-feira
"""

csv_mock = [
    {"name": "maria", "ingredient": "hamburguer", "day": "terça-feira"},
    {"name": "joao", "ingredient": "hamburguer", "day": "terça-feira"},
    {"name": "maria", "ingredient": "pizza", "day": "terça-feira"},
    {"name": "maria", "ingredient": "pizza", "day": "segunda-feira"},
]

expect_format_dict = {
    "joao": ({"terça-feira": 1, "hamburguer": 1}),
    "maria": (
        {
            "terça-feira": 2,
            "hamburguer": 1,
            "pizza": 2,
            "segunda-feira": 1,
        }
    ),
}
expect_valid_keys = {
    "days": {"segunda-feira", "terça-feira"},
    "ingredients": {"hamburguer", "pizza"},
    "names": {"joao", "maria"},
}


def test_format_dict():
    obj1, obj2 = format_dict(csv_mock)
    assert obj1 == expect_format_dict
    assert obj2 == expect_valid_keys


def test_mais_pedido():
    assert (
        mais_pedido(
            expect_format_dict["joao"], expect_valid_keys["ingredients"]
            )
        == "hamburguer"
    )
    assert (
        mais_pedido(
            expect_format_dict["maria"], expect_valid_keys["ingredients"]
            )
        == "pizza"
    )


def test_comida_por_pessoa():
    assert comida_por_pessoa(expect_format_dict["maria"], "pizza") == "2"
    assert comida_por_pessoa(expect_format_dict["joao"], "hamburguer") == "1"


def test_full_pass_analyse_log():
    with patch(
        "builtins.open",
            mock_open(read_data=mock_data)) as mock_file:
        analyse_log(mock_file)
        mock_file.return_value.write.assert_has_calls(
            [
                call("hamburguer\n"),
                call("0\n"),
                # call("{'pizza', 'coxinha', 'misto-quente'}\n"),
                # call("{'segunda-feira', 'sabado'}\n")
            ]
        )
