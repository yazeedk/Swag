from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Actions:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def login_actions(self):
        elements = Elements(self.driver)
        username = elements.user_name()
        username.send_keys("problem_user")

        password = elements.password()
        password.send_keys("secret_sauce")

        login_button = elements.button_login()
        login_button.click()
        return self

    def add_action(self):
        elements = Elements(self.driver)
        add_cart_button = elements.add_to_cart()
        add_cart_button.click()
        return self

    def click_cart(self):
        self.driver.implicitly_wait(10)
        elements = Elements(self.driver)
        cart_icon = elements.click_to_cart()
        cart_icon.click()
        return self

    def click_checkout(self):
        elements = Elements(self.driver)
        checkout_button = elements.click_checkout()
        checkout_button.click()
        return self

    def fill_first_name_action(self):
        elements = Elements(self.driver)
        first_name_input = elements.fill_first_name()
        first_name_input.send_keys("Yazeed")
        return self

    def fill_last_name_action(self):
        elements = Elements(self.driver)
        last_name_input = elements.fill_last_name()
        last_name_input.send_keys("deriah")
        return self

    def fill_zip_action(self):
        elements = Elements(self.driver)
        zip_input = elements.fill_zip_code()
        zip_input.send_keys("123")
        return self

    def cancel_action(self):
        elements = Elements(self.driver)
        cancel_button = elements.cancel()
        cancel_button.click()
        return self

    def continue_shopping(self):
        elements = Elements(self.driver)
        continue_shopping_button = elements.continue_shopping()
        continue_shopping_button.click()
        return self

    def menu_icon(self):
        elements = Elements(self.driver)
        menu_icon_button = elements.menu_click()
        menu_icon_button.click()
        return self

    def log_out_action(self):
        elements = Elements(self.driver)
        logout_button = elements.log_out_action()
        logout_button.click()
        return self

class Elements:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def user_name(self):
        return self.driver.find_element(By.ID, "user-name")

    def password(self):
        return self.driver.find_element(By.ID, "password")

    def button_login(self):
        return self.driver.find_element(By.ID, "login-button")

    def add_to_cart(self):
        return self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")

    def click_to_cart(self):
        return self.driver.find_element(By.ID, "shopping_cart_container")

    def click_checkout(self):
        return self.driver.find_element(By.ID, "checkout")

    def fill_first_name(self):
        return self.driver.find_element(By.ID, "first-name")

    def fill_last_name(self):
        return self.driver.find_element(By.ID, "last-name")

    def fill_zip_code(self):
        return self.driver.find_element(By.ID, "postal-code")

    def cancel(self):
        return self.driver.find_element(By.ID, "cancel")

    def continue_shopping(self):
        return self.driver.find_element(By.ID, "continue-shopping")

    def menu_click(self):
        return self.driver.find_element(By.ID, "react-burger-menu-btn")

    def log_out_action(self):
        return self.driver.find_element(By.ID, "logout_sidebar_link")
