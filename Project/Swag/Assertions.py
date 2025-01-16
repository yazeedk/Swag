from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import unittest


class Assertions:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def login_assertions(self):
        elements = Elements(self.driver)
        assert_prepare = elements.assert_title()
        title = assert_prepare.text
        print(title)
        unittest.TestCase().assertEqual(title, "Products")
        return self

    def add_assertions(self):
        elements = Elements(self.driver)
        assert_remove = elements.assert_add_to_cart()
        unittest.TestCase().assertEqual(assert_remove.text, "Remove")
        return self

    def click_cart_assertions(self):
        elements = Elements(self.driver)
        assert_cart = elements.assert_click_cart()
        unittest.TestCase().assertEqual(assert_cart.text, "Your Cart")
        return self

    def click_checkout_assertions(self):
        elements = Elements(self.driver)
        assert_checkout = elements.assert_checkout()
        unittest.TestCase().assertEqual(assert_checkout.text, "Checkout: Your Information")
        return self

    def fill_first_name_assertions(self):
        elements = Elements(self.driver)
        fill_first_name = elements.fill_first_name()
        unittest.TestCase().assertEqual(fill_first_name.get_attribute("value"), "Yazeed")
        return self

    def fill_last_name_assertions(self):
        elements = Elements(self.driver)
        fill_last_name = elements.fill_last_name()
        unittest.TestCase().assertEqual(fill_last_name.get_attribute("value"), "deriah")
        return self

    def fill_zip_assertions(self):
        elements = Elements(self.driver)
        fill_zip = elements.fill_zip_code()
        unittest.TestCase().assertEqual(fill_zip.get_attribute("value"), "123")
        return self

    def continue_shopping_assert(self):
        self.login_assertions()
        return self

    def menu_icon_assert(self):
        elements = Elements(self.driver)
        logout_button = elements.log_out_action()
        title = logout_button.text
        unittest.TestCase().assertEqual(title, "Logout")
        return self

    def log_out_assertion(self):
        elements = Elements(self.driver)
        log_out_assert = elements.log_out_assertion()
        title = log_out_assert.text
        unittest.TestCase().assertEqual(title, "Project")
        return self



class Elements:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def assert_title(self):
        return self.driver.find_element(By.CLASS_NAME, "title")

    def assert_add_to_cart(self):
        return self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")

    def assert_click_cart(self):
        return self.driver.find_element(By.CLASS_NAME, "shopping_cart_link")

    def assert_checkout(self):
        return self.driver.find_element(By.ID, "checkout")

    def fill_first_name(self):
        return self.driver.find_element(By.ID, "first-name")

    def fill_last_name(self):
        return self.driver.find_element(By.ID, "last-name")

    def fill_zip_code(self):
        return self.driver.find_element(By.ID, "postal-code")

    def log_out_action(self):
        return self.driver.find_element(By.ID, "react-burger-menu-btn")

    def log_out_assertion(self):
        return self.driver.find_element(By.CLASS_NAME, "app_logo")
