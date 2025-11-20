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



# Абстракція (Abstraction) 👻
"Що це?"# Процес приховування складної реалізації та відображення лише необхідної функціональності.
# В Python це досягається через абстрактні класи (ABC) та абстрактні методи (@abstractmethod), які формують контракт.
# У коді: Клас Medicine є абстрактним.
"Де це"# Методи вимагає_рецепту, вимоги_зберігання,
#  info оголошені як абстрактні. Це означає, що будь-який клас, що успадковує від Medicine, обов'язково повинен реалізувати ці методи.

# Інкапсуляція (Encapsulation) 🔒
"Що це?"# З'єднання даних (атрибутів) і методів, що оперують цими даними, в єдиний об'єкт (клас),
# а також обмеження прямого доступу до внутрішніх деталей.
# У коді: Всі дані (name, quantity, price) та логіка (наприклад, total_price)
# для кожного препарату згруповані всередині відповідного класу.
"Де це"# Хоча в Python поля за замовчуванням публічні, принцип інкапсуляції застосовується,
# оскільки ми взаємодіємо з об'єктом, викликаючи методи (med.info(), med.total_price()), а не отримуючи доступ до даних безпосередньо.

# Поліморфізм (Polymorphism) 🎭
"Що це?"# Здатність різних об'єктів реагувати на один і той же виклик методу (одне ім'я) по-різному (багато форм).
# У коді: Виклик med.info() у функції midicines.
"Де це"# Для об'єкта Antibiotic викликається його версія info(), а для об'єкта Vaccine — його версія,
# яка включає націнку. Хоча функція викликає одну й ту саму назву методу (info), результат (поведінка) 
# залежить від конкретного типу об'єкта.

# Успадкування (Inheritance) 🧬
"Що це?" #Механізм, що дозволяє новому класу (нащадку) брати атрибути та методи з уже існуючого класу (батьківського).
# Це сприяє повторному використанню коду.
# У коді: Класи Antibiotic, Vitamin, та Vaccine успадковують від Medicine.
"Де це"# Усі нащадки автоматично отримують атрибути з __init__ (name, quantity, price) та метод total_price() 
# без необхідності їх повторного написання.

#self це аргумент без якого би метод не знав з якими даними йому працювати


