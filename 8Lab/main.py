from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Запуск браузера
driver = webdriver.Chrome()
driver.maximize_window()

# Открытие страницы со списком стихотворений
driver.get("https://www.culture.ru/literature/poems/author-aleksandr-pushkin")
driver.execute_script("window.open('https://translate.yandex.ru');")
driver.switch_to.window(driver.window_handles[0])

# Извлекаем полный текст первых восьми стихотворений
# Извлекаем полный текст первых восьми стихотворений
poems = []
poem_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "ICocV"))
)[:8]

for element in poem_elements:
    # Получаем URL страницы стихотворения
    poem_url = element.get_attribute("href")

    # Открываем новую вкладку и переходим к стихотворению
    driver.execute_script(f"window.open('{poem_url}', '_blank');")
    driver.switch_to.window(driver.window_handles[-1])

    # Ожидание загрузки блоков текста стихотворения
    poem_text_blocks = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, '//div[@data-content="text"]'))
    )[:2]  # Извлекаем только первые три блока текста

    # Объединение текста из первых трех блоков
    poem_text = "\n".join([block.get_attribute("innerHTML").replace("<br>", "\n") for block in poem_text_blocks])

    # Удаление нежелательных символов, таких как &nbsp;
    poem_text = poem_text.replace("&nbsp;", " ")

    # Добавляем текст стихотворения в список
    poems.append(poem_text)

    # Закрываем текущую вкладку и возвращаемся к списку стихотворений
    driver.close()
    driver.switch_to.window(driver.window_handles[0])


# Переход на вкладку Яндекс.Переводчика
driver.switch_to.window(driver.window_handles[1])

driver.find_element(By.XPATH, '//*[@id="langsPanel"]/div[2]/div/div/button[2] ').click()

translations = []
for index, poem in enumerate(poems, start=1):
    # Ожидание и ввод текста для перевода
    input_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "fakeArea"))
    )
    input_box.clear()
    input_box.click()
    input_box.send_keys(poem)

    # Ожидание появления текста перевода
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "EzKURWReUAB5oZgtQNkl"))
    )
    
    # Получение текста перевода
    translated_text_elements = driver.find_elements(By.CLASS_NAME, "EzKURWReUAB5oZgtQNkl")
    translated_text = " ".join([element.text for element in translated_text_elements])

    # Добавление в список переводов
    translations.append(f"Стих {index}:\nОригинал:\n{poem}\nПеревод:\n{translated_text}\n\n")

# Запись результатов в файл
with open("Python/8Lab/translated_poems.txt", "w", encoding="utf-8") as file:
    file.write("\n\n".join(translations))

# Закрытие браузера
driver.quit()