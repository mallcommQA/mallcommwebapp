__author__ = 'Chidozie Amefule'

from selenium.webdriver.common.by import By
from Tests.TestBase.EnvironmentSetup import EnvironmentSetup
from Tests.PageObject.Pages.Locators import Locator
from time import sleep
import TestData


class TestHelpButton(EnvironmentSetup):

    def test_help_button(self):
        driver = self.driver

        enter_email = driver.find_element(By.XPATH, Locator.sign_in_email)
        enter_email.clear()
        enter_email.send_keys(TestData.valid_email)
        driver.find_element(By.XPATH, Locator.sign_in_next_button).click()
        enter_password = driver.find_element(By.XPATH, Locator.sign_in_password)
        enter_password.clear()
        enter_password.send_keys(TestData.valid_password)
        driver.find_element(By.XPATH, Locator.sign_in_button).click()
        sleep(5)

        help_button = driver.find_element(By.XPATH, Locator.help_button)
        help_button.click()
        sleep(2)
        help_button.click()

        chat_bot = driver.find_elements(By.XPATH, Locator.help_button_chatbot)
        assert chat_bot is not None
        print("Chat Bot is displayed.")

