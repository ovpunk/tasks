# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()


def wait_element(by, value):
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((by, value)))
    return element


def wait_element_for_click(by, value):
    element = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((by, value))
        )
    return element


def test_first_case():
    try:
        driver.get("https://sbis.ru/")
        contacts = wait_element_for_click(By.CSS_SELECTOR, '.sbisru-Header__menu-item-1')
        contacts.click()

        tensor = wait_element_for_click(By.CSS_SELECTOR, '.sbisru-Contacts__logo-tensor')
        tensor.click()

        driver.switch_to.window(driver.window_handles[1])

        # power_is_in_people_block = wait_element(By.XPATH, '//*[contains(text(), "Сила в людях")]')
        power_is_in_people_block = wait_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-content .tensor_ru-Index__card-title')
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", power_is_in_people_block)
        assert power_is_in_people_block.text == 'Сила в людях', 'Блок не найден'

        tensor_about = wait_element_for_click(By.CSS_SELECTOR, '.tensor_ru-Index__block4-content a.tensor_ru-link')
        tensor_about.click()
        url = driver.current_url
        assert url == 'https://tensor.ru/about', 'Ожидается другой URL'

    finally:
        driver.quit()



