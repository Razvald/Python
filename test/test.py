from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Путь к Yandex Browser и драйверу
yandex_driver_path = r"yandexdriver.exe"
options = Options()
options.binary_location = r"C:\Users\Razvald\AppData\Local\Yandex\YandexBrowser\Application\browser.exe"

# Запуск браузера
driver = webdriver.Chrome(service=Service(yandex_driver_path), options=options)

# Открытие сайта
driver.get("https://www.base64encode.org/")

# Даем время для полной загрузки
time.sleep(10)

# Проверка заголовка страницы
print(driver.title)

# Закрытие браузера
driver.quit()
