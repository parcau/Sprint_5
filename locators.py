from selenium.webdriver.common.by import By

class StellaBurgersLocators:
    REGISTRATION_NAME_INPUT = (By.XPATH, "//label[text() = 'Имя']/../input") # поле Имя в форме регистрации
    REGISTRATION_EMAIL_INPUT = (By.XPATH, "//label[text() = 'Email']/../input") # поле Email в форме регистрации
    REGISTRATION_PASSWORD_INPUT = (By.XPATH, "//label[text() = 'Пароль']/../input") # поле Пароль в форме регистрации
    INCORRECT_PASSWORD_INSCRIPTION = (By.XPATH, ".//p[@class='input__error text_type_main-default']") #надпись "Неккоретный пароль"
    ENTER_ACCOUNT_BUTTON = (By.XPATH, "//button[text()= 'Войти в аккаунт']")  # кнопка "Войти в аккаунт"
    AUTH_EMAIL_INPUT = (By.NAME, "name") # Поле ввода email при авторизации
    AUTH_PASSWORD_INPUT = (By.NAME, "Пароль") # Поел ввода password при авторизации
    HISTORY_ORDERS_BUTTON = (By.XPATH, "//a[text()= 'История заказов']") # кнопка "История заказов" в личном кабинете
    REGISTRATION_BUTTON = (By.XPATH, "//a[text()= 'Зарегистрироваться']") # кнопка "Зарегистрироваться"
    LOGIN_BUTTON_IN_RESTORE_PASSWORD = (By.XPATH, "//a[text()= 'Войти']") #кнопка "Войти" в разделе восстановления пароля
    LOGIN_BUTTON_IN_REGISTRATION_FORM = (By.XPATH, "//a[text()= 'Войти']") #кнопка "Войти" в форме регистрации
    CONFIRM_REGISTRATION_BUTTON = (By.XPATH, "//button[text()= 'Зарегистрироваться']") # кнопка подтверждения регистрации
    PERSONAL_CABINET_BUTTON = (By.XPATH, "//p[text()= 'Личный Кабинет']") # Кнопка "Личный кабинет"
    RESTORE_PASSWORD_BUTTON = (By.XPATH, "//a[text()= 'Восстановить пароль']") # кнопка "Восстановить пароль"
    LOGIN_BUTTON = (By.XPATH, "//button[text()= 'Войти']") # кнопка "Войти" при авторизации
    QUIT_PERSONAL_CABINET = (By.XPATH, "//button[text()= 'Выход']") # кнопка "Выход" в личном кабинете
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text() = 'Конструктор']") # кнопка Конструктор
    LOGO_BUTTON = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2") # логотип сайта
    COLLECT_BURGER_TEXT = (By.XPATH, "//h1[text()= 'Соберите бургер']") # надпись "Соберите бургер"
    SAUCES_LOCATION_BUTTON = (By.XPATH, "//span[text() = 'Соусы']") # кнопка "Соусы" в конструкторе
    SAUCES_PARRENT_CLASS = (By.XPATH, "//span[text()= 'Соусы']/parent::div")
    FILINGS_LOCATION_BUTTON = (By.XPATH, "//span[text() = 'Начинки']") #кнопка "Начинки" в конструкторе
    FILINGS_PARRENT_CLASS = (By.XPATH, "//span[text()= 'Начинки']/parent::div")
    BUNS_LOCATION_BUTTON = (By.XPATH, "//span[text()= 'Булки']") #кнопка "Булки" в конструкторе
    BUNS_PARRENT_CLASS = (By.XPATH, "//span[text()= 'Булки']/parent::div")
    CURRENT_SECTION_IN_CONSTRUCTOR_BUTTON = (
        By.XPATH,
        "//div[@class= 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']",
    )  # Класс выбранного раздела в Конструкторе
