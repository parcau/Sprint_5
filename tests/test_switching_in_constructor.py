from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import StellaBurgersLocators
from data import StellaBurgerTestData

class TestSwitchingInConstructor:
    # Проверяем переход в раздел "Соусы"
    def test_switch_to_sauces_section(self, driver):
        driver.find_element(*StellaBurgersLocators.ENTER_ACCOUNT_BUTTON).click()
        driver.find_element(*StellaBurgersLocators.AUTH_EMAIL_INPUT).send_keys(StellaBurgerTestData.AUTH_EMAIL)
        driver.find_element(*StellaBurgersLocators.AUTH_PASSWORD_INPUT).send_keys(StellaBurgerTestData.AUTH_PASSWORD)
        driver.find_element(*StellaBurgersLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                (StellaBurgersLocators.SAUCES_LOCATION_BUTTON)
            )
        )
        driver.find_element(*StellaBurgersLocators.SAUCES_LOCATION_BUTTON).click()
        sauces_class_parent = driver.find_element(*StellaBurgersLocators.SAUCES_PARRENT_CLASS)
        current_button_class = driver.find_element(*StellaBurgersLocators.CURRENT_SECTION_IN_CONSTRUCTOR_BUTTON)
        assert sauces_class_parent == current_button_class

    # Проверяем переход в раздел "Начинки"
    def test_switch_to_filings_section(self, driver):
        driver.find_element(*StellaBurgersLocators.ENTER_ACCOUNT_BUTTON).click()
        driver.find_element(*StellaBurgersLocators.AUTH_EMAIL_INPUT).send_keys(StellaBurgerTestData.AUTH_EMAIL)
        driver.find_element(*StellaBurgersLocators.AUTH_PASSWORD_INPUT).send_keys(StellaBurgerTestData.AUTH_PASSWORD)
        driver.find_element(*StellaBurgersLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                (StellaBurgersLocators.FILINGS_LOCATION_BUTTON)
            )
        )
        driver.find_element(*StellaBurgersLocators.FILINGS_LOCATION_BUTTON).click()
        filings_class_parent = driver.find_element(*StellaBurgersLocators.FILINGS_PARRENT_CLASS)
        current_button_class = driver.find_element(*StellaBurgersLocators.CURRENT_SECTION_IN_CONSTRUCTOR_BUTTON)
        assert filings_class_parent == current_button_class

    #Проверяем переход в раздел "Булки"
    def test_switch_to_buns(self, driver):
        driver.find_element(*StellaBurgersLocators.ENTER_ACCOUNT_BUTTON).click()
        driver.find_element(*StellaBurgersLocators.AUTH_EMAIL_INPUT).send_keys(StellaBurgerTestData.AUTH_EMAIL)
        driver.find_element(*StellaBurgersLocators.AUTH_PASSWORD_INPUT).send_keys(StellaBurgerTestData.AUTH_PASSWORD)
        driver.find_element(*StellaBurgersLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                (StellaBurgersLocators.FILINGS_LOCATION_BUTTON)
            )
        )
        driver.find_element(*StellaBurgersLocators.FILINGS_LOCATION_BUTTON).click()
        driver.find_element(*StellaBurgersLocators.BUNS_LOCATION_BUTTON).click()
        buns_class_parent = driver.find_element(*StellaBurgersLocators.BUNS_PARRENT_CLASS)
        current_button_class = driver.find_element(*StellaBurgersLocators.CURRENT_SECTION_IN_CONSTRUCTOR_BUTTON)
        assert buns_class_parent == current_button_class
