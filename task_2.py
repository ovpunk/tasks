# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver import Keys
from time import sleep

driver = webdriver.Chrome()
driver.implicitly_wait(30)

LOGIN = ''
PASSWORD = ''


def wait_element(by, value):
    element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((by, value)))
    return element


def wait_element_for_click(by, value):
    element = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((by, value))
        )
    return element


def test_second_case():
    try:
        driver.get("https://fix-online.sbis.ru/")
        sleep(5)
        login = wait_element_for_click(By.CSS_SELECTOR, '.controls-InputBase__nativeField_caretFilled')
        login.send_keys(LOGIN, Keys.ENTER)

        password = wait_element(By.CSS_SELECTOR, '.controls-Password__nativeField_caretFilled')
        password.send_keys(PASSWORD, Keys.ENTER)

        contacts = driver.find_element(By.CSS_SELECTOR, '[data-qa="Контакты"] [data-qa="counter"]')
        driver.execute_script("arguments[0].click();", contacts)

        chats = wait_element_for_click(By.CSS_SELECTOR, '[title="Чаты"]')
        chats.click()

        text_editor = wait_element_for_click(By.CSS_SELECTOR, '.textEditor_Viewer__Paragraph ')
        sleep(5)
        text_editor.click()
        text_editor.send_keys('hi')
        send_button = wait_element_for_click(By.CSS_SELECTOR, '[title="Создать новый диалог"]')
        send_button.click()
        message = wait_element(By.CSS_SELECTOR, '.msg-Correspondence__DialogItem')
        assert message.is_displayed(), 'Сообщение не найдено'

        message_wrapper = driver.find_element(By.CSS_SELECTOR,
                                              '.msg-CorrespondenceDetail.controls-Scroll-containerBase_userContent')
        action_chains = ActionChains(driver)
        action_chains.move_to_element(message_wrapper)
        action_chains.perform()
        delete_button = driver.find_element(By.CSS_SELECTOR, '[data-qa="controls-itemActions__action del"]')
        action_chains.move_to_element(delete_button)
        action_chains.perform()
        delete_button.click()

        no_messages = driver.find_element(By.XPATH, '//*[contains(text(), "У вас нет сообщений")]')
        assert no_messages.text == "У вас нет сообщений", 'Сообщение не удалено'

    finally:
        driver.quit()



