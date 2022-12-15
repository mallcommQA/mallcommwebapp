__author__ = 'Chidozie Amefule'

from selenium.webdriver.common.by import By
from Tests.TestBase.EnvironmentSetup import EnvironmentSetup
from Tests.PageObject.Pages.Locators import Locator
from time import sleep
import TestData


class TestCentreSwitch(EnvironmentSetup):

    # Check that user can switch from one centre to another
    def test_user_can_switch_centre(self):
        driver = self.driver
    # Sign in to user account
        enter_email = driver.find_element(By.XPATH, Locator.sign_in_email)
        enter_email.clear()
        enter_email.send_keys(TestData.valid_email)
        driver.find_element(By.XPATH, Locator.sign_in_next_button).click()
        enter_password = driver.find_element(By.XPATH, Locator.sign_in_password)
        enter_password.clear()
        enter_password.send_keys(TestData.valid_password)
        driver.find_element(By.XPATH, Locator.sign_in_button).click()
        sleep(5)

    # Switch to another centre
        driver.find_element(By.XPATH, Locator.switch_centre_button).click()
        sleep(1)
        search_button = driver.find_element(By.XPATH, Locator.switch_centre_search_button)
        assert search_button.is_displayed()

        driver.find_element(By.XPATH, Locator.alt_centre).click()
        sleep(5)
        print("Centre switch successful.")
