from src.analyse_log import analyse_log
from src.constants import (
    path_not_exists_csv, path_exists_csv, path_txt, expected_report)
import pytest
import os
from unittest.mock import patch


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
