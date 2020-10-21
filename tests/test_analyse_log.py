from src.analyse_log import analyse_log, read_csv, discover_items
from src.analyse_log import food_most_eaten_by, times_most_eaten
from src.analyse_log import items_that_was_not_asked, save_log
from unittest.mock import patch, mock_open, call

file_content_mock = """maria,pizza,terça-feira
maria,hamburguer,terça-feira
joao,hamburguer,terça-feira
maria,coxinha,segunda-feira
arnaldo,misto-quente,terça-feira
jose,hamburguer,sabado
maria,hamburguer,terça-feira
maria,hamburguer,terça-feira
joao,hamburguer,terça-feira
"""

file_no_content_mock = ""

csv_parsed = [
    ['maria', 'pizza', 'terça-feira'],
    ['maria', 'hamburguer', 'terça-feira'],
    ['joao', 'hamburguer', 'terça-feira'],
    ['maria', 'coxinha', 'segunda-feira'],
    ['arnaldo', 'misto-quente', 'terça-feira'],
    ['jose', 'hamburguer', 'sabado'],
    ['maria', 'hamburguer', 'terça-feira'],
    ['maria', 'hamburguer', 'terça-feira'],
    ['joao', 'hamburguer', 'terça-feira']
]

mock_saved = """hamburguer
0
{'coxinha', 'misto-quente', 'pizza'}
{'segunda-feira', 'sabado'}
"""


def test_full_pass_analyse_log():
    mock_opened = mock_open(read_data=file_content_mock)
    with patch("builtins.open", mock_opened) as mocked_file:
        analyse_log(mocked_file)
        mocked_file.return_value.write.assert_has_calls([
            call("hamburguer\n"),
            call("0\n"),
        ])


def test_analyse_log_file_null():
    mock_opened = mock_open(read_data=file_no_content_mock)
    with patch("builtins.open", mock_opened) as mocked_file:
        result = analyse_log(mocked_file)
        assert 'Arquivo vazio' in result


def test_read_csv_if_return_correct():
    mock_opened = mock_open(read_data=file_content_mock)
    with patch("builtins.open", mock_opened):
        result = read_csv('naoimporta.csv')
        assert csv_parsed == result


def test_discover_items_if_return_correct():
    result = discover_items(csv_parsed, column=1)
    assert {'coxinha', 'hamburguer', 'misto-quente', 'pizza'} == result


def test_food_most_eaten_by_if_return_correct():
    result = food_most_eaten_by('maria', csv_parsed)
    assert 'hamburguer' == result


def test_times_most_eaten_by_if_return_correct():
    result = times_most_eaten('maria', 'hamburguer', csv_parsed)
    assert 3 == result


def test_items_that_was_not_asked_if_return_correct():
    result = items_that_was_not_asked(
        'joao', csv_parsed, discover_items(csv_parsed, column=1), column=1)
    assert {'coxinha', 'misto-quente', 'pizza'} == result


def test_save_log_if_saves_to_file_correct():
    mock_opened = mock_open(read_data=file_content_mock)
    with patch("builtins.open", mock_opened) as mocked_file:
        line_1 = food_most_eaten_by('maria', csv_parsed)
        line_2 = times_most_eaten('arnaldo', 'hamburguer', csv_parsed)
        line_3 = items_that_was_not_asked(
            'joao', csv_parsed, discover_items(csv_parsed, column=1), column=1)
        line_4 = items_that_was_not_asked(
            'joao', csv_parsed, discover_items(csv_parsed, column=2), column=2)
        save_log([line_1, line_2, line_3, line_4])
        mocked_file.return_value.write.assert_has_calls([
            call("hamburguer\n"),
            call("0\n"),
        ])
