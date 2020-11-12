from src.main import main
from src.constants import (expected_print)


def test_main(capsys):
    main("data/orders_1.csv")
    out, err = capsys.readouterr()
    assert out == expected_print
