from src.analyse_log import analyse_log, maria_orders, arnaldo_orders
from src.analyse_log import joao_orders, joao_not_in_days, write_document
from src.analyse_log import open_orders
from unittest.mock import patch, mock_open
from io import StringIO

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

writed_document = """hamburguer
0
{'coxinha', 'misto-quente', 'pizza'}
{'sabado', 'segunda-feira'}
"""

write_to_document = [
    'hamburguer',
    0,
    {'coxinha', 'misto-quente', 'pizza'},
    {'segunda-feira', 'sabado'},
]

return_open = [
    {'client': 'maria', 'meal': 'pizza', 'day': 'terça-feira'},
    {'client': 'maria', 'meal': 'hamburguer', 'day': 'terça-feira'},
    {'client': 'joao', 'meal': 'hamburguer', 'day': 'terça-feira'},
    {'client': 'maria', 'meal': 'coxinha', 'day': 'segunda-feira'},
    {'client': 'arnaldo', 'meal': 'misto-quente', 'day': 'terça-feira'},
    {'client': 'jose', 'meal': 'hamburguer', 'day': 'sabado'},
    {'client': 'maria', 'meal': 'hamburguer', 'day': 'terça-feira'},
    {'client': 'maria', 'meal': 'hamburguer', 'day': 'terça-feira'},
    {'client': 'joao', 'meal': 'hamburguer', 'day': 'terça-feira'},
]


class TestAnalysLog:
    def test_analyse_log(self):
        mock_opened = mock_open(read_data=file_content_mock)
        with patch("os.path.exists", return_value=True), patch(
                "builtins.open", mock_opened) as file_mocked:
            analyse_log("teste.csv")
            file_mocked.return_value.write.assert_any_call("hamburguer\n")
            file_mocked.return_value.write.assert_any_call("0\n")
            # assertIn(row1, file_mocked.return_value.write())

    def test_analyse_log_fail_exist_false(self, capsys):
        with patch("os.path.exists", return_value=False):
            analyse_log("nao_existe.csv")
            capture = capsys.readouterr()
            assert capture.err == "Arquivo nao_existe.csv não existe\n"

    def test_analyse_log_fail_endswith(self, capsys):
        with patch("os.path.exists", return_value=True):
            analyse_log("teste")
            capture = capsys.readouterr()
            assert capture.err == "Formato Inválido\n"

    def test_maria_orders(self):
        mock_opened = mock_open(read_data=file_content_mock)
        with patch("os.path.exists", return_value=True), patch(
                "builtins.open", mock_opened):
            result = maria_orders("teste.csv")
            assert result == "hamburguer"

    def test_arnaldo_orders(self):
        mock_opened = mock_open(read_data=file_content_mock)
        with patch("os.path.exists", return_value=True), patch(
                "builtins.open", mock_opened):
            result = arnaldo_orders("teste.csv")
            assert result == 0

    def test_joao_orders(self):
        mock_opened = mock_open(read_data=file_content_mock)
        with patch("os.path.exists", return_value=True), patch(
                "builtins.open", mock_opened):
            result = joao_orders("teste.csv")
            assert result == {'coxinha', 'misto-quente', 'pizza'}

    def test_joao_not_in_days(self):
        mock_opened = mock_open(read_data=file_content_mock)
        with patch("os.path.exists", return_value=True), patch(
                "builtins.open", mock_opened):
            result = joao_not_in_days("teste.csv")
            assert result == {'sabado', 'segunda-feira'}

    def test_write_document(self):
        mock_opened = mock_open(read_data=writed_document)
        with patch("builtins.open", mock_opened) as mock:
            write_document(write_to_document)
            mock.return_value.write.assert_any_call("hamburguer\n")
            mock.return_value.write.assert_any_call("0\n")
            mock.return_value.write.assert_any_call(
                f"{write_to_document[2]}\n"
            )
            mock.return_value.write.assert_any_call(
                f"{write_to_document[3]}\n"
            )

    def test_open_orders(self):
        mock_opened = mock_open(read_data=file_content_mock)
        with patch("builtins.open", mock_opened):
            result = open_orders("teste.csv")
            assert result == return_open
# Crie uma suíte de testes para o método analyse_log
# Obtenha, no mínimo, 90% de cobertura
