import csv


def check_extension(path, expected_extension):
    if expected_extension not in path:
        raise ValueError("Formato inválido")


def file_not_found(path):
    file = path.split("/").pop()
    return "Arquivo {} não encontrado".format(file)


def csv_importer(csv_path):
    try:
        with open(csv_path) as csv_file:
            check_extension(csv_path, ".csv")
            csv_reader = csv.DictReader(csv_file, delimiter=",")
            data = []
            for csv_row in csv_reader:
                row = list(csv_row.values())
                data_row = {"name": row[0], "order": row[1], "day": row[2]}
                data.append(data_row)
    except(FileNotFoundError):
        raise ValueError(file_not_found(csv_path))
    else:
        return data
