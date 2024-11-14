import os
import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Путь к Yandex Browser и драйверу
yandex_driver_path = r"yandexdriver.exe"
options = Options()
options.binary_location = r"C:\Users\Дмитрий\AppData\Local\Yandex\YandexBrowser\Application\browser.exe"

driver = webdriver.Chrome(service=Service(yandex_driver_path), options=options)

driver.get("https://the-internet.herokuapp.com/context_menu")

driver.maximize_window()

element = driver.find_element(By.ID, "hot-spot")
action = ActionChains(driver)
action.context_click(element).perform()

time.sleep(2)

# Сделать скриншот всего экрана
pyautogui.screenshot("screenshot_with_alert.png")

alert = driver.switch_to.alert
alert.accept()

driver.get("https://the-internet.herokuapp.com/upload")

my_file = r"empty_file.txt"
with open(my_file, "w") as file:
   pass

# Найти элемент для загрузки файла
file_input = driver.find_element(By.ID, "file-upload")

# Отправка пути к файлу
file_input.send_keys(os.path.abspath(my_file))

submit_button = driver.find_element(By.ID, "file-submit")
submit_button.click()

time.sleep(1)

# Сделать скриншот всего экрана
pyautogui.screenshot("screenshot_with_file.png")