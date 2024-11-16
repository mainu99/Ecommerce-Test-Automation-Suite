from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture
def setup_driver():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()


def test_valid_login(setup_driver):
    driver = setup_driver
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    assert "inventory.html" in driver.current_url


def test_invalid_login(setup_driver):
    driver = setup_driver
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("<PASSWORD>")
    driver.find_element(By.ID, "login-button").click()
    error_msg = driver.find_element(By.CLASS_NAME, "error-message-container").text
    assert "Epic sadface" in error_msg


def test_ivalid_login_wrong_password(setup_driver):
    driver = setup_driver
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("wrong_password")
    driver.find_element(By.ID, "login-button").click()
    error_msg = driver.find_element(By.CLASS_NAME, "error-message-container").text
    assert "Epic sadface" in error_msg


def test_ivalid_login_wrong_username(setup_driver):
    driver = setup_driver
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("wrong_password")
    driver.find_element(By.ID, "login-button").click()
    error_msg = driver.find_element(By.CLASS_NAME, "error-message-container").text
    assert "Epic sadface" in error_msg


def test_invalid_login_no_username(setup_driver):
    driver = setup_driver
    driver.find_element(By.ID, "user-name").send_keys("")
    driver.find_element(By.ID, "password").send_keys("wrong_password")
    driver.find_element(By.ID, "login-button").click()
    error_msg = driver.find_element(By.CLASS_NAME, "error-message-container").text
    assert "Username is required" in error_msg

def test_invalid_login_no_password(setup_driver):
    driver = setup_driver
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("")
    driver.find_element(By.ID, "login-button").click()
    error_msg = driver.find_element(By.CLASS_NAME, "error-message-container").text
    assert "Password is required" in error_msg

def test_invalid_login_empty_fields(setup_driver):
    driver = setup_driver
    driver.find_element(By.ID, "user-name").send_keys("")
    driver.find_element(By.ID, "password").send_keys("")
    driver.find_element(By.ID, "login-button").click()
    error_msg = driver.find_element(By.CLASS_NAME, "error-message-container").text
    assert "Username is required" in error_msg
