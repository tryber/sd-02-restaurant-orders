import csv
from collections import Counter


def analyse_log(path_to_file):
    def format_dict(dict_values):
        new_obj= {}
        keys = { 'days':set(), 'ingredients': set(), 'names': set() }
        for item in dict_values:
            try:
                new_obj[item['name']].extend([item['day'], item['ingredient']])
            except KeyError:
                new_obj[item['name']] = []
                new_obj[item['name']].extend([item['day'], item['ingredient']])
            keys['days'].add(item['day'])
            keys['ingredients'].add(item['ingredient'])
            keys['names'].add(item['name'])

        for name in keys['names']:
            new_obj[name]= Counter(new_obj[name])
        return new_obj, keys

    def mais_pedido(iterator, keys):
        final_value = { 'valor' : '', 'contagem' : 0 }
        for item in keys:
            if(iterator[item] > final_value['contagem']):
                final_value = { 'valor': item, 'contagem': iterator[item]}
        return final_value['valor']


    def comida_por_pessoa(iterator, key):
        return str(iterator[key])


    def dias_pratos(iterator, keys):
        final_value = set()
        for item in list(keys):
            if(iterator[item] == 0):
                final_value.add(item)
        return str(final_value)

    with open(path_to_file) as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',', fieldnames=['name', 'ingredient', 'day'])
        object_info, valid_keys = format_dict(csv_reader)
    with open('data/mkt_campaign.txt', 'w') as txt_file:
        txt_file.write(f"{mais_pedido(object_info['maria'], valid_keys['ingredients'])}\n")
        txt_file.write(f"{comida_por_pessoa(object_info['arnaldo'], 'hamburguer')}\n")
        txt_file.write(f"{dias_pratos(object_info['joao'], valid_keys['ingredients'])}\n")
        txt_file.write(f"{dias_pratos(object_info['joao'], valid_keys['days'])}\n")
        