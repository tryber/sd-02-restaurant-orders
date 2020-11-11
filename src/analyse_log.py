from src.services import (csv_importer)


def analyse_log(path_to_file):
    data = csv_importer(path_to_file)
    print("data", data)
