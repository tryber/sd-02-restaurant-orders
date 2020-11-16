class InventoryControl:
    def __init__(self):
        self.ingredients = {
            'hamburguer': ['pao', 'hamburguer', 'queijo'],
            'pizza': ['massa', 'queijo', 'molho'],
            'misto-quente': ['pao', 'queijo', 'presunto'],
            'coxinha': ['massa', 'frango'],
        }

        self.minimum_inventory = {
            'pao': 50,
            'hamburguer': 35,
            'queijo': 100,
            'molho': 30,
            'presunto': 20,
            'massa': 20,
            'frango': 10,
        }

        self.current_inventory = {
            'pao': 50,
            'hamburguer': 35,
            'queijo': 100,
            'molho': 30,
            'presunto': 20,
            'massa': 20,
            'frango': 10,
        }

    def add_new_order(self, costumer, order, day):
        ingredients = self.ingredients[order]
        for ingredient in ingredients:
            self.current_inventory[
                ingredient] = self.current_inventory[ingredient] - 1

    def get_shopping_list(self):
        report = {}
        for ingredient in self.current_inventory:
            report[ingredient] = self.minimum_inventory[ingredient] - \
                self.current_inventory[ingredient]
        return report

    def get_available_dishes(self):
        orders = []
        for order, ingredients in self.ingredients.items():
            is_available = True
            for ingredient in ingredients:
                if self.current_inventory[ingredient] <= 0:
                    is_available = False
                    break
            if is_available:
                orders.append(order)
        return orders
