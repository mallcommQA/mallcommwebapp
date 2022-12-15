__author__ = 'Chidozie Amefule'

from selenium.webdriver.common.by import By
from Tests.TestBase.EnvironmentSetup import EnvironmentSetup
from Tests.PageObject.Pages.Locators import Locator
from time import sleep
import TestData


class TestChangePassword(EnvironmentSetup):

    # Test that a user can change password via User Profile
    def test_that_user_can_change_password(self):
        driver = self.driver
    # Sign In
        enter_email = driver.find_element(By.XPATH, Locator.sign_in_email)
        enter_email.clear()
        enter_email.send_keys(TestData.valid_email_1)
        driver.find_element(By.XPATH, Locator.sign_in_next_button).click()
        enter_password = driver.find_element(By.XPATH, Locator.sign_in_password)
        enter_password.clear()
        enter_password.send_keys(TestData.current_password)
        driver.find_element(By.XPATH, Locator.sign_in_button).click()
        sleep(3)
    # Take screenshot if password entered is invalid
        driver.get_screenshot_as_file("password_change.png")
        driver.save_screenshot("ScreenShots/password_change.png")
    # Navigate to User Profile
        driver.find_element(By.XPATH, Locator.avatar).click()
        sleep(2)
        driver.find_element(By.XPATH, Locator.profile_change_password).click()
    # Enter current password
        current_password = driver.find_element(By.XPATH, Locator.old_password)
        current_password.send_keys(TestData.current_password)
    # Enter new password
        password = driver.find_element(By.XPATH, Locator.new_password)
        password.send_keys(TestData.new_password)
        re_enter_password = driver.find_element(By.XPATH, Locator.confirm_new_password)
        re_enter_password.send_keys(TestData.new_password)
        driver.find_element(By.XPATH, Locator.save_profile).click()
        sleep(2)
    # Logout and re-login with the new password
        driver.find_element(By.XPATH, Locator.logout_button).click()
        enter_email = driver.find_element(By.XPATH, Locator.sign_in_email)
        enter_email.clear()
        enter_email.send_keys(TestData.valid_email_1)
        driver.find_element(By.XPATH, Locator.sign_in_next_button).click()
        enter_password = driver.find_element(By.XPATH, Locator.sign_in_password)
        enter_password.clear()
        enter_password.send_keys(TestData.new_password)
        driver.find_element(By.XPATH, Locator.sign_in_button).click()
        sleep(5)
    # Confirm sign in successful
        assert "dashboard" in driver.current_url
        print("Successfully signed in with new password")

