__author__ = "Chidozie Amefule"

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from Tests.TestBase.EnvironmentSetup import EnvironmentSetup
from Tests.PageObject.Pages.Locators import Locator
from Tests.Scripts.SignIn import TestSignIn
from time import sleep
import TestData

# Test data
search_word = "store"


class TestHeaderTab(EnvironmentSetup):

    def test_header_tab_items(self):
        driver = self.driver

        # Sign in
        enter_email = driver.find_element(By.XPATH, Locator.sign_in_email)
        enter_email.clear()
        enter_email.send_keys(TestData.valid_email_3)
        driver.find_element(By.XPATH, Locator.sign_in_next_button).click()
        enter_password = driver.find_element(By.XPATH, Locator.sign_in_password)
        enter_password.clear()
        enter_password.send_keys(TestData.valid_password_1)
        driver.find_element(By.XPATH, Locator.sign_in_button).click()
        sleep(5)

        # Check header items
        menu = driver.find_element(By.XPATH, Locator.menu_button)
        menu.click()
        sleep(2)
        menu.click()

        # Confirm centre name displayed
        centre = driver.find_element(By.XPATH, Locator.centre_name)
        print("Centre name displayed is: " + centre.get_attribute("text"))

        # Check notification button can open and close
        notification = driver.find_element(By.XPATH, Locator.notification_bell)
        notification.click()
        sleep(1)
        close_notification = driver.find_element(By.XPATH, Locator.close_notification_button)
        close_notification.click()

        # Check search button can search and find items
        search = driver.find_element(By.XPATH, Locator.search_button)
        search.click()
        driver.find_element(By.XPATH, Locator.search_box).send_keys(search_word)
        sleep(2)
        search.click()

        # Check help button works and displays list of help questions
        help_button = driver.find_element(By.XPATH, Locator.help_button)
        help_button.click()
        assert driver.find_element(By.XPATH, Locator.help_button_chatbot_header).is_displayed()
        help_button.click()

        # Check settings button is functional
        settings = driver.find_element(By.XPATH, Locator.settings_button)
        settings.click()

        # Check logout button is functional
        logout_button = driver.find_element(By.XPATH, Locator.logout)
        logout_button.click()
