from src.analyse_log import analyse_log


def test_analyse_log():
    analyse_log('./test.txt')

    with open('./test.txt', "r") as file:
        assert 'hamburguer\n' == file.readline()
        assert '0\n' == file.readline()
        assert {'pizza', 'coxinha', 'misto-quente'} == eval(file.readline())
        assert {'sabado', 'segunda-feira'} == eval(file.readline())
