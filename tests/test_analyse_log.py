from src.analyse_log import (analyse_log, get_maria_favorite_order, get_no_joao_days,
                             get_no_joao_orders, how_many_times_arnaldo_ordered_hamburguer)
from src.constants import (
    path_not_exists_csv, path_exists_csv, path_txt, expected_report)
import pytest
import os
from unittest.mock import patch


def test_analyse_log_file_not_exist():
    with pytest.raises(ValueError,
                       match="Arquivo not_exist.csv não encontrado"):
        analyse_log(path_not_exists_csv)


def test_get_no_joao_orders():
    data = [{"name": "joao", "order": "amora", "day": "segunda-feira"},
            {"name": "maria", "order": "peixe", "day": "quarta-feira"},
            {"name": "joao", "order": "torta", "day": "quinta-feira"}]
    assert get_no_joao_orders(data) == '- peixe'


def test_get_no_joao_days():
    data = [{"name": "joao", "order": "amora", "day": "segunda-feira"},
            {"name": "maria", "order": "peixe", "day": "quarta-feira"},
            {"name": "joao", "order": "torta", "day": "quinta-feira"}]
    assert get_no_joao_days(data) == '- quarta-feira'


def test_get_maria_favorite_order():
    data = [{"name": "maria", "order": "peixe", "day": "segunda-feira"},
            {"name": "maria", "order": "peixe", "day": "quarta-feira"},
            {"name": "maria", "order": "torta", "day": "segunda-feira"}]
    assert get_maria_favorite_order(data) == '- peixe'


def test_how_many_times_arnaldo_ordered_hamburguer():
    data = [{"name": "arnaldo", "order": "hamburguer", "day": "segunda-feira"},
            {"name": "arnaldo", "order": "peixe", "day": "quarta-feira"},
            {"name": "arnaldo", "order": "hamburguer", "day": "segunda-feira"}]
    assert how_many_times_arnaldo_ordered_hamburguer(data) == '- 2'


def test_analyse_log_file_not_exist():
    with pytest.raises(ValueError,
                       match="Arquivo not_exist.csv não encontrado"):
        analyse_log(path_not_exists_csv)


def test_analyse_log_save_file():
    analyse_log(path_exists_csv)
    assert os.path.exists(path_txt) is True
    os.remove(path_txt)


def test_analyse_log_file_content():
    with patch("src.analyse_log.export_txt") as export_txt_mock:
        analyse_log(path_exists_csv)
        export_txt_mock.assert_called_with(expected_report)
