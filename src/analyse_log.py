from src.services import (
    csv_importer, get_frequency_report_by,
    get_fields_by, get_fields_related, export_txt)


def get_maria_favorite_order(data):
    orders_frequency_in_maria = get_frequency_report_by(
        "name", "maria", "order", data)
    return f"- {orders_frequency_in_maria[0][0]}"


def how_many_times_arnaldo_ordered_hamburguer(data):
    orders_frequency_in_arnaldo = get_frequency_report_by(
        "name", "arnaldo", "order", data)
    try:
        times = dict(orders_frequency_in_arnaldo)["hamburguer"]
    except(KeyError):
        times = 0
    return f"- {times}"


def get_no_joao_orders(data):
    orders = get_fields_by("order", data)
    joao_orders = get_fields_related("name", "joao", "order", data)

    difference = ", ".join(sorted(orders - joao_orders))
    return f"- {difference}"


def get_no_joao_days(data):
    days = get_fields_by("day", data)
    joao_days = get_fields_related("name", "joao", "day", data)
    difference = ", ".join(sorted(days - joao_days))
    return f"- {difference}"


def analyse_log(path_to_file):
    data = csv_importer(path_to_file)
    q1 = get_maria_favorite_order(data)
    print("q1", q1)
    q2 = how_many_times_arnaldo_ordered_hamburguer(data)
    print("q2", q2)
    q3 = get_no_joao_orders(data)
    print("q3", q3)
    q4 = get_no_joao_days(data)
    print("q4", q4)
    questions = q1 + "\n" + q2 + "\n" + q3 + "\n" + q4
    export_txt(questions)
