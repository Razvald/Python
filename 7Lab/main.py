import sys
import io
import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Запуск драйвера
yandex_driver_path = r"yandexdriver.exe"
options = Options()
options.binary_location = r"C:\Users\Razvald\AppData\Local\Yandex\YandexBrowser\Application\browser.exe"

# Запуск браузера
driver = webdriver.Chrome(service=Service(yandex_driver_path), options=options)
driver.maximize_window()

driver.get("https://www.base64encode.org/")
driver.execute_script("window.open('https://ru.wikipedia.org');")
driver.execute_script("window.open('https://en.wikipedia.org');")

def open_random_articles(tab_index, screenshot_prefix):
    driver.switch_to.window(driver.window_handles[tab_index])
    for i in range(5):
        try:
            random_link = driver.find_element(By.XPATH, "//li[@id='n-randompage']/a")
            driver.execute_script(f"window.open('{random_link.get_attribute('href')}');")
        except Exception as e:
            print(f"Error on iteration {i}: {e}")

open_random_articles(1, 'scr_rnd_ru')

time.sleep(10)
pyautogui.screenshot(f"Output/scr_rnd_ru.png")

open_random_articles(2, 'scr_rnd_en')

time.sleep(10)
pyautogui.screenshot(f"Output/scr_rnd_en.png")

titles = []
for handle in driver.window_handles[3:]:
    driver.switch_to.window(handle)
    titles.append(driver.title)
    driver.close()

driver.switch_to.window(driver.window_handles[0])

textarea = driver.find_element(By.ID, "input")
textarea.clear()
textarea.send_keys("\n".join(titles))

encode_button = driver.find_element(By.ID, "submit_text")
encode_button.click()

output_area = driver.find_element(By.ID, "output")
encoded_text_from_site = output_area.get_attribute('value')

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print("Заголовки:")
print("\n".join(titles))

print("\nЗаголовки в base64:")
print(encoded_text_from_site)
#Code writes by Панченко Дмитрий