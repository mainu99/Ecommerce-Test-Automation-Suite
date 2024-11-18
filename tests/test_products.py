import pytest
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException


def login(driver, username="standard_user", password="secret_sauce"):
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    assert "inventory.html" in driver.current_url, "Login failed or did not navigate to inventory page!"


def test_products_are_displayed(setup_driver):
    driver = setup_driver
    login(driver)
    products = driver.find_elements(By.CLASS_NAME, "inventory_item")
    print(f'length of products: {len(products)}')
    assert len(products) > 0, "No products are displayed on the page!"


def test_add_product_to_cart(setup_driver):
    driver = setup_driver
    login(driver)
    driver.find_element(By.CLASS_NAME, "btn_inventory").click()
    cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert cart_badge.text == "1", "Cart count did not update!"

def test_remove_product_from_products_page(setup_driver):
    driver = setup_driver
    login(driver)
    add_to_cart_button = driver.find_element(By.CLASS_NAME, "btn_inventory")
    add_to_cart_button.click()
    try:
        # Relocate the button after the page updates
        add_to_cart_button = driver.find_element(By.CLASS_NAME, "btn_inventory")
        assert add_to_cart_button.text == "Remove", "Add to Cart button did not change to Remove after adding the product!"
        add_to_cart_button.click()
        add_to_cart_button = driver.find_element(By.CLASS_NAME, "btn_inventory")
        assert add_to_cart_button.text == "Add to cart", "Remove button did not revert to Add to Cart!"
    except StaleElementReferenceException as e:
        pytest.fail(f"Encountered StaleElementReferenceException: {str(e)}")

def test_product_details(setup_driver):
    driver = setup_driver
    login(driver)
    driver.find_element(By.CLASS_NAME, "inventory_item_name").click()
    assert "inventory-item.html" in driver.current_url
    product_name = driver.find_element(By.CLASS_NAME, "inventory_details_name").text
    product_price = driver.find_element(By.CLASS_NAME, "inventory_details_price").text
    assert product_name, "Product name is missing!"
    assert product_price, "Product price is missing!"
