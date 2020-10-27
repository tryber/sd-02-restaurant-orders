from src.analyse_log import analyse_log


def test_analyse_log():
    row = set(['pizza', 'misto-quente', 'coxinha'])
    row_2 = set(['segunda-feira', 'sábado'])

    analyse_log("./data/orders_1.csv")

    file = open("./data/mkt_campaign.txt", "r")

    assert 'hamburguer\n' == file.readline()
    assert '0\n' == file.readline()
    assert f"{row}\n" in file.readline()
    assert f"{row_2}\n" in file.readline()


# Crie uma suíte de testes para o método analyse_log
# Obtenha, no mínimo, 90% de cobertura
