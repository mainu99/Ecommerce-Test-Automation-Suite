from selenium import webdriver
import pytest

@pytest.fixture
def setup_driver():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()