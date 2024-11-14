from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Пути к драйверу и браузеру
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
    except Exception as e:
        file.write(f"Ошибка при загрузке заголовка видео на {video_url}: {e}\n")
        return

    try:
        title = driver.find_element(By.XPATH, "//div[@data-testid='video_modal_title']").text
        file.write(f"Название видео: {title}\n")
    except Exception as e:
        file.write(f"Ошибка при извлечении названия видео на {video_url}: {e}\n")

    try:
        views_and_date_element = driver.find_element(By.XPATH, "//div[@data-testid='video_modal_additional_info']")
        actions = ActionChains(driver)
        actions.move_to_element(views_and_date_element).perform()
        time.sleep(1)
        tooltip = driver.find_element(By.XPATH, "//div[contains(@class, 'vkuiTooltipBase')]")
        tooltip_text = tooltip.text
        views, date = tooltip_text.split("·")
        file.write(f"Точные просмотры: {views.strip()}\n")
        file.write(f"Точная дата создания: {date.strip()}\n")
    except Exception as e:
        file.write(f"Ошибка при извлечении точных просмотров и даты на {video_url}: {e}\n")

    try:
        likes = driver.find_element(By.XPATH, "//div[@data-testid='video_modal_like_button']//span[contains(@class, 'PostFooterAction-module__label')]").text
        file.write(f"Лайки: {likes.strip()}\n")
    except Exception as e:
        file.write(f"Ошибка при извлечении лайков на {video_url}: {e}\n")

    try:
        channel_name = driver.find_element(By.XPATH, "//div[@class='vkuiSimpleCell__middle']//a").text
        file.write(f"Название канала: {channel_name}\n")
    except Exception as e:
        file.write(f"Ошибка при извлечении названия канала на {video_url}: {e}\n")

    try:
        subscribers = driver.find_element(By.XPATH, "//div[@class='vkuiSimpleCell__middle']//div[@class='vkuiSimpleCell__content']/span").text
        file.write(f"Подписчики на канале: {subscribers.strip()}\n")
    except Exception as e:
        file.write(f"Ошибка при извлечении количества подписчиков на канале на {video_url}: {e}\n")

    file.write("\n")

# Функция для обработки видео на странице
def process_videos(driver, file, video_links):
    for i, video in enumerate(video_links):
        try:
            video_url = video.get_attribute('href')
            driver.execute_script(f"window.open('{video_url}');")
            driver.switch_to.window(driver.window_handles[-1])

            if "video" in driver.current_url:
                file.write(f"Видео {i+1}:\n")
                file.write(f"Ссылка: {video_url}\n")
                extract_video_data(driver, file, video_url)
            else:
                file.write(f"Видео {i+1}: неверный URL - {driver.current_url}\n")

            driver.close()
            driver.switch_to.window(driver.window_handles[0])
        except Exception as e:
            file.write(f"Ошибка при обработке видео {i+1}: {e}\n")
            driver.switch_to.window(driver.window_handles[0])

# Открываем страницу "Для вас" и собираем видео
driver.get("https://vk.com/video")
video_links_for_you = driver.find_elements(By.XPATH, "//*[@id='video_type_trends_list']//a[@href and contains(@href, 'video')]")
video_links_for_you = video_links_for_you[:5]

# Открываем страницу "Тренды" и собираем видео
driver.get("https://vk.com/video/trends")
video_links_trends = driver.find_elements(By.XPATH, "//*[@id='video_type_popular_trends_list']//a[@href and contains(@href, 'video')]")
video_links_trends = video_links_trends[:5]

# Открываем файл для записи результатов
with open('vk_video_data.txt', 'w', encoding='utf-8') as file:
    file.write(f"Количество видео с 'Для вас': {len(video_links_for_you)}\n\n")
    process_videos(driver, file, video_links_for_you)

    file.write(f"Количество видео с 'Тренды': {len(video_links_trends)}\n\n")
    process_videos(driver, file, video_links_trends)

# Закрываем браузер
driver.quit()
