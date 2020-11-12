path_exists_csv = "/home/anderson.bolivar/Documents/projects/sd-02-restaurant-orders/data/orders_1.csv"

path_not_exists_csv = "/home/anderson.bolivar/Documents/projects/sd-02-restaurant-orders/data/not_exist.csv"

path_txt = "/home/anderson.bolivar/Documents/projects/sd-02-restaurant-orders/data/mkt_campaign.txt"

expected_report = "- hamburguer" + "\n" + "- 0" + "\n" + \
    "- coxinha, misto-quente, pizza" + "\n" + "- sabado, segunda-feira"

expected_print = "hamburguer\n{'misto-quente': 8}\ncoxinha, misto-quente, pizza\nsabado, segunda-feira\n{'pao': 40, 'hamburguer': 32, 'queijo': 48, 'molho': 8, 'presunto': 8, 'massa': 16, 'frango': 8}\n"
