from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import StellaBurgersLocators
from faker import Faker


fake = Faker()


class TestStellaBurgerRegistration:

    # Проверяем успешную регистрацию
    def test_registration(self, driver):
        registration_successfully = "https://stellarburgers.nomoreparties.site/login"
        driver.find_element(*StellaBurgersLocators.ENTER_ACCOUNT_BUTTON).click()
        driver.find_element(*StellaBurgersLocators.REGISTRATION_BUTTON).click()
        driver.find_elements(By.NAME, "name")[0].send_keys(fake.name())
        driver.find_elements(By.NAME, "name")[1].send_keys(fake.email())
        driver.find_element(By.NAME, "Пароль").send_keys("123456789")
        driver.find_element(*StellaBurgersLocators.CONFIRM_REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, "//button[text() = 'Войти']")
            )
        )
        url_after_click_registartion = driver.current_url
        assert registration_successfully == url_after_click_registartion

        driver.quit()

    # Проверяем ошибку валидации длины пароля
    def test_password_error_registration(self, driver):
        registration_successfully = "https://stellarburgers.nomoreparties.site/login"
        driver.find_element(*StellaBurgersLocators.ENTER_ACCOUNT_BUTTON).click()
        driver.find_element(*StellaBurgersLocators.REGISTRATION_BUTTON).click()
        driver.find_elements(By.NAME, "name")[0].send_keys(fake.name())
        driver.find_elements(By.NAME, "name")[1].send_keys(fake.email())
        driver.find_element(By.NAME, "Пароль").send_keys("12345")
        driver.find_element(*StellaBurgersLocators.CONFIRM_REGISTRATION_BUTTON).click()
        password_error = driver.find_element(
            By.XPATH, './/p[@class="input__error text_type_main-default"]'
        ).text
        assert password_error == "Некорректный пароль"

        driver.quit()
