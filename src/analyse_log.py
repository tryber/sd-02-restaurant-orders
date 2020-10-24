import csv


def analyse_log(path_to_file):
    with open(path_to_file) as file:
        data = csv.reader(file, delimiter=",", quotechar='"')

        orders = []
        for row in data:
            orders.append({
                "cliente": row[0],
                "prato": row[1],
                "dia": row[2],
            })

    pratos_maria = [
        order["prato"]
        for order in orders
        if order["cliente"] == "maria"
    ]

    quantidade_por_prato_maria = {}
    for prato in pratos_maria:
        if prato not in quantidade_por_prato_maria:
            quantidade_por_prato_maria[prato] = 1
        else:
            quantidade_por_prato_maria[prato] += 1

    maior_quantidade = 0
    mais_pedido_por_maria = ""
    for key, value in quantidade_por_prato_maria.items():
        if value > maior_quantidade:
            maior_quantidade = value
            mais_pedido_por_maria = key

    quantidade_hamburguer_arnaldo = len([
        order
        for order in orders
        if order["cliente"] == "arnaldo" and order["prato"] == "hamburguer"
    ])

    conjunto_pratos_joao = set([
        order["prato"]
        for order in orders
    ])
    for order in orders:
        if order["cliente"] == "joao":
            conjunto_pratos_joao.discard(order["prato"])

    conjunto_dias_joao = set([
        order["dia"]
        for order in orders
    ])
    for order in orders:
        if order["cliente"] == "joao":
            conjunto_dias_joao.discard(order["dia"])

    with open("data/mkt_campaign.txt", mode="w") as new_file:
        new_file.write(f"{mais_pedido_por_maria}\n")
        new_file.write(f"{quantidade_hamburguer_arnaldo}\n")
        new_file.write(f"{conjunto_pratos_joao}\n")
        new_file.write(f"{conjunto_dias_joao}\n")


analyse_log("data/orders_1.csv")
