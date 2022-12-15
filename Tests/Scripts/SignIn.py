__author__ = 'Chidozie Amefule'

from selenium.webdriver.common.by import By
from Tests.TestBase.EnvironmentSetup import EnvironmentSetup
from Tests.PageObject.Pages.Locators import Locator
from time import sleep
import TestData


class TestSignIn(EnvironmentSetup):

    # Check that User can sign in with valid credentials
    def test_valid_sign_in(self):
        driver = self.driver

        enter_email = driver.find_element(By.XPATH, Locator.sign_in_email)
        enter_email.clear()
        enter_email.send_keys(TestData.valid_email)
        sleep(1)
        driver.find_element(By.XPATH, Locator.sign_in_next_button).click()
        enter_password = driver.find_element(By.XPATH, Locator.sign_in_password)
        enter_password.clear()
        enter_password.send_keys(TestData.valid_password)
        sleep(1)
        driver.find_element(By.XPATH, Locator.sign_in_button).click()
        sleep(5)

    # Confirm sign in successful
        assert "dashboard" in driver.current_url
        print("Successfully Signed In.")

    # Test invalid login (Enter unregistered email address)
    def test_sign_in_unregistered_email(self):
        driver = self.driver

        enter_email = driver.find_element(By.XPATH, Locator.sign_in_email)
        enter_email.clear()
        enter_email.send_keys(TestData.unregistered_email)
        sleep(1)
        driver.find_element(By.XPATH, Locator.sign_in_next_button).click()

        redirect_to_register = driver.find_element(By.XPATH, Locator.unregistered_email_sign_in)
        assert redirect_to_register.is_displayed()
        print("Email address is not registered.")

    # Test invalid login (Enter invalid password)
    def test_sign_in_invalid_password(self):
        driver = self.driver
        enter_email = driver.find_element(By.XPATH, Locator.sign_in_email)
        enter_email.clear()
        enter_email.send_keys(TestData.valid_email)
        sleep(1)
        driver.find_element(By.XPATH, Locator.sign_in_next_button).click()
        enter_password = driver.find_element(By.XPATH, Locator.sign_in_password)
        enter_password.clear()
        enter_password.send_keys(TestData.invalid_password)
        sleep(1)

        driver.find_element(By.XPATH, Locator.sign_in_button).click()
        password_error_message = driver.find_elements(By.XPATH, Locator.invalid_password_message)
        assert password_error_message is not None
        print("Password entered is not valid")
