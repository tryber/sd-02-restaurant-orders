# Crie uma suíte de testes para o método analyse_log
# Obtenha, no mínimo, 90% de cobertura

from src.analyse_log import (
    import_csv,
    most_requested_food,
    most_type_food,
    never_requested_meal,
    days_that_wasnt_in_place,
    check_path_and_format,
    analyse_log
)
from unittest.mock import patch, mock_open

mocked_resp = {
  'maria': {
    'Orders': ['hamburguer', 'pizza', 'coxinha', 'hamburguer'],
    'Days': ['terça-feira', 'terça-feira', 'segunda-feira', 'terça-feira']
  },
  'joao': {
    'Orders': ['hamburguer'],
    'Days': ['terça-feira']
  },
  'arnaldo': {
    'Orders': ['misto-quente'],
    'Days': ['terça-feira']
  }
}

mocked_all_days = {"segunda-feira", "terça-feira"}

mocked_all_foods = {"hamburguer", "coxinha", "misto-quente", "pizza"}


mocked_csv_data = """maria,hamburguer,terça-feira
joao,hamburguer,terça-feira
maria,pizza,terça-feira
maria,coxinha,segunda-feira
maria,hamburguer,terça-feira
arnaldo,misto-quente,terça-feira
"""


def test_analyse_log():
    with patch(
      "src.analyse_log.import_csv", return_value=(
          mocked_resp,
          mocked_all_days,
          mocked_all_foods,
        )
    ),  patch("builtins.open", mock_open()) as mock_write:
        analyse_log('test.csv')
        mock_write.return_value.write.assert_any_call("0\n")
        mock_write.return_value.write.assert_any_call("hamburguer\n")
        mock_write.return_value.write.assert_any_call(
          "{'segunda-feira'}"
          )


def test_import_csv_is_correct():
    with patch(
      "builtins.open", mock_open(read_data=mocked_csv_data)
    ):
        assert import_csv('test.csv') == (
          mocked_resp,
          mocked_all_days,
          mocked_all_foods,
        )


def test_check_path_and_format():
    assert check_path_and_format('test.csv', '.csv') is False
    assert check_path_and_format('test.csv', '.json') is True


def test_most_resquested_fodd():
    assert most_requested_food(mocked_resp['maria']) == 'hamburguer'


def test_most_type_food():
    assert most_type_food('hamburger', mocked_resp['arnaldo']['Orders']) == 0


def test_never_requested_meal():
    assert never_requested_meal(
      mocked_all_foods, mocked_resp['joao']['Orders']
    ) == {'pizza', 'misto-quente', 'coxinha'}


def test_days_that_wasnt_in_place():
    assert days_that_wasnt_in_place(
      mocked_all_days, mocked_resp['joao']['Days']
    ) == {'segunda-feira'}
