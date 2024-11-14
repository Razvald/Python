from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

yandex_driver_path = r"D:\Progs\yandexdriver.exe"
options = Options()
options.binary_location = r"C:\Users\Дмитрий\AppData\Local\Yandex\YandexBrowser\Application\browser.exe"

driver = webdriver.Chrome(service=Service(yandex_driver_path), options=options)

driver.get("https://www.python.org")

dw_btn = driver.find_element(By.LINK_TEXT, 'Downloads')
dw_btn.click()

srh_inp = driver.find_element(By.ID, 'id-search-field')
srh_inp.send_keys('python 3.11')

srh_btn = driver.find_element(By.ID, "submit")
srh_btn.click()

# Бесконечный цикл, чтобы браузер не закрывался
while True:
    pass

#Code writes by Панченко Дмитрий