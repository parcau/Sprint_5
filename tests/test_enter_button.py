from selenium.webdriver.common.by import By
from locators import StellaBurgersLocators

enter_page_url = 'https://stellarburgers.nomoreparties.site/login'
class TestButtonNavigation:

    # Проверяем вход по кнопке "Войти в аккаунт"
    def test_enter_in_account_button(self, driver):
        driver.find_element(*StellaBurgersLocators.ENTER_ACCOUNT_BUTTON).click()
        expected_url = driver.current_url
        assert expected_url == enter_page_url

        driver.quit()

    # Проверяем вход по кнопке "Личный кабинет"
    def test_personal_cabinet_button(self, driver):
        driver.find_element(*StellaBurgersLocators.PERSONAL_CABINET_BUTTON).click()
        expected_url = driver.current_url
        assert expected_url == enter_page_url

        driver.quit()

    # Проверяем вход через кнопку в форме регистрации
    def test_login_button_in_registration_form(self, driver):
        driver.find_element(*StellaBurgersLocators.ENTER_ACCOUNT_BUTTON).click()
        driver.find_element(*StellaBurgersLocators.REGISTRATION_BUTTON).click()
        driver.find_element(By.XPATH, "//a[text()= 'Войти']").click()
        expected_url = driver.current_url
        assert expected_url == enter_page_url

        driver.quit()

    # Проверяем вход через кнопку в форме восстановления пароля
    def test_login_button_in_restore_password(self, driver):
        driver.find_element(*StellaBurgersLocators.ENTER_ACCOUNT_BUTTON).click()
        driver.find_element(*StellaBurgersLocators.RESTORE_PASSWORD_BUTTON).click()
        driver.find_element(By.XPATH, "//a[text()= 'Войти']").click()
        expected_url = driver.current_url
        assert expected_url == enter_page_url

        driver.quit()