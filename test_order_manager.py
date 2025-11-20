import pytest

class OrderManager:
    def __init__(self, items):
        self.items = items

    def total(self):
        return sum(item['price'] for item in self.items)

    def most_expensive(self):
        if not self.items:
            return None
        return max(self.items, key=lambda x: x['price'])

    def apply_discount(self, percent):
        if not 0 <= percent <= 100:
            raise ValueError("Discount must be between 0 and 100")
        factor = 1 - (percent / 100)
        for item in self.items:
            item['price'] *= factor

    def __repr__(self):
        return f"OrderManager(items={len(self.items)})"

def test_total_calculation():
    items = [{'name': 'A', 'price': 100}, {'name': 'B', 'price': 50}]
    manager = OrderManager(items)
    assert manager.total() == 150

def test_total_empty():
    manager = OrderManager([])
    assert manager.total() == 0

def test_most_expensive():
    items = [{'name': 'A', 'price': 10}, {'name': 'B', 'price': 100}, {'name': 'C', 'price': 50}]
    manager = OrderManager(items)
    result = manager.most_expensive()
    assert result['name'] == 'B'
    assert result['price'] == 100

def test_most_expensive_empty():
    manager = OrderManager([])
    assert manager.most_expensive() is None

def test_apply_discount_valid():
    items = [{'name': 'A', 'price': 100}, {'name': 'B', 'price': 200}]
    manager = OrderManager(items)
    manager.apply_discount(10)
    assert manager.items[0]['price'] == 90.0
    assert manager.items[1]['price'] == 180.0
    assert manager.total() == 270.0

def test_apply_discount_zero():
    items = [{'name': 'A', 'price': 100}]
    manager = OrderManager(items)
    manager.apply_discount(0)
    assert manager.items[0]['price'] == 100

def test_apply_discount_full():
    items = [{'name': 'A', 'price': 100}]
    manager = OrderManager(items)
    manager.apply_discount(100)
    assert manager.items[0]['price'] == 0

def test_apply_discount_invalid_negative():
    manager = OrderManager([{'name': 'A', 'price': 100}])
    with pytest.raises(ValueError):
        manager.apply_discount(-10)

def test_apply_discount_invalid_huge():
    manager = OrderManager([{'name': 'A', 'price': 100}])
    with pytest.raises(ValueError):
        manager.apply_discount(150)

def test_repr():
    items = [{'name': 'A', 'price': 10}, {'name': 'B', 'price': 20}]
    manager = OrderManager(items)
    assert repr(manager) == "OrderManager(items=2)"