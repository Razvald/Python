import time
from selenium import webdriver

# Запуск
driver = webdriver.Chrome()

# Открытие страницы
driver.get("https://www.example.com")

# Ожидание 5 секунд для просмотра страницы
time.sleep(10)

# Закрытие
driver.quit()
