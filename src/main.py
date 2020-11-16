import csv
from pubsub import pub
from src.inventory_control import InventoryControl
from src.track_orders import TrackOrders
import sys


def print_info(tracker, control):
    print(tracker.get_most_ordered_dish_per_costumer('maria'))
    print(tracker.get_order_frequency_per_costumer('arnaldo', 'hamburguer'))
    print(tracker.get_never_ordered_per_costumer('joao'))
    print(tracker.get_days_never_visited_per_costumer('joao'))
    print(control.get_shopping_list())
    print(control.get_available_dishes())


def main(path):
    topic = 'order'

    tracker = TrackOrders()
    control = InventoryControl()
    subs = [tracker.add_new_order, control.add_new_order]

    for sub in subs:
        pub.subscribe(sub, topic)

    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for costumer, order, day in csv_reader:
            available_orders = control.get_available_dishes()
            if order in available_orders:
                pub.sendMessage(topic, costumer=costumer, order=order, day=day)

    print_info(tracker, control)


if __name__ == "__main__":
    path = sys.argv[1]
    main(path)
