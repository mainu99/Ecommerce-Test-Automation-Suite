import os
from dotenv import load_dotenv
from selenium.webdriver.common.by import By

load_dotenv()
def test_valid_login(setup_driver):
    driver = setup_driver
    username = os.getenv('SAUCEDEMO_USERNAME')
    password = os.getenv('SAUCEDEMO_PASSWORD')
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    assert "inventory.html" in driver.current_url


def test_invalid_login(setup_driver):
    driver = setup_driver
    driver.find_element(By.ID, "user-name").send_keys("dummy_username")
    driver.find_element(By.ID, "password").send_keys("dummy_password")
    driver.find_element(By.ID, "login-button").click()
    error_msg = driver.find_element(By.CLASS_NAME, "error-message-container").text
    assert "Epic sadface" in error_msg


def test_invalid_login_wrong_password(setup_driver):
    driver = setup_driver
    username = os.getenv('USERNAME')
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys("dummy_password")
    driver.find_element(By.ID, "login-button").click()
    error_msg = driver.find_element(By.CLASS_NAME, "error-message-container").text
    assert "Epic sadface" in error_msg


def test_invalid_login_wrong_username(setup_driver):
    driver = setup_driver
    password = os.getenv('SAUCEDEMO_PASSWORD')
    driver.find_element(By.ID, "user-name").send_keys("dummy_username")
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    error_msg = driver.find_element(By.CLASS_NAME, "error-message-container").text
    assert "Epic sadface" in error_msg


def test_invalid_login_no_username(setup_driver):
    driver = setup_driver
    driver.find_element(By.ID, "user-name").send_keys("")
    driver.find_element(By.ID, "password").send_keys("dummy_password")
    driver.find_element(By.ID, "login-button").click()
    error_msg = driver.find_element(By.CLASS_NAME, "error-message-container").text
    assert "Username is required" in error_msg

def test_invalid_login_no_password(setup_driver):
    driver = setup_driver
    username = os.getenv('USERNAME')
    driver.find_element(By.ID, "user-name").send_keys(username)
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
