from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import locators

def test_switch_sauces(driver):

    driver.get("https://stellarburgers.nomoreparties.site")

    #переходим на вкладку соусы
    driver.find_element(By.XPATH,locators.sauses)
    #ждем
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, locators.sauce_item)))

    #кликаем на первый отобразившийся элемент
    driver.find_element(By.XPATH, locators.sauce_item).click()

     #проверяем что это соуc
    element = driver.find_element(By.XPATH, locators.item_name_in_card).text
    assert 'Соус' in element

def test_switch_buns():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site")
    # переходим на вкладку начинки т.у. булки по умолчанию
    driver.find_element(By.XPATH, locators.fillings)

    #переходим на вкладку булки
    driver.find_element(By.XPATH,locators.buns)
    #ждем
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, locators.buns_item)))

    #кликаем на первый отобразившийся элемент
    driver.find_element(By.XPATH, locators.buns_item).click()

    # проверяем что это булка
    element = driver.find_element(By.XPATH, locators.item_name_in_card).text
    assert 'булка' in element

def test_switch_fillings():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site")

    # переходим на вкладку начинки
    driver.find_element(By.XPATH, locators.fillings)
    #ждем
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, locators.fillings_item)))

    # кликаем на первый отобразившийся элемент
    driver.find_element(By.XPATH, locators.fillings_item).click()

    # проверяем
    element = driver.find_element(By.XPATH, locators.item_name_in_card).text
    assert 'Мясо бессмертных моллюсков Protostomia' in element
