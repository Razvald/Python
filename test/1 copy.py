from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Настройки драйвера
yandex_driver_path = r"D:\Progs\yandexdriver.exe"
options = Options()
options.binary_location = r"C:\Users\Дмитрий\AppData\Local\Yandex\YandexBrowser\Application\browser.exe"
driver = webdriver.Chrome(service=Service(yandex_driver_path), options=options)

# Функция для извлечения данных видео
def extract_video_data(driver, file, video_url):
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@data-testid='video_modal_title']"))
        )
        title = driver.find_element(By.XPATH, "//div[@data-testid='video_modal_title']").text
        
        # Получение точных данных по просмотрам и дате через ActionChains
        views_and_date_element = driver.find_element(By.XPATH, "//div[@data-testid='video_modal_additional_info']")
        actions = ActionChains(driver)
        actions.move_to_element(views_and_date_element).perform()
        time.sleep(1)  # Небольшая задержка для появления всплывающей подсказки
        tooltip = driver.find_element(By.XPATH, "//div[contains(@class, 'vkuiTooltipBase')]")
        views, date = tooltip.text.split('·')
        likes = driver.find_element(By.XPATH, "//div[@data-testid='video_modal_like_button']//span[contains(@class, 'PostFooterAction-module__label')]").text
        channel_name = driver.find_element(By.XPATH, "//div[@class='vkuiSimpleCell__middle']//a").text
        subscribers = driver.find_element(By.XPATH, "//div[@class='vkuiSimpleCell__middle']//div[@class='vkuiSimpleCell__content'][2]").text

        file.write(f"Название видео: {title}\n")
        file.write(f"Просмотры: {views.strip()}\n")
        file.write(f"Дата создания: {date.strip()}\n")
        file.write(f"Лайки: {likes.strip()}\n")
        file.write(f"Канал: {channel_name}\n")
        file.write(f"Подписчики: {subscribers.strip()}\n\n")
    except Exception as e:
        file.write(f"Ошибка на {video_url}: {e}\n")

# Функция обработки списка видео
def process_videos(driver, file, video_links):
    for i, video in enumerate(video_links):
        try:
            video_url = video.get_attribute('href')
            driver.execute_script(f"window.open('{video_url}');")
            driver.switch_to.window(driver.window_handles[-1])
            if "video" in driver.current_url:
                file.write(f"Видео {i+1}:\nСсылка: {video_url}\n")
                extract_video_data(driver, file, video_url)
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
        except Exception as e:
            file.write(f"Ошибка при обработке видео {i+1}: {e}\n")
            driver.switch_to.window(driver.window_handles[0])

# Открываем страницу "Для вас"
driver.get("https://vk.com/video")
video_links = driver.find_elements(By.XPATH, "//*[@id='video_type_trends_list']//a[@href and contains(@href, 'video-')]")
video_links = [video for idx, video in enumerate(video_links) if idx % 2 == 0][:5]

# Запись данных "Для вас"
with open('vk_video_data.txt', 'w', encoding='utf-8') as file:
    file.write(f"Количество видео 'Для вас': {len(video_links)}\n\n")
    process_videos(driver, file, video_links)

# Открываем страницу "Тренды"
driver.get("https://vk.com/video/trends")
video_trends_links = driver.find_elements(By.XPATH, "//*[@id='video_type_popular_trends_list']//a[@href and contains(@href, 'video-')]")
video_trends_links = [video for idx, video in enumerate(video_trends_links) if idx % 2 == 0][:5]

# Запись данных "Тренды"
with open('vk_video_data.txt', 'a', encoding='utf-8') as file:
    file.write(f"Количество видео 'Тренды': {len(video_trends_links)}\n\n")
    process_videos(driver, file, video_trends_links)

driver.quit()
