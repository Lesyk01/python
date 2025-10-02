from abc import ABC, abstractmethod

class Medicine(ABC):
    def __init__(self, name: str, quantity: int, price: float) -> None:
        if not isinstance(name, str):
            return 'Incorrect data'
        if not isinstance(quantity, int):
            return 'Incorrect data'
        if not isinstance(price, float):
            return 'Incorrect data'

        self.name = name
        self.quantity = quantity
        self.price = price

    @abstractmethod
    def requires_prescription(self) -> bool:
        pass
    @abstractmethod
    def storage_requirments(self) -> str:
        pass
    def total_price(self) -> float:
        return self.quantity * self.price
    @abstractmethod
    def info(self) -> str:
        pass

class Antibiotic(Medicine):
    def requires_prescription(self) -> bool:
        return True
    def storage_requirments(self) -> str:
        return '8-15 C, Dark place'
    def info(self) -> str:
        return f'Antibiotic: {self.name}, Quantity: {self.quantity}, price: {self.price}, price per order: {self.total_price():.2f}, recipe: {self.requires_prescription()}, storage conditions: {self.storage_requirments()}'
    
class Vitamin(Medicine):
    def requires_prescription(self) -> bool:
        return False
    def storage_requirments(self) -> str:
        return '15-25 C, dry place'
    def info(self) -> str:
        return f'Vitamin: {self.name}, Quantity: {self.quantity}, price: {self.price}, price per order: {self.total_price():.2f}, recipe: {self.requires_prescription()}, storage conditions: {self.storage_requirments()}'

class Vaccine(Medicine):
    def requires_prescription(self) -> bool:
        return True
    def storage_requirments(self) -> str:
        return '2-8 C, Refrigerator'
    def info(self) -> str:
        return f'Vaccine: {self.name}, Quantity: {self.quantity}, price: {self.price}, price per order: {self.total_price() * 1.1:.2f}, recipe: {self.requires_prescription()}, storage conditions: {self.storage_requirments()}'

