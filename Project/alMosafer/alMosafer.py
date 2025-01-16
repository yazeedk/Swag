import time
import random
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

class TestAlMosafer:

    alMosaferURL = "https://global.almosafer.com/en"
    driver = None
    wait = None

    arabicCitiesNames = ["\u062f\u0628\u064a", "\u062c\u062f\u0629"]  # Dubai, Jeddah in Arabic
    englishCitiesNames = ["Dubai", "Jeddah", "Riyadh"]

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get(cls.alMosaferURL)
        cls.driver.maximize_window()
        cls.wait = WebDriverWait(cls.driver, 10)

        welcome_screen = cls.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Kingdom of Saudi Arabia, SAR']")))
        welcome_screen.click()

    @pytest.mark.order(1)
    def test_check_language(self):
        actual_language = self.driver.find_element(By.TAG_NAME, "html").get_attribute("lang")
        expected_language = "en"
        assert actual_language == expected_language, "The language is not 'en'."

    @pytest.mark.order(1)
    def test_check_currency(self):
        currency_element = self.driver.find_element(By.CSS_SELECTOR, ".sc-dRFtgE.fPnvOO")
        actual_currency = currency_element.text
        expected_currency = "SAR"
        assert actual_currency == expected_currency, "Currency is not 'SAR'."

    @pytest.mark.order(1)
    def test_check_contact_number(self):
        contact_number_element = self.driver.find_element(By.CSS_SELECTOR, "a[class='sc-hUfwpO bWcsTG'] strong")
        actual_contact_number = contact_number_element.text
        expected_contact_number = "+966554400000"
        assert actual_contact_number == expected_contact_number, "Contact number is incorrect."

    @pytest.mark.order(1)
    def test_check_qitaff_logo(self):
        try:
            qitaff_logo = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='sc-dznXNo iZejAw']"))
            )
            assert qitaff_logo.is_displayed(), "Qitaff logo is not displayed."
        except TimeoutException:
            pytest.fail("Qitaff logo element was not found within the timeout period.")

    @pytest.mark.order(2)
    def test_hotel_tab_is_not_selected(self):
        hotel_tab = self.driver.find_element(By.ID, "uncontrolled-tab-example-tab-hotels")
        actual_status = hotel_tab.get_attribute("aria-selected")
        expected_status = "false"
        assert actual_status == expected_status, "Hotel tab should not be selected."

    @pytest.mark.order(3)
    def test_check_dates(self):
        departure_date_element = self.driver.find_element(By.CSS_SELECTOR, "div[class='sc-OxbzP sc-lnrBVv gKbptE'] span[class='sc-fvLVrH hNjEjT']")
        return_date_element = self.driver.find_element(By.CSS_SELECTOR, "div[class='sc-OxbzP sc-bYnzgO bojUIa'] span[class='sc-fvLVrH hNjEjT']")

        actual_departure_date = int(departure_date_element.text)
        actual_return_date = int(return_date_element.text)

        today = datetime.now()
        expected_departure_date = (today + timedelta(days=1)).day
        expected_return_date = (today + timedelta(days=2)).day

        assert actual_departure_date == expected_departure_date, "Departure date is incorrect."
        assert actual_return_date == expected_return_date, "Return date is incorrect."

    @pytest.mark.order(4)
    def test_check_language_switching(self):
        urls = ["https://global.almosafer.com/ar", "https://global.almosafer.com/en"]
        random_url = random.choice(urls)
        self.driver.get(random_url)

        hotel_tab = self.driver.find_element(By.ID, "uncontrolled-tab-example-tab-hotels")
        hotel_tab.click()

        try:
            search_hotel_input = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search for a hotel']"))
            )
            if "ar" in self.driver.current_url:
                search_hotel_input.send_keys(random.choice(self.arabicCitiesNames))
            else:
                search_hotel_input.send_keys(random.choice(self.englishCitiesNames))
        except TimeoutException:
            pytest.fail("Search input field was not found within the timeout period.")

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
