__author__ = "Chidozie Amefule"

from imagesfile import profile_image
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from Tests.PageObject.Pages.Locators import Locator
from Tests.TestBase.EnvironmentSetup import EnvironmentSetup
from time import sleep
import TestData


class TestUserProfile(EnvironmentSetup):

    def test_profile_image_upload(self):
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

        # Upload profile image
        driver.find_element(By.XPATH, Locator.image).click()
        sleep(1)
        upload_image = driver.find_element(By.XPATH, Locator.input_image)
        upload_image.send_keys(profile_image)
        driver.find_element(By.XPATH, Locator.back_tab).click()
        sleep(3)
        print("Image uploaded successfully")

    def test_remove_profile_image(self):
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
        driver.find_element(By.XPATH, Locator.image).click()
        sleep(1)
        # Remove image
        driver.find_element(By.XPATH, Locator.remove_image).click()
        sleep(1)
        # Verify that image is removed
        verify_image_removed = driver.find_element(By.XPATH, Locator.image_input_text)
        assert verify_image_removed.is_displayed()
        driver.find_element(By.XPATH, Locator.back_tab).click()
        sleep(3)
        driver.find_element(By.XPATH, Locator.save_profile).click()
        print("Image removed successfully")




