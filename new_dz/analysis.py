import numpy as np
import pandas as pd

file_name = 'supplies.csv'
try:
    df = pd.read_csv(file_name)
except FileNotFoundError:
    print(f"Помилка: файл {file_name} не знайдено.")
    exit()

df['total_price'] = df['quantity'] * df['price_per_unit']


mean_price = np.mean(df['price_per_unit'])       
median_qty = np.median(df['quantity'])           
std_price = np.std(df['price_per_unit'])        
supplier_stats = df.groupby('supplier')['total_price'].sum()
top_supplier = supplier_stats.idxmax()
top_profit = supplier_stats.max()


category_stats = df.groupby('category')['quantity'].sum()


low_supply = df[df['quantity'] < 100]
low_supply.to_csv('low_supply.csv', index=False)


top_3 = df.sort_values(by='total_price', ascending=False).head(3)

plot = category_stats.plot(kind='bar', title='Кількість по категоріях')
fig = plot.get_figure()
fig.savefig('chart.png')


report = f"""--- АНАЛІТИЧНИЙ ЗВІТ ---
1. Статистика (NumPy):
   - Середня ціна: {mean_price:.2f}
   - Медіана кількості: {median_qty:.0f}
   - Стандартне відхилення ціни: {std_price:.2f}

2. Лідери (Pandas):
   - Найкращий постачальник: {top_supplier} (Прибуток: {top_profit:.2f})

3. Експорт:
   - Дефіцитні товари збережено у 'low_supply.csv'
   - Графік збережено у 'chart.png'
"""

with open('report.txt', 'w', encoding='utf-8') as f:
    f.write(report)


print(report)
print("Топ-3 найдорожчі поставки:")
print(top_3[['supplier', 'category', 'total_price']])