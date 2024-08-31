from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import locators


def test_registration_field_name_empty():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/register")

    # Поля ввода для регистрации и ввод невалидного email
    driver.find_element(By.XPATH, locators.name_field).send_keys("Lia")
    driver.find_element(By.XPATH, locators.email_field).send_keys("gsfdgsfgfsd")
    driver.find_element(By.XPATH, locators.password_field).send_keys("4154151")
    driver.find_element(By.XPATH, locators.register_button).click()

    # Ожидание появления ошибки о некорректном email
    error_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//p[@class='input__error text_type_main-default' and text()='Такой пользователь уже существует']")))

    # кнопка "Зарегистрироваться" не кликабельна
    assert error_message.is_displayed()

    # Закрытие браузера
    driver.quit()
