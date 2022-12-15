__author__ = 'Chidozie Amefule'

from selenium.common.exceptions import NoSuchElementException
from selenium. webdriver.common.by import By
from Tests.TestBase.EnvironmentSetup import EnvironmentSetup
from Tests.PageObject.Pages.Locators import Locator
from time import sleep
import TestData


class TestRegistration(EnvironmentSetup):

    def test_email_already_registered(self):
        driver = self.driver

        # Check if email is already registered
        enter_email = driver.find_element(By.XPATH, Locator.register_email)
        enter_email.clear()
        enter_email.send_keys(TestData.registered_email_address)

        driver.find_element(By.XPATH, Locator.register_next_button).click()
        sleep(2)

        enter_password_page_displayed = driver.find_element(By.XPATH, Locator.forgot_password_link)
        if enter_password_page_displayed is not None:
            print("This email address is already registered")
        else:
            print("Email address is not yet registered.")

    def test_new_registration(self):
        driver = self.driver

        # Check that user can register successfully
        enter_email = driver.find_element(By.XPATH, Locator.register_email)
        enter_email.clear()
        enter_email.send_keys(TestData.unregistered_email_address)

        driver.find_element(By.XPATH, Locator.register_next_button).click()
        sleep(2)

        # Check if first name field is left blank, a warning message is displayed
        try:
            driver.find_element(By.XPATH, Locator.register_next_button_2).click()
            warning_message = driver.find_element(By.XPATH, Locator.first_name_empty_warning)
            if warning_message.is_displayed():
                print(warning_message.get_attribute("text"))
        except NoSuchElementException:
            pass

        driver.find_element(By.XPATH, Locator.register_first_name).send_keys(TestData.firstname)

        # Check if last name is left blank, a warning message is displayed
        enter_lastname = driver.find_element(By.XPATH, Locator.register_last_name)
        enter_lastname.clear()
        try:
            driver.find_element(By.XPATH, Locator.register_next_button_2).click()
            warning_message2 = driver.find_element(By.XPATH, Locator.last_name_empty_warning)
            if warning_message2.is_displayed():
                print(warning_message2.get_attribute("text"))
        except NoSuchElementException:
            pass
        enter_lastname.send_keys(TestData.lastname)

        # Enter phone number is optional
        enter_phone = driver.find_element(By.XPATH, Locator.phone_number)
        enter_phone.clear()
        enter_phone.send_keys(TestData.phone)
        sleep(2)

        driver.find_element(By.XPATH, Locator.register_next_button_2).click()

        enter_password = driver.find_element(By.XPATH, Locator.password)
        enter_password.clear()
        enter_password.send_keys(TestData.new_user_password)

        enter_confirm_password = driver.find_element(By.XPATH, Locator.confirm_password)
        enter_confirm_password.clear()
        enter_confirm_password.send_keys(TestData.new_user_password)
        sleep(2)

        driver.find_element(By.XPATH, Locator.register_next_button_3).click()

        #choose_centre = driver.find_element(By.XPATH, Locator.select_centre_dropdown)
        #choose_centre.click()
        #chosen_centre = driver.find_element(By.XPATH, Locator.selected_centre)
        #chosen_centre.click()

        choose_store = driver.find_element(By.XPATH, Locator.select_store_dropdown)
        choose_store.click()
        chosen_store = driver.find_element(By.XPATH, Locator.selected_store)
        chosen_store.click()
        sleep(2)

        driver.find_element(By.XPATH, Locator.register_next_button_4).click()

        driver.find_element(By.XPATH, Locator.terms_conditions_tick_box).click()

        driver.find_element(By.XPATH, Locator.register_button).click()
        sleep(2)

        # Confirm registration successful
        verify_link = driver.find_element(By.XPATH, Locator.confirm_registration)
        if verify_link.is_displayed():
            print("Registration is successful.")

    def test_newly_registered_user_signin(self):
        driver = self.driver
        # Check that newly registered user can sign in successfully
        enter_email = driver.find_element(By.XPATH, Locator.sign_in_email)
        enter_email.clear()
        enter_email.send_keys(TestData.unregistered_email_address)

        driver.find_element(By.XPATH, Locator.sign_in_next_button).click()

        enter_password = driver.find_element(By.XPATH, Locator.sign_in_password)
        enter_password.clear()
        enter_password.send_keys(TestData.new_user_password)

        driver.find_element(By.XPATH, Locator.sign_in_button).click()
        sleep(5)
        # Confirm sign in successful
        assert "dashboard" in driver.current_url
        print("Successfully Signed In new User.")
