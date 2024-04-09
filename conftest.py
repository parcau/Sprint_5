import pytest
from selenium import webdriver

@pytest.fixture(scope='function')
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get("https://stellarburgers.nomoreparties.site/")
    return chrome_driver
