from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import StellaBurgerTestData
import urls
from locators import StellaBurgersLocators


class TestPersonalCabinet:

    # Проверяем переход в личный кабинет по нажатию на кнопку "Личный кабинет"
    def test_enter_in_personal_cabinet_by_button(self, driver):
        driver.find_element(*StellaBurgersLocators.ENTER_ACCOUNT_BUTTON).click()
        driver.find_element(*StellaBurgersLocators.AUTH_EMAIL_INPUT).send_keys(StellaBurgerTestData.AUTH_EMAIL)
        driver.find_element(*StellaBurgersLocators.AUTH_PASSWORD_INPUT).send_keys(StellaBurgerTestData.AUTH_PASSWORD)
        driver.find_element(*StellaBurgersLocators.LOGIN_BUTTON).click()
        driver.find_element(*StellaBurgersLocators.PERSONAL_CABINET_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                (StellaBurgersLocators.HISTORY_ORDERS_BUTTON)
            )
        )
        url_personal_page = driver.current_url
        assert url_personal_page == urls.PERSONAL_CABINET_PAGE_URL

    # Проверяем выход из личного кабинета по кнопке
    def test_quit_from_personal_cabinet_by_button(self, driver):
        driver.find_element(*StellaBurgersLocators.ENTER_ACCOUNT_BUTTON).click()
        driver.find_element(*StellaBurgersLocators.AUTH_EMAIL_INPUT).send_keys(StellaBurgerTestData.AUTH_EMAIL)
        driver.find_element(*StellaBurgersLocators.AUTH_PASSWORD_INPUT).send_keys(StellaBurgerTestData.AUTH_PASSWORD)
        driver.find_element(*StellaBurgersLocators.LOGIN_BUTTON).click()
        driver.find_element(*StellaBurgersLocators.PERSONAL_CABINET_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                (StellaBurgersLocators.HISTORY_ORDERS_BUTTON)
            )
        )
        driver.find_element(*StellaBurgersLocators.QUIT_PERSONAL_CABINET).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                (StellaBurgersLocators.LOGIN_BUTTON)
            )
        )
        url_exit_personal_cabinet = driver.current_url
        assert url_exit_personal_cabinet == urls.ENTER_PAGE_URL
