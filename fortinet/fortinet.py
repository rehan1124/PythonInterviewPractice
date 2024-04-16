import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

URL = "https://www.saucedemo.com/"
IMPLICIT_WAIT = 15
STANDARD_USER = "standard_user"
LOCKED_USER = "locked_out_user"
PASSWORD = "secret_sauce"
SLEEP = 0


def wait_for(sleep_seconds):
    time.sleep(sleep_seconds)


def login_to_app(driver, _username, _password):
    username = driver.find_element(By.ID, "user-name")
    username.clear()
    username.send_keys(_username)
    # Enter Password
    password = driver.find_element(By.ID, "password")
    password.clear()
    password.send_keys(_password)


def logout(driver):
    driver.find_element(By.ID, "react-burger-menu-btn").click()
    driver.find_element(By.ID, "logout_sidebar_link").click()


def main():
    # Create Chrome driver
    driver = webdriver.Chrome()

    # Navigate to URL, add implicit wait, maximize browser
    driver.get(URL)
    driver.implicitly_wait(IMPLICIT_WAIT)
    driver.maximize_window()

    try:
        login_to_app(driver, STANDARD_USER, PASSWORD)
        wait_for(SLEEP)
        # Login to app
        login_btn = driver.find_element(By.ID, "login-button")
        login_btn.click()
        wait_for(SLEEP)
        print("Logged into application")

        # Sort based on Price (low to high)
        sort_dropdown = driver.find_element(
            By.CSS_SELECTOR, "[data-test='product-sort-container']"
        )
        select = Select(sort_dropdown)
        select.select_by_visible_text("Price (low to high)")
        wait_for(SLEEP)
        print("Sorted entries from low to high")

        # Locate Add to cart button
        add_to_cart = driver.find_elements(By.XPATH, "//button[text()='Add to cart']")
        # Add lowest priced item to cart
        add_to_cart[0].click()
        wait_for(SLEEP)
        print("Added lower priced item to cart")

        # Remove item added from cart
        remove_btn = driver.find_element(By.XPATH, "//button[text()='Remove']")
        remove_btn.click()
        wait_for(SLEEP)
        print("Removed item from cart")

        # Add next lower priced item
        add_to_cart[1].click()
        wait_for(SLEEP)
        print("Added next lowest priced item to cart")

        cart_btn = driver.find_element(
            By.CSS_SELECTOR, "[data-test='shopping-cart-badge']"
        )
        assert cart_btn.text == "1"
        wait_for(SLEEP)
        print("Validate cart value")
        cart_btn.click()

        # Perform checkout
        checkout_btn = driver.find_element(By.ID, "checkout")
        checkout_btn.click()
        wait_for(SLEEP)
        print("Perform checkout")

        # Fill in basic details and click on continue
        firstname = driver.find_element(By.ID, "first-name")
        firstname.send_keys("Test1")
        lastname = driver.find_element(By.ID, "last-name")
        lastname.send_keys("User1")
        postal_code = driver.find_element(By.ID, "postal-code")
        postal_code.send_keys("560037")
        wait_for(SLEEP)
        continue_btn = driver.find_element(By.ID, "continue")
        continue_btn.click()
        print("Filled in basic details")

        # Finish checkout
        finish_btn = driver.find_element(By.ID, "finish")
        finish_btn.click()
        print("Finish checkout")

        order_thanks = driver.find_element(
            By.CSS_SELECTOR, "[data-test='complete-header']"
        )
        assert order_thanks.text == "Thank you for your order!"
        print("Order is placed successfully")
        logout(driver)

        print("Login with locked out user")
        login_to_app(driver, LOCKED_USER, PASSWORD)
        wait_for(SLEEP)
        driver.find_element(By.ID, "login-button").click()
        error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
        assert error.text == "Epic sadface: Sorry, this user has been locked out."
        print("Error validated successfully")

    except Exception as e:
        print("Some error occurred...")
        print(e)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
