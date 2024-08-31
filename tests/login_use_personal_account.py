from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import locators

def test_login_use_personal_account():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")

    # Клик по кнопке "Личный кабинет" на главной странице
    driver.find_element(By.XPATH, locators.personal_account).click()

    # Ожидание, пока URL изменится на страницу входа
    WebDriverWait(driver, 10).until(EC.url_contains("login"))

    # Поля ввода
    driver.find_element(By.XPATH, locators.email_field).send_keys("liana_mantashyan_13_987@mail.com")
    driver.find_element(By.XPATH, locators.password_field).send_keys("45611451")
    driver.find_element(By.XPATH, locators.login).click()

    # Ожидание, пока URL изменится на нужную страницу после регистрации
    WebDriverWait(driver, 10).until(EC.url_contains("site"))

    # Добавление assert для проверки, что произошло правильное перенаправление
    assert "site" in driver.current_url

    # Закрытие браузера
    driver.quit()

