import pytest
from service_body_test import Order  


@pytest.fixture
def sample_items():
    return [
        {'name': 'Laptop', 'price': 1000, 'quantity': 1},
        {'name': 'Mouse', 'price': 50, 'quantity': 2},
        {'name': 'Keyboard', 'price': 100, 'quantity': 1}
    ]

@pytest.fixture
def order(sample_items):
    return Order(id=1, items=sample_items)



def test_init(order, sample_items):
    assert order.id == 1
    assert order.items == sample_items

def test_total_calculation(order):
    assert order.total() == 1200

def test_total_empty():
    empty_order = Order(id=2, items=[])
    assert empty_order.total() == 0

def test_most_expensive(order):
    expensive = order.most_expensive()
    assert expensive['name'] == 'Laptop'
    assert expensive['price'] == 1000

def test_apply_discount_valid(order):
    order.apply_discount(10)

    assert order.items[0]['price'] == 900.0
    assert order.items[1]['price'] == 45.0
    assert order.items[2]['price'] == 90.0
    

    assert order.total() == 1080

def test_apply_discount_zero(order):
    order.apply_discount(0)
    assert order.items[0]['price'] == 1000

def test_apply_discount_full(order):
    order.apply_discount(100)
    assert order.items[0]['price'] == 0
    assert order.total() == 0

def test_apply_discount_invalid_negative(order):
    with pytest.raises(ValueError, match="Invalid discount"):
        order.apply_discount(-1)

def test_apply_discount_invalid_huge(order):
    with pytest.raises(ValueError, match="Invalid discount"):
        order.apply_discount(101)

def test_repr(order):
    assert repr(order) == "<Order 1: 3 items>"

def test_most_expensive_fail_on_empty():
    empty_order = Order(id=99, items=[])
    with pytest.raises(ValueError): 
        empty_order.most_expensive()
