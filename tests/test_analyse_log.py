from src.analyse_log import (
    most_frequent_order,
    times_specific_order,
    not_asked_order,
    days_not_gone,
    check_file,
    analyse_log,
)
from unittest.mock import patch, mock_open


order_by_name = {
    "pedro": {
        "days": {"segunda-feira", "sabado"},
        "Food most Frequent": "Azeitona",
        "Azeitona": 3,
        "Pera": 2,
        "Most Frequent Value": 3,
    }
}

all_days = {"segunda-feira", "sabado", "domingo"}

mocked_data = """pedro,couve,domingo
pedro,couve,segunda-feira
pedro,abacate,domingo
maria,coxinha,segunda-feira
maria,coxinha,segunda-feira
arnaldo,coxinha,segunda-feira
arnaldo,coxinha,segunda-feira
arnaldo,hamburguer,segunda-feira
joao,couve,segunda-feira
joao,abacate,segunda-feira
joao,abacate,segunda-feira
"""

adjusted_data = {
    "pedro": {
        "days": {"domingo", "segunda-feira"},
        "Most Frequent Value": 2,
        "Food most Frequent": "couve",
        "couve": 2,
        "abacate": 1,
    },
    "maria": {
        "days": {"segunda-feira"},
        "Most Frequent Value": 2,
        "Food most Frequent": "coxinha",
        "coxinha": 2,
    },
    "arnaldo": {
        "days": {"segunda-feira"},
        "Most Frequent Value": 2,
        "Food most Frequent": "coxinha",
        "coxinha": 2,
        "hamburguer": 1,
    },
    "joao": {
        "days": {"segunda-feira"},
        "Most Frequent Value": 2,
        "Food most Frequent": "abacate",
        "couve": 1,
        "abacate": 2,
    },
}


def test_most_frequent_order_returns_correct():
    assert most_frequent_order(order_by_name, "pedro") == "Azeitona"


def test_times_specific_order_returns_correct():
    assert times_specific_order(order_by_name, "pedro", "Azeitona") == 3
    assert times_specific_order(order_by_name, "pedro", "Coxinha") == 0


def test_not_asked_order_returns_correct():
    assert not_asked_order(
        order_by_name, "pedro", {"Coxinha", "Azeitona", "Pera"}
    ) == {"Coxinha"}


def test_days_not_gone_returns_correct():
    assert days_not_gone(order_by_name, "pedro", all_days) == {"domingo"}


def test_check_file_returns_correct():
    with patch("builtins.open", mock_open(read_data=mocked_data)):
        assert check_file("Qualquer_coisa.csv") == (
            adjusted_data,
            {"abacate", "couve", "coxinha", "hamburguer"},
            {"domingo", "segunda-feira"},
        )


def test_analyse_log_line1():
    with patch(
        "src.analyse_log.check_file",
        return_value=(
            adjusted_data,
            {
                "abacate",
                "couve",
                "coxinha",
            },
            {"domingo", "segunda-feira"},
        ),
    ), patch("builtins.open", mock_open()) as mock_write:
        analyse_log("arquivo1.csv", "arquivo2.txt")
        mock_write.return_value.write.assert_any_call("coxinha\n")


def test_analyse_log_line2():
    with patch(
        "src.analyse_log.check_file",
        return_value=(
            adjusted_data,
            {"abacate", "couve", "coxinha"},
            {"domingo", "segunda-feira"},
        ),
    ), patch("builtins.open", mock_open()) as mock_write:
        analyse_log("arquivo1.csv", "arquivo2.txt")
        mock_write.return_value.write.assert_any_call("1\n")


# def test_analyse_log_line3():
#     with patch("src.analyse_log.check_file", return_value=(adjusted_data,
# {"abacate", "couve", "coxinha"})) as return_file, patch("builtins.open",
# mock_open()) as mock_write:
#         analyse_log('arquivo1.csv', 'arquivo2.txt')
#         mock_write.return_value.write.assert_any_call("{'coxinha',
# 'hamburguer'}\n")
#
#
# def test_analyse_log_line4():
#     with patch("src.analyse_log.check_file", return_value=(adjusted_data,
# {"abacate", "couve", "coxinha"})) as return_file,
# patch("builtins.open", mock_open()) as mock_write:
#         analyse_log('arquivo1.csv', 'arquivo2.txt')
#         mock_write.return_value.write.assert_any_call("{'domingo'}\n")
