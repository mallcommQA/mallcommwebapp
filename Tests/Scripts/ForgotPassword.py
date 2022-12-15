__author__ = 'Chidozie Amefule'

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from Tests.TestBase.EnvironmentSetup import EnvironmentSetup
from Tests.PageObject.Pages.Locators import Locator
from time import sleep
import TestData


class TestForgotPassword(EnvironmentSetup):

    def test_forgot_password(self):
        driver = self.driver

        # Enter valid email address
        valid_email = driver.find_element(By.XPATH, Locator.sign_in_email)
        valid_email.clear()
        valid_email.send_keys(TestData.valid_email_2)
        driver.find_element(By.XPATH, Locator.sign_in_next_button).click()

        # Click the forgotten password link
        driver.find_element(By.XPATH, Locator.forgot_password_link).click()
        driver.find_element(By.XPATH, Locator.send_password_reset_email_button).click()
        sleep(2)

        # Check that email is sent successfully
        reset_password_email = driver.find_element(By.XPATH, Locator.confirm_reset_password_email_sent)
        assert reset_password_email.is_displayed()
        print("Password Reset email sent successfully.")
