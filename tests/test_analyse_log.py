from src.analyse_log import analyse_log
from src.constants import (path_not_exists_csv, path_exists_csv)
import pytest


def test_analyse_log_file_not_exist():
    with pytest.raises(ValueError,
                       match="Arquivo not_exist.csv não encontrado"):
        analyse_log(path_not_exists_csv)


def test_analyse_log_on_success():
    analyse_log(path_exists_csv)
    assert False
