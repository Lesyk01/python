class JunkItem:
    def __init__(self, name, quantity, value):
        self.name = name
        self.quantity = quantity
        self.value = value

    def __str__(self):
        return f"{self.name} ({self.quantity} шт, {self.value} грн)"


class JunkStorage:
  
    def serialize(self, items, filename):
        with open(filename, "w", encoding="utf-8") as f:
            for item in items:
              
                line = f"{item.name}|{item.quantity}|{str(item.value).replace('.', ',')}\n"
                f.write(line)

  
    def parse(self, filename):
        items = []
        with open(filename, "r", encoding="utf-8") as f:
            for line_number, line in enumerate(f, start=1):
                line = line.strip()
                if not line:
                    continue

                parts = line.split("|")
                if len(parts) != 3:
                    print(f"Рядок {line_number} пропущено: неправильна кількість полів")
                    continue

                name, quantity_str, value_str = parts

                try:
                    quantity = int(quantity_str)
                    value = float(value_str.replace(",", "."))
                    items.append(JunkItem(name, quantity, value))
                except ValueError:
                    print(f" Рядок {line_number} пропущено: невірний формат чисел")

        return items



if __name__ == "__main__":
    storage = JunkStorage()

    junk_list = [
        JunkItem("Бляшанка", 5, 2.5),
        JunkItem("Стара плата", 3, 7.8),
        JunkItem("Купка дротів", 10, 1.2)
    ]


    storage.serialize(junk_list, "junk_storage.txt")
    print(" Дані записано у файл 'junk_storage.txt'")


    loaded = storage.parse("junk_storage.txt")
    print("\n Зчитані предмети:")
    for item in loaded:
        print("-", item)



# Серіалізація — це процес перетворення  списку об'єктів (items) у файл (filename).
#"r" "a" 
#Метод __str__ (string) у класі JunkItem служить для визначення "офіційного" рядкового представлення об'єкта.об'єкт на звичайний текст
#він використовується print(" -", item)

# що файл повинен використовувати кодування UTF-8 
# для правильного збереження та зчитування всіх символів, включаючи українську кирилицю.

# __repr__ (зазвичай) повертає: JunkItem("Бляшанка", 5, 2.5) (тобто код, який можна скопіювати і створити об'єкт знову).