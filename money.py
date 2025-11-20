def shadow(limit):
    def decorator(generator_func):
        def wrapper(*args, **kwargs):
            print(f"--- Тіньовий Аудит: Ліміт встановлено на {limit} ---")
            total_sum = 0
            limit_triggered = False 
            gen = generator_func(*args, **kwargs)
            for transaction in gen:
                try:
                    parts = transaction.lower().split()
                    if len(parts) != 2:
                        print(f"   [Помилка даних] -> Невірний формат: '{transaction}'")
                        continue

                    transaction_type, amount_str = parts

                    if transaction_type not in ("payment", "refund", "transfer"):
                        print(f"   [Помилка даних] -> Невідомий тип: '{transaction}'")
                        continue


                    amount = int(amount_str)
                    if transaction_type == "refund":
                        total_sum -= amount
                    else: 
                        total_sum += amount
            
                    print(f"   [Аудит] Транзакція: {transaction} | Поточна тіньова сума: {total_sum}")

                    if total_sum >= limit and not limit_triggered:
                        print(f"   >>> ТІНЬОВИЙ ЛІМІТ ({limit}) ПЕРЕВИЩЕНО! Активую схему. <<<")
                        limit_triggered = True 
                    yield transaction

                except ValueError:
                    print(f"   [Помилка конвертації] -> Сума не є числом: '{transaction}'")
                    continue 
                except Exception as e:
                    print(f"   [Невідома помилка] -> '{transaction}' | {e}")
                    continue
            print(f"--- Тіньовий Аудит Завершено ---")
            return total_sum
        
        return wrapper
    return decorator

@shadow(limit=200)
def transaction_generator(data_list):
    """
    Простий генератор, що віддає транзакції зі списку.
    """
    for item in data_list:
        yield item


transactions = [
    "payment 120",      
    "refund 50",        
    "transfer 150",     
    "payment 500",      
    "bad_data 10",      
    "payment 100",      
 
]


shadow_stream = transaction_generator(transactions)

print("\n=== АКТИВАЦІЯ ЗВИЧАЙНОГО ПОТОКУ (не знає про аудит) ===")
final_sum = 0

try:
    for transaction_data in shadow_stream:
        print(f"   [ВИДИМИЙ ПОТІК] Отримано: {transaction_data}")
except StopIteration as e:
    final_sum = e.value
    print(f"\n--- ФІНАЛЬНА ТІНЬОВА СУМА (Спіймано з return): {final_sum} ---")

print(f"Роботу завершено. Фінальна сума: {final_sum}")



#Декоратори
# Декоратор — це функція, яка обгортає іншу функцію, щоб додати їй нову поведінку, не змінюючи її код.
# Декоратор приймає функцію як аргумент, створює нову функцію-обгортку і повертає її замість старої. 
# Тому, коли викликаєш оригінальну функцію, насправді виконується нова з додатковими діями. 
# Що це робить: Символ @ (декоратор) говорить Python: «Не використовуй функцію transaction_generator саму по собі. 
# Спершу передай її у функцію,яку поверне виклик shadow(limit=200), 
# і використовуй результат (обгортку wrapper) замість оригінальної функції».



# *args -- Позиційні аргументи (без імені) -- Кортеж (tuple) -- func(1, 2, 3) -- Для елементів списку, сум
# **kwargs (Дві зірочки) -- Іменовані аргументи (ключ=значення) -- Словник (dict) -- func(a=1, b=2) -- Для налаштувань, конфігурацій, опцій



# Генератори
# Генератор — це функція, яка не повертає всі результати одразу, а видає їх поступово, по одному, коли їх запитують.
# Він запам'ятовує, де зупинився, і продовжує роботу з того місця.
# Генератор wrapper перехоплює кожну транзакцію, що виходить з оригінального генератора (gen = generator_func(*args, **kwargs)). 
# Він не просто пропускає її далі; він робить із нею три речі:
# Валідація: Перевіряє, чи має транзакція правильний формат (два слова, відомий тип).
# Облік: Оновлює тіньову суму (total_sum) на основі цієї транзакції.
# Моніторинг: Перевіряє, чи не перевищено встановлений ліміт (limit).


# Чим yield відрізняється від return?
# return — завершує функцію назавжди.
# yield — призупиняє виконання і запам'ятовує стан. Наступний виклик продовжує з того самого місця.




