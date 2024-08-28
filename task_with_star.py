# Перейти на  https://sbis.ru/
# В Footer'e найти "Скачать СБИС"
# Перейти по ней
# Скачать СБИС Плагин для вашей ОС в папку с данным тестом
# Убедиться, что плагин скачался
# Вывести на печать размер скачанного файла в мегабайтах
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

chrome_options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": f"{os.getcwd()}/downloads"
}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(30)

DOWNLOAD_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "downloads"))
print("DOWNLOAD_DIR:", DOWNLOAD_DIR)
FILE_NAME = "sbisplugin-setup-web.exe"
FILE_PATH = os.path.join(DOWNLOAD_DIR, FILE_NAME)


def wait_element_for_click(by, value):
    element = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((by, value))
        )
    return element


def test_third_case():
    try:
        driver.get('https://sbis.ru/')
        sleep(5)
        download_sbis_page = wait_element_for_click(By.CSS_SELECTOR, '[href="/download"]')
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", download_sbis_page)
        download_sbis_page.click()

        download_sbis_link = driver.find_element(By.CSS_SELECTOR,
                                                 '['
                                                 'href="https://update.sbis.ru/Sbis3Plugin/master/win32/sbisplugin-setup-web.exe"]')
        download_sbis_link.click()
        WebDriverWait(driver, 60).until(lambda _: os.path.exists(FILE_PATH))
        assert os.path.exists(FILE_PATH), "Файл не успел загрузиться"

        file_size = round(os.path.getsize(FILE_PATH) / 1024 / 1024, 2)
        print(f"Размер файла: {file_size}мб")
    finally:
        if os.path.exists(FILE_PATH):
            os.remove(FILE_PATH)
        driver.quit()

