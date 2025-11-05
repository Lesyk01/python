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



