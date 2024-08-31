from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import locators

def test_registration_valid_data():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/register")

    #Поля ввода для регистрации
    driver.find_element(By.XPATH, locators.name_field).send_keys("Lidia")
    driver.find_element(By.XPATH, locators.email_field).send_keys("liana_mantashyan_13_987@mail.com")
    driver.find_element(By.XPATH, locators.password_field).send_keys("45611451")
    driver.find_element(By.XPATH, locators.register_button).click()

    #Ожидание перенаправления на  страницу входа
    WebDriverWait(driver, 10).until(EC.url_contains("login"))

    #Если регистрация успешная, то ты перенаправляешься на страницу с login
    assert "login" in driver.current_url

    # Закрытие браузера
    driver.quit()


