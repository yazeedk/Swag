from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class Elements:
    def __init__(self, driver: WebDriver):
        """
        Constructor to initialize the WebDriver instance.
        """
        self.driver = driver

    def user_name(self):
        return self.driver.find_element(By.ID, "user-name")

    def password(self):
        return self.driver.find_element(By.ID, "password")

    def button_login(self):
        return self.driver.find_element(By.ID, "login-button")

    def assert_title(self):
        return self.driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/span')

    def add_to_cart(self):
        return self.driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-onesie"]')

    def assert_add_to_cart(self):
        return self.driver.find_element(By.ID, "remove-sauce-labs-onesie")

    def click_to_cart(self):
        return self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge")

    def assert_click_cart(self):
        return self.driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/span')

    def click_checkout(self):
        return self.driver.find_element(By.ID, "checkout")

    def assert_checkout(self):
        return self.driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/span')

    def fill_first_name(self):
        return self.driver.find_element(By.ID, "first-name")

    def fill_last_name(self):
        return self.driver.find_element(By.ID, "last-name")

    def cancel(self):
        return self.driver.find_element(By.ID, "cancel")

    def continue_shopping(self):
        return self.driver.find_element(By.ID, "continue-shopping")

    def fill_zip_code(self):
        return self.driver.find_element(By.ID, "postal-code")

    def menu_click(self):
        return self.driver.find_element(By.ID, "react-burger-menu-btn")

    def log_out_action(self):
        return self.driver.find_element(By.ID, "logout_sidebar_link")

    def log_out_assertion(self):
        return self.driver.find_element(By.CSS_SELECTOR, "div.login_logo")
