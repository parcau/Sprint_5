from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import StellaBurgersLocators
from data import StellaBurgerTestData
from faker import Faker
import urls


fake = Faker()

class TestStellaBurgerRegistration:

    # Проверяем успешную регистрацию
    def test_registration(self, driver):
        driver.find_element(*StellaBurgersLocators.ENTER_ACCOUNT_BUTTON).click()
        driver.find_element(*StellaBurgersLocators.REGISTRATION_BUTTON).click()
        driver.find_element(*StellaBurgersLocators.REGISTRATION_NAME_INPUT).send_keys(fake.name())
        driver.find_element(*StellaBurgersLocators.REGISTRATION_EMAIL_INPUT).send_keys(fake.email())
        driver.find_element(*StellaBurgersLocators.REGISTRATION_PASSWORD_INPUT).send_keys(fake.password())
        driver.find_element(*StellaBurgersLocators.CONFIRM_REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located
            ((StellaBurgersLocators.LOGIN_BUTTON))
        )
        url_after_click_registartion = driver.current_url
        assert urls.REGISTRATION_SUCCES_URL == url_after_click_registartion

    # Проверяем ошибку валидации длины пароля
    def test_password_error_registration(self, driver):
        driver.find_element(*StellaBurgersLocators.ENTER_ACCOUNT_BUTTON).click()
        driver.find_element(*StellaBurgersLocators.REGISTRATION_BUTTON).click()
        driver.find_element(*StellaBurgersLocators.REGISTRATION_NAME_INPUT).send_keys(fake.name())
        driver.find_element(*StellaBurgersLocators.REGISTRATION_EMAIL_INPUT).send_keys(fake.email())
        driver.find_element(*StellaBurgersLocators.REGISTRATION_PASSWORD_INPUT).send_keys(StellaBurgerTestData.INCORRECT_PASSWORD)
        driver.find_element(*StellaBurgersLocators.CONFIRM_REGISTRATION_BUTTON).click()
        password_error = driver.find_element(*StellaBurgersLocators.INCORRECT_PASSWORD_INSCRIPTION).text
        assert password_error == "Некорректный пароль"

