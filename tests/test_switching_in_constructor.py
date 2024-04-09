from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import StellaBurgersLocators


class TestSwitchingInConstructor:
    # Проверяем переход в раздел "Соусы"
    def test_switch_to_sauces_section(self, driver):
        driver.find_element(*StellaBurgersLocators.ENTER_ACCOUNT_BUTTON).click()
        driver.find_element(By.NAME, "name").send_keys("markov7777@yandex.ru")
        driver.find_element(By.NAME, "Пароль").send_keys("123456789")
        driver.find_element(*StellaBurgersLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, "//span[text() = 'Соусы']")
            )
        )
        driver.find_element(By.XPATH, "//span[text()= 'Соусы']").click()
        sauces_button_parent = driver.find_element(By.XPATH, "//span[text()= 'Соусы']/parent::div")
        current_button_class = driver.find_element(*StellaBurgersLocators.CURRENT_SECTION_IN_CONSTRUCTOR_BUTTON)
        assert sauces_button_parent == current_button_class
        driver.quit()

    # Проверяем переход в раздел "Начинки"
    def test_switch_to_filings_section(self, driver):
        driver.find_element(*StellaBurgersLocators.ENTER_ACCOUNT_BUTTON).click()
        driver.find_element(By.NAME, "name").send_keys("markov7777@yandex.ru")
        driver.find_element(By.NAME, "Пароль").send_keys("123456789")
        driver.find_element(*StellaBurgersLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, "//span[text() = 'Начинки']")
            )
        )
        driver.find_element(By.XPATH, "//span[text()= 'Начинки']").click()
        filings_button_parent = driver.find_element(By.XPATH, "//span[text()= 'Начинки']/parent::div")
        current_button_class = driver.find_element(*StellaBurgersLocators.CURRENT_SECTION_IN_CONSTRUCTOR_BUTTON)
        assert filings_button_parent == current_button_class
        driver.quit()

    #Проверяем переход в раздел "Булки"
    def test_switch_to_buns(self, driver):
        driver.find_element(*StellaBurgersLocators.ENTER_ACCOUNT_BUTTON).click()
        driver.find_element(By.NAME, "name").send_keys("markov7777@yandex.ru")
        driver.find_element(By.NAME, "Пароль").send_keys("123456789")
        driver.find_element(*StellaBurgersLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, "//span[text() = 'Начинки']")
            )
        )
        driver.find_element(By.XPATH, "//span[text()= 'Начинки']").click()
        driver.find_element(By.XPATH, "//span[text()= 'Булки']").click()
        buns_button_parent = driver.find_element(By.XPATH, "//span[text()= 'Булки']/parent::div")
        current_button_class = driver.find_element(*StellaBurgersLocators.CURRENT_SECTION_IN_CONSTRUCTOR_BUTTON)
        assert buns_button_parent == current_button_class
        driver.quit()
