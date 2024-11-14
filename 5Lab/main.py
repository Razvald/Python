from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Путь к Yandex Browser и драйверу
yandex_driver_path = r"yandexdriver.exe"
options = Options()
options.binary_location = r"C:\Users\Razvald\AppData\Local\Yandex\YandexBrowser\Application\browser.exe"
driver = webdriver.Chrome(service=Service(yandex_driver_path), options=options)

driver.get("https://ci.nsu.ru/news")

driver.find_element(By.CSS_SELECTOR, "#arrFilter_DATE_ACTIVE_FROM_1").send_keys("01.10.2020")

driver.find_element(By.CSS_SELECTOR, "#arrFilter_DATE_ACTIVE_FROM_2").send_keys("01.10.2024")

driver.find_element((By.CSS_SELECTOR, ".btn.btn-success.filter-btn"))

while True:
	try:
		load_more_button = driver.find_element(By.CSS_SELECTOR, ".moreNewsList.loadMoreButton")
		load_more_button.click()
	except:
		break

news_items = driver.find_elements(By.CSS_SELECTOR, ".news-list-grid-item")

with open("result.txt", "w", encoding="utf-8") as file:
	for item in news_items:
		date = item.find_element(By.CSS_SELECTOR, ".date").text

		title_element = item.find_element(By.CSS_SELECTOR, "a.name")
		title = title_element.text
		link = title_element.get_attribute("href")
		
		image_element = item.find_element(By.CSS_SELECTOR, "a.img-wrap img")
		image_url = image_element.get_attribute("src")
		
		file.write(f"Дата: {date}\n")
		file.write(f"Заголовок: {title}\n")
		file.write(f"Ссылка на новость: https://ci.nsu.ru{link}\n")
		file.write(f"Изображение: https://ci.nsu.ru{image_url}\n")
		file.write("\n")

driver.quit()

#Code writes by Панченко Дмитрий