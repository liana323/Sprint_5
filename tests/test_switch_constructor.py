from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import locators

def test_switch_sauces(driver):
    driver.get("https://stellarburgers.nomoreparties.site")

    # Переходим на вкладку соусы
    sauces_tab = driver.find_element(By.XPATH, locators.sauces)
    sauces_tab.click()

    # Ожидание, пока первый элемент вкладки "Соусы" станет видимым
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located((By.XPATH, locators.sauce_item))
    )

    # Проверяем, что первый элемент вкладки "Соусы" отображается
    assert driver.find_element(By.XPATH, locators.sauce_item).is_displayed()

def test_switch_buns(driver):
    driver.get("https://stellarburgers.nomoreparties.site")

    # Переходим на вкладку булки
    buns_tab = driver.find_element(By.XPATH, locators.buns)
    buns_tab.click()

    # Ожидание, пока первый элемент вкладки "Булки" станет видимым
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located((By.XPATH, locators.buns_item))
    )

    # Проверяем, что первый элемент вкладки "Булки" отображается
    assert driver.find_element(By.XPATH, locators.buns_item).is_displayed()

def test_switch_fillings(driver):
    driver.get("https://stellarburgers.nomoreparties.site")

    # Переходим на вкладку начинки
    fillings_tab = driver.find_element(By.XPATH, locators.fillings)
    fillings_tab.click()

    # Ожидание, пока первый элемент вкладки "Начинки" станет видимым
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located((By.XPATH, locators.fillings_item))
    )

    # Проверяем, что первый элемент вкладки "Начинки" отображается
    assert driver.find_element(By.XPATH, locators.fillings_item).is_displayed()