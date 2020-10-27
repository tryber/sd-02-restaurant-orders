# Crie uma suíte de testes para a classe TrackOrders
# Obtenha, no mínimo, 90% de cobertura

from src.track_orders import TrackOrders


mocked_resp = {
  'maria': {
    'Orders': ['hamburguer', 'pizza', 'coxinha', 'hamburguer'],
    'Days': ['terça-feira', 'terça-feira', 'segunda-feira', 'terça-feira']
  },
  'joao': {
    'Orders': ['hamburguer'],
    'Days': ['terça-feira']
  },
  'arnaldo': {
    'Orders': ['misto-quente'],
    'Days': ['terça-feira']
  }
}

mocked_all_days = {"segunda-feira", "terça-feira"}

mocked_all_foods = {"hamburguer", "coxinha", "misto-quente", "pizza"}


instance_test = TrackOrders()
instance_test.add_new_order("maria", "hamburguer", "terça-feira")
instance_test.add_new_order("joao", "hamburguer", "terça-feira")
instance_test.add_new_order("maria", "pizza", "terça-feira")
instance_test.add_new_order("maria", "coxinha", "segunda-feira")
instance_test.add_new_order("maria", "hamburguer", "terça-feira")
instance_test.add_new_order("arnaldo", "misto-quente", "terça-feira")


def test_add_new_order():
    assert instance_test.dict_orders == mocked_resp


def test_get_most_ordered_dish_per_costumer():
    assert instance_test.get_most_ordered_dish_per_costumer(
      'maria'
      ) == 'hamburguer'


def test_get_order_frequency_per_costumer():
    assert instance_test.get_order_frequency_per_costumer(
      'arnaldo', 'hamburguer'
      ) == 0


def test_get_never_ordered_per_costumer():
    assert instance_test.get_never_ordered_per_costumer(
      'joao'
      ) == {'pizza', 'misto-quente', 'coxinha'}


def test_get_days_never_visited_per_costumer():
    assert instance_test.get_days_never_visited_per_costumer(
      'joao'
      ) == {'segunda-feira'}


def test_get_busiest_day():
    assert instance_test.get_busiest_day() == ['terça-feira']


def test_get_least_busy_day():
    assert instance_test.get_least_busy_day() == ['segunda-feira']
