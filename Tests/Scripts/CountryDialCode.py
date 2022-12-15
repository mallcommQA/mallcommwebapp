__author__ = 'Chidozie Amefule'

from selenium.webdriver.common.by import By
from Tests.TestBase.EnvironmentSetup import EnvironmentSetup
from Tests.PageObject.Pages.Locators import Locator
from time import sleep
import TestData


class TestCountryCodeSwitch(EnvironmentSetup):

    def test_country_code(self):
        driver = self.driver
    # Test that user can change country dial code during registration
        enter_email = driver.find_element(By.XPATH, Locator.register_email)
        enter_email.clear()
        enter_email.send_keys(TestData.email)
        driver.find_element(By.XPATH, Locator.register_next_button).click()

        driver.find_element(By.XPATH, Locator.country_code_dropdown).click()
        sleep(2)
        code_list = driver.find_elements(By.XPATH, Locator.country_code_list)
        # Confirm the number of country code displayed
        assert len(code_list) == 246

        # Check that country code can be changed
        # Switch country code United Kingdom
        uk = driver.find_element(By.XPATH, Locator.uk_country_code)
        uk.click()
        sleep(2)

        # Switch country code to United States
        driver.find_element(By.XPATH, Locator.country_code_dropdown).click()
        driver.find_element(By.XPATH, Locator.us_country_code).click()
        sleep(2)

        # Switch country code to France
        driver.find_element(By.XPATH, Locator.country_code_dropdown).click()
        driver.find_element(By.XPATH, Locator.france_country_code).click()
        sleep(2)
        print("Country Dial Code switching successfully.")



