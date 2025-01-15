import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

from QA.Actions import Actions
from QA.Assertions import Assertions
from QA.Elements import Elements


class MainClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):

        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        cls.driver = webdriver.Chrome(service=Service(), options=chrome_options)
        cls.driver.implicitly_wait(10)
        cls.driver.get("https://www.saucedemo.com/")
        cls.el = Elements(cls.driver)
        cls.ac = Actions(cls.driver)
        cls.ass = Assertions(cls.driver)

    def test_1_testing_login_page(self):

        self.ac.login_actions()
        self.ass.login_assertions()
        time.sleep(2)

    def test_2_test_add_to_cart(self):

        self.ac.add_action()
        self.ass.add_assertions()
        time.sleep(2)

    def test_3_test_cart_icon(self):

        self.ac.click_cart()
        self.ass.click_cart_assertions()
        time.sleep(2)

    def test_4_test_checkout(self):

        self.ac.click_checkout()
        self.ass.click_checkout_assertions()
        time.sleep(2)

    def test_5_test_datafile(self):

        self.ac.fill_first_name_action()
        # Uncomment below to include assertions
        # self.ass.fill_first_name_assertions()
        self.ac.fill_last_name_action()
        # Uncomment below to include assertions
        # self.ass.fill_last_name_assertions()
        self.ac.fill_zip_action()
        # Uncomment below to include assertions
        # self.ass.fill_zip_assertions()

    def test_6_test_logout(self):

        self.ac.cancel_action()
        self.ac.continue_shopping()
        self.ass.continue_shopping_assert()
        self.ac.menu_icon()
        self.ass.menu_icon_assert()

    @classmethod
    def tearDownClass(cls):

        cls.ac.log_out_action()
        cls.ass.log_out_assertion()
        time.sleep(3)
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
