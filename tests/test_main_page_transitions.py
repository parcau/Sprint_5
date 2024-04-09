from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import StellaBurgersLocators

main_page_url = "https://stellarburgers.nomoreparties.site/"


class TestTransitionFromLkToConstructor:
    # Проверяем переход из личного кабинета в конструктор, нажимая кнопку "Конструктор"
    def test_transition_click_button_constructor(self, driver):
        driver.find_element(*StellaBurgersLocators.ENTER_ACCOUNT_BUTTON).click()
        driver.find_element(By.NAME, "name").send_keys("markov7777@yandex.ru")
        driver.find_element(By.NAME, "Пароль").send_keys("123456789")
        driver.find_element(*StellaBurgersLocators.LOGIN_BUTTON).click()
        driver.find_element(*StellaBurgersLocators.PERSONAL_CABINET_BUTTON).click()
        driver.find_element(By.XPATH, "//p[text() = 'Конструктор']").click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, "//h1[text()= 'Соберите бургер']")
            )
        )
        expected_url = driver.current_url
        assert expected_url == main_page_url

        driver.quit()

    # Проверяем переход из личного кабинета в конструктор, нажимая на логотип сайта
    def test_transition_click_logo(self, driver):
        driver.find_element(*StellaBurgersLocators.ENTER_ACCOUNT_BUTTON).click()
        driver.find_element(By.NAME, "name").send_keys("markov7777@yandex.ru")
        driver.find_element(By.NAME, "Пароль").send_keys("123456789")
        driver.find_element(*StellaBurgersLocators.LOGIN_BUTTON).click()
        driver.find_element(*StellaBurgersLocators.PERSONAL_CABINET_BUTTON).click()
        driver.find_element(By.CLASS_NAME, "AppHeader_header__logo__2D0X2").click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, "//h1[text()= 'Соберите бургер']")
            )
        )
        expected_url = driver.current_url
        assert expected_url == main_page_url

        driver.quit()
