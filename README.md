# Selenium Test Suite for Stellar Burgers

Этот проект содержит набор автоматических тестов для веб-сайта [Stellar Burgers](https://stellarburgers.nomoreparties.site/). Тесты написаны на Python с использованием библиотеки Selenium и предназначены для проверки различных сценариев взаимодействия с сайтом.


Описание тестов
test_login_use_personal_account: Проверяет вход в личный кабинет через форму авторизации.
test_registration_field_name_empty: Проверяет, что форма регистрации не позволяет зарегистрироваться без заполнения всех обязательных полей.
test_login_to_on_main_menu: Проверяет вход в личный кабинет через главное меню.
test_logout_to_account: Проверяет успешный выход из аккаунта пользователя.
test_personal_account_to_constructor: Проверяет переход из личного кабинета в конструктор бургеров.
test_registration_valid_data: Проверяет успешную регистрацию нового пользователя с корректными данными.
test_registration_field_name_empty: Проверяет отображение ошибки при вводе некорректного пароля.
test_switch_buns: Проверяет переключение на вкладку "Булки" и выбор первого элемента.
test_switch_fillings: Проверяет переключение на вкладку "Начинки" и выбор первого элемента.
Локаторы
Файл locators.py содержит все используемые в тестах XPATH-локаторы для элементов сайта:

incorrect_password_warning: Локатор для сообщения об ошибке некорректного пароля.
name_field: Поле ввода имени.
email_field: Поле ввода электронной почты.
password_field: Поле ввода пароля.
register_button: Кнопка регистрации.
login_to_account: Кнопка входа в аккаунт.
login: Кнопка входа.
personal_account: Локатор для ссылки на личный кабинет.
constructor_link: Ссылка на конструктор бургеров.
constructor_header: Заголовок конструктора бургеров.
logout_button: Кнопка выхода из аккаунта.
buns: Вкладка "Булки".
buns_item: Элемент списка булок.
fillings: Вкладка "Начинки".
fillings_item: Элемент списка начинок.


Требования
Python 3.x
Selenium
ChromeDriver