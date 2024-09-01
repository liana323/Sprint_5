import pytest
from selenium import webdriver
import pytest
import time
import random

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def email():
    unique_number = int(time.time())  # Используем текущее время для уникальности
    random_number = random.randint(100, 999)  # Добавляем случайное число для большей уникальности
    generated_email = f"user_{unique_number}_{random_number}@test.com"
    return generated_email