__author__ = 'Chidozie Amefule'

from selenium.webdriver.common.by import By
from Tests.TestBase.EnvironmentSetup import EnvironmentSetup
from Tests.PageObject.Pages.Locators import Locator
from time import sleep
import TestData


# Test that user can register for another store
class TestRegisterForAnotherStore(EnvironmentSetup):

    def test_another_store_register(self):
        driver = self.driver
        # Sign in
        enter_email = driver.find_element(By.XPATH, Locator.sign_in_email)
        enter_email.clear()
        enter_email.send_keys(TestData.valid_email)
        driver.find_element(By.XPATH, Locator.sign_in_next_button).click()
        enter_password = driver.find_element(By.XPATH, Locator.sign_in_password)
        enter_password.clear()
        enter_password.send_keys(TestData.valid_password)
        driver.find_element(By.XPATH, Locator.sign_in_button).click()
        sleep(5)

        # Go to Edit Profile page
        driver.find_element(By.XPATH, Locator.avatar).click()
        # Go to Register for another store
        driver.find_element(By.XPATH, Locator.register_for_another_store).click()
        # Select centre to register to
        driver.find_element(By.XPATH, Locator.profile_select_centre_dropdown).click()
        driver.find_element(By.XPATH, Locator.profile_selected_centre).click()
        sleep(1)
        driver.find_element(By.XPATH, Locator.profile_selected_centre_next).click()
        # Select store to register
        driver.find_element(By.XPATH, Locator.profile_select_store_dropdown).click()
        driver.find_element(By.XPATH, Locator.profile_selected_store).click()
        sleep(1)
        driver.find_element(By.XPATH, Locator.profile_selected_store_next).click()
        # Accept terms & conditions
        driver.find_element(By.XPATH, Locator.profile_terms_condition_tick_box).click()
        driver.find_element(By.XPATH, Locator.profile_terms_condition_tick_box_next).click()
        # Enter password
        driver.find_element(By.XPATH, Locator.register_for_another_store_password).send_keys(TestData.password)
        driver.find_element(By.XPATH, Locator.register_for_another_store_confirm_password).send_keys(TestData.password)
        driver.find_element(By.XPATH, Locator.register_for_another_store_register_button).click()
        # Check confirmation message is displayed
        register_successful = driver.find_element(By.XPATH, Locator.registration_success_display)
        assert register_successful.is_displayed()
        driver.find_element(By.XPATH, Locator.continue_tab).click()
        sleep(5)
        print("Successfully registered for another store")





