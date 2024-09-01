from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import locators


def test_registration_field_name_empty(driver):

    driver.get("https://stellarburgers.nomoreparties.site/register")

    # Поля ввода для регистрации и ввод валидных данных
    driver.find_element(By.XPATH, locators.name_field).send_keys("")
    driver.find_element(By.XPATH, locators.email_field).send_keys("liana_mantashyan_13_767@mail.com")
    driver.find_element(By.XPATH, locators.password_field).send_keys("4154151")

    # Сохраняем текущий URL до нажатия кнопки
    current_url = driver.current_url

    # Нажатие на кнопку регистрации
    driver.find_element(By.XPATH, locators.register_button).click()

    # Ожидание перенаправления на  страницу входа
    WebDriverWait(driver, 2)

    # кнопка "Зарегистрироваться" не кликабельна
    assert driver.current_url == current_url





