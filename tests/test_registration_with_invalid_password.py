from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import locators


def test_registration_field_name_empty():

    driver.get("https://stellarburgers.nomoreparties.site/register")

    # Ввод данных в том числе некорретного пароля
    driver.find_element(By.XPATH, locators.name_field).send_keys("Lia")
    driver.find_element(By.XPATH, locators.email_field).send_keys("liana_mantashyan_13_767@mail.com")
    driver.find_element(By.XPATH, locators.password_field).send_keys("525")
    driver.find_element(By.XPATH, locators.register_button).click()

    # Ожидание появления ошибки о некорректном пароле
    error_message = driver.find_element(By.XPATH, locators.incorrect_password_warning).text
    # Выдает ошибку -
    assert error_message =='Некорректный пароль'






