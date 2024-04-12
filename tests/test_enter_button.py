import urls
from locators import StellaBurgersLocators


class TestButtonNavigation:

    # Проверяем вход по кнопке "Войти в аккаунт"
    def test_enter_in_account_button(self, driver):
        driver.find_element(*StellaBurgersLocators.ENTER_ACCOUNT_BUTTON).click()
        expected_url = driver.current_url
        assert expected_url == urls.ENTER_PAGE_URL


    # Проверяем вход по кнопке "Личный кабинет"
    def test_personal_cabinet_button(self, driver):
        driver.find_element(*StellaBurgersLocators.PERSONAL_CABINET_BUTTON).click()
        expected_url = driver.current_url
        assert expected_url == urls.ENTER_PAGE_URL


    # Проверяем вход через кнопку в форме регистрации
    def test_login_button_in_registration_form(self, driver):
        driver.find_element(*StellaBurgersLocators.ENTER_ACCOUNT_BUTTON).click()
        driver.find_element(*StellaBurgersLocators.REGISTRATION_BUTTON).click()
        driver.find_element(*StellaBurgersLocators.LOGIN_BUTTON_IN_REGISTRATION_FORM).click()
        expected_url = driver.current_url
        assert expected_url == urls.ENTER_PAGE_URL


    # Проверяем вход через кнопку в форме восстановления пароля
    def test_login_button_in_restore_password(self, driver):
        driver.find_element(*StellaBurgersLocators.ENTER_ACCOUNT_BUTTON).click()
        driver.find_element(*StellaBurgersLocators.RESTORE_PASSWORD_BUTTON).click()
        driver.find_element(*StellaBurgersLocators.LOGIN_BUTTON_IN_RESTORE_PASSWORD).click()
        expected_url = driver.current_url
        assert expected_url == urls.ENTER_PAGE_URL
