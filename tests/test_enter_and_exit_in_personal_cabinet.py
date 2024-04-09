from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import StellaBurgersLocators

enter_page_url = "https://stellarburgers.nomoreparties.site/login"
personal_cabinet_page = "https://stellarburgers.nomoreparties.site/account/profile"

class TestPersonalCabinet:

    # Проверяем переход в личный кабинет по нажатию на кнопку "Личный кабинет"
    def test_enter_in_personal_cabinet_by_button(self, driver):
        driver.find_element(*StellaBurgersLocators.ENTER_ACCOUNT_BUTTON).click()
        driver.find_element(By.NAME, "name").send_keys("markov7777@yandex.ru")
        driver.find_element(By.NAME, "Пароль").send_keys("123456789")
        driver.find_element(*StellaBurgersLocators.LOGIN_BUTTON).click()
        driver.find_element(*StellaBurgersLocators.PERSONAL_CABINET_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, "//a[text()= 'История заказов']")
            )
        )
        url_personal_page = driver.current_url
        assert url_personal_page == personal_cabinet_page

        driver.quit()

    # Проверяем выход из личного кабинета по кнопке
    def test_quit_from_personal_cabinet_by_button(self, driver):
        driver.find_element(*StellaBurgersLocators.ENTER_ACCOUNT_BUTTON).click()
        driver.find_element(By.NAME, "name").send_keys("markov7777@yandex.ru")
        driver.find_element(By.NAME, "Пароль").send_keys("123456789")
        driver.find_element(*StellaBurgersLocators.LOGIN_BUTTON).click()
        driver.find_element(*StellaBurgersLocators.PERSONAL_CABINET_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, "//a[text()= 'История заказов']")
            )
        )
        driver.find_element(*StellaBurgersLocators.QUIT_PERSONAL_CABINET).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, "//button[text()= 'Войти']")
            )
        )
        url_exit_personal_cabinet = driver.current_url
        assert url_exit_personal_cabinet == enter_page_url

        driver.quit()
