incorrect_password_warning = '//p[@class="input__error text_type_main-default"]'
name_field = "//label[text()='Имя']/following-sibling::input"
email_field = "//label[text()='Email']/following-sibling::input"
password_field = "//label[text()='Пароль']/following-sibling::input"
register_button = "//button[text()='Зарегистрироваться']"
login_to_account = "//button[text()= 'Войти в аккаунт']"
login = "//button[text()= 'Войти']"
personal_account = "//a[@href='/account']//p[contains(text(), 'Личный Кабинет')]"
constructor_link = '//a[@href="/" and @class="AppHeader_header__link__3D_hX"]'
constructor_header = '//h1[@class="text text_type_main-large mb-5 mt-10"]'
logout_button = "//button[contains(@class, 'Account_button__14Yp3') and text()='Выход']"


# Локаторы для переключения вкладок
sauces = '//span[contains(@class, "text_type_main-default") and text()="Соусы"]'
buns = '//h2[contains(@class, "text_type_main-medium") and text()="Булки"]'
fillings = '//span[contains(@class, "text_type_main-default") and text()="Начинки"]'

# Локаторы для элементов в каждой секции
sauce_item = '//p[contains(text(), "Соус Spicy")]'
buns_item = '//p[contains(text(), "Флюоресцентная булка")]'
fillings_item = '//p[contains(text(), "Мясо бессмертных моллюсков Protostomia")]'

# Локатор для проверки заголовка элемента
item_name_in_card = '//p[1][@class="text text_type_main-medium mb-8"]'
#
sauces_tab ="//div[contains(@class, 'current') and .//span[text()='Соусы']]"
buns_tab ="//div[contains(@class, 'current') and .//span[text()='Булки']]"
fillings_tab ="//div[contains(@class, 'current') and .//span[text()='Начинки']]"