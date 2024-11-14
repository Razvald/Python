from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

yandex_driver_path = r"D:\Progs\yandexdriver.exe"
options = Options()
options.binary_location = r"C:\Users\Дмитрий\AppData\Local\Yandex\YandexBrowser\Application\browser.exe"
driver = webdriver.Chrome(service=Service(yandex_driver_path), options=options)

driver.get("https://www.python.org")

# Поиск изображения внутри тега h1
img = driver.find_element(By.XPATH, "//h1//img")
img_url = img.get_attribute('src')
print("Ссылка на изображение заголовка:", img_url)

# Поиск всех ссылок внутри раздела About
about_links = driver.find_elements(By.XPATH, "//li[@id='about']//a")
for link in about_links:
    print("Ссылка из раздела 'About':", link.get_attribute('href'))

# Поиск всех заголовков h2 через CSS селектор
h2_elements = driver.find_elements(By.CSS_SELECTOR, "h2")
for h2 in h2_elements:
    print("Текст заголовка h2:", h2.text)

# Поиск ссылок в Navigation Menu через CSS селектор
nav_links = driver.find_elements(By.CSS_SELECTOR, "#mainnav a")
for nav_link in nav_links:
    print("Ссылка из Navigation Menu:", nav_link.get_attribute('href'))

# Бесконечный цикл, чтобы браузер не закрывался
while True:
    pass

#Code writes by Панченко Дмитрий