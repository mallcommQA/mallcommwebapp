__author__ = 'Chidozie Amefule'

from selenium.webdriver.common.by import By
from Tests.TestBase.EnvironmentSetup import EnvironmentSetup
from Tests.PageObject.Pages.Locators import Locator
import TestData
from time import sleep


class TestLockedAccount(EnvironmentSetup):

    # Check that user is locked out after unsuccessful multiple attempts to sign in
    def test_account_locked_after_multiple_password_attempts(self):
        driver = self.driver

        # Enter valid email and then enter invalid password up to 5 times
        password_entry = 0
        while password_entry < 5:
            enter_email = driver.find_element(By.XPATH, Locator.sign_in_email)
            enter_email.clear()
            enter_email.send_keys(TestData.locked_email_address)
            driver.find_element(By.XPATH, Locator.sign_in_next_button).click()
            enter_password = driver.find_element(By.XPATH, Locator.sign_in_password)
            enter_password.clear()
            enter_password.send_keys(TestData.locked_password)
            driver.find_element(By.XPATH, Locator.sign_in_button).click()
            sleep(2)
            password_entry += 1
        alert = driver.find_element(By.XPATH, Locator.locked_account_message)
        if password_entry == 5:
            # Confirm that a message is displayed notifying that account is locked
            assert alert.is_displayed()
            print("Account is locked after multiple unsuccessful password entry attempts.")


