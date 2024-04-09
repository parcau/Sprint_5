from selenium.webdriver.common.by import By


class StellaBurgersLocators:
    ENTER_ACCOUNT_BUTTON = (By.XPATH, "//button[text()= 'Войти в аккаунт']")  # кнопка "Войти в аккаунт"
    REGISTRATION_BUTTON = (By.XPATH, "//a[text()= 'Зарегистрироваться']") # кнопка "Зарегистрироваться"
    CONFIRM_REGISTRATION_BUTTON = (By.XPATH, "//button[text()= 'Зарегистрироваться']") # кнопка подтверждения регистрации
    PERSONAL_CABINET_BUTTON = (By.XPATH, "//p[text()= 'Личный Кабинет']") # Кнопка "Личный кабинет"
    RESTORE_PASSWORD_BUTTON = (By.XPATH, "//a[text()= 'Восстановить пароль']") # кнопка "Восстановить пароль"
    LOGIN_BUTTON = (By.XPATH, "//button[text()= 'Войти']") # кнопка "Войти" при авторизации
    QUIT_PERSONAL_CABINET = (By.XPATH, "//button[text()= 'Выход']") # кнопка "Выход" в личном кабинете
    CURRENT_SECTION_IN_CONSTRUCTOR_BUTTON = (
        By.XPATH,
        "//div[@class= 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']",
    )  # Класс выбранного раздела в Конструкторе
