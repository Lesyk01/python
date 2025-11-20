from abc import ABC, abstractmethod

class Transport(ABC):
    def __init__(self, name: str, speed: int, capacity: int):
        self.name = name
        self.speed = speed
        self.capacity = capacity
    
    @abstractmethod
    def move(self, distance: int) -> float:
        pass
    @abstractmethod
    def fuel_consumption(self, distance: int) -> float:
        pass
    @abstractmethod
    def info(self) -> str:
        pass

    def calculate_cost(self, distance: int, price_per_unit: float) -> float:
        total_units = self.fuel_consumption(distance)
        return total_units * price_per_unit

class Car(Transport):
    def __init__(self, name: str, speed: int, capacity: int):
        super().__init__(name, speed, capacity)
        self.fuel_rate = 0.07 

    def move(self, distance: int) -> float:
        return distance / self.speed

    def fuel_consumption(self, distance: int) -> float:
        return distance * self.fuel_rate

    def info(self) -> str:
        return f"{self.name} - Легковий автомобіль. Шв: {self.speed} км/год, Місця: {self.capacity}."

class Bus(Transport):
    def __init__(self, name: str, speed: int, capacity: int, passengers: int):
        super().__init__(name, speed, capacity)
        self.passengers = passengers
        self.fuel_rate = 0.15 

    def move(self, distance: int) -> float:
        return distance / self.speed

    def fuel_consumption(self, distance: int) -> float:
        if self.passengers > self.capacity:
            print(f"⚠️ {self.name}: Перевантажено! (Пасажирів: {self.passengers}, Місць: {self.capacity})")
            return 0.0
        
        return distance * self.fuel_rate

    def info(self) -> str:
        status = "Перевантажений" if self.passengers > self.capacity else "Норма"
        return f"{self.name} - Автобус. Шв: {self.speed} км/год, Пасажири: {self.passengers}/{self.capacity} ({status})."

class Bicycle(Transport):
    MAX_SPEED = 20
    
    def move(self, distance: int) -> float:
        actual_speed = min(self.speed, self.MAX_SPEED)
        return distance / actual_speed

    def fuel_consumption(self, distance: int) -> float:
        return 0.0

    def info(self) -> str:
        speed_limit = min(self.speed, self.MAX_SPEED)
        return f"{self.name} - Велосипед. Макс. шв: {speed_limit} км/год. Пального не потребує."

class ElectricCar(Car):
    def __init__(self, name: str, speed: int, capacity: int):
        super().__init__(name, speed, capacity)
        self.battery_rate = 0.2 

    def fuel_consumption(self, distance: int) -> float:
        return 0.0

    def battery_usage(self, distance: int) -> float:
        return distance * self.battery_rate
    
    def info(self) -> str:
        return f"{self.name} - Електромобіль. Шв: {self.speed} км/год. Витрати: {self.battery_rate} кВт⋅год/км."

    def calculate_cost(self, distance: int, price_per_unit: float) -> float:
        total_units = self.battery_usage(distance)
        return total_units * price_per_unit
    
    
    
    
    
    # self — це перший, обов'язковий аргумент кожного методу екземпляра (інстанса) класу в Python.
    # Він служить як посилання на конкретний об'єкт, з яким наразі працює метод.
    
#     Метод __init__ (читається як "ініт") виконує функцію конструктора. Його головна мета:
# Прийняти вхідні дані: Отримати значення, які ви хочете присвоїти новому об'єкту (наприклад, ім'я,
# швидкість, місткість у вашому випадку з транспортом).
# Ініціалізувати стан: Взяти ці дані та зберегти їх як атрибути (властивості) всередині цього конкретного об'єкта.

# абстрактний метод це означає що будьь який клас який його унаслідує має реалізувати певні методи 
# ->> Car, Bus, Bicycle, ElectricCar) повинен реалізувати : move, info, витрату пального
# Наслідування: Car, Bus, Bicycle та ElectricCar успадковують властивості та методи від Transport.
# поліморфізм: У циклі for t in fleet: ми викликаємо одні й ті самі методи (t.move(), t.fuel_consumption(), t.info()),
# але отримуємо різну поведінку залежно від фактичного типу об'єкта