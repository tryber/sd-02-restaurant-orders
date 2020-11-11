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


def merge(left, right, merged):
    left_cursor, right_cursor = 0, 0
    while left_cursor < len(left) and right_cursor < len(right):
        if left[left_cursor][1] <= right[right_cursor][1]:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1
        else:
            merged[left_cursor + right_cursor] = left[left_cursor]
            left_cursor += 1
    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]
    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]

    return merged


def sort_frequency_report(report_list):
    report_length = len(report_list)
    if report_length <= 1:
        return report_list
    middle = report_length // 2
    left, right = sort_frequency_report(
        report_list[:middle]), sort_frequency_report(report_list[middle:])
    return merge(left, right, report_list.copy())


def get_frequency_report_by(field_key, field_value, compare_key, data):
    frequency_report = {}
    for row in data:
        if field_value == row[field_key]:
            compare_value = row[compare_key]
            if compare_value in frequency_report:
                frequency_report[compare_value] += 1
            else:
                frequency_report[compare_value] = 1
    frequency_report_list = list(frequency_report.items())
    return sort_frequency_report(frequency_report_list)


def get_fields_by(field, data):
    fields = set()
    for row in data:
        fields.add(row[field])
    return fields


def get_fields_related(field_key, field_value, compare_key, data):
    fields = set()
    for row in data:
        if field_value == row[field_key]:
            fields.add(row[compare_key])
    return fields


def export_txt(string):
    with open("data/mkt_campaign.txt", "w") as file:
        file.write(string)
