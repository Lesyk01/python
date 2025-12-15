import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

class SimpleScraper:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.driver.quit()
        print("Браузер закрито.")

    def run(self):
        results = []
        try:
            self.driver.get(self.url)
            self.driver.implicitly_wait(10)
            items = self.driver.find_elements(By.TAG_NAME, "h3")
            
            for item in items:
                text = item.text
                if text:  
                    results.append([text])
            
            print(f"Знайдено {len(results)} елементів.")
            return results

        except Exception as e:
            print(f"Сталася помилка: {e}")
            return []

    def save_to_file(self, data):
        with open('twitch_data.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Stream Title / Category']) 
            writer.writerows(data)
        print("Дані збережено у twitch_data.csv")

if __name__ == "__main__":
    link = "https://www.twitch.tv/"
    
    with SimpleScraper(link) as bot:
        data = bot.run()
        bot.save_to_file(data)