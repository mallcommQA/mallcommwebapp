__author__ = 'Chidozie Amefule'

from selenium.webdriver.common.by import By
from Tests.TestBase.EnvironmentSetup import EnvironmentSetup
from Tests.PageObject.Pages.Locators import Locator
from time import sleep
import TestData


class TestSettings(EnvironmentSetup):

    def test_settings_functions(self):
        driver = self.driver

        # Sign in to account
        enter_email = driver.find_element(By.XPATH, Locator.sign_in_email)
        enter_email.clear()
        enter_email.send_keys(TestData.valid_email)
        driver.find_element(By.XPATH, Locator.sign_in_next_button).click()
        enter_password = driver.find_element(By.XPATH, Locator.sign_in_password)
        enter_password.clear()
        enter_password.send_keys(TestData.valid_password)
        driver.find_element(By.XPATH, Locator.sign_in_button).click()
        sleep(5)

        # Go to settings page
        settings_page = driver.find_element(By.XPATH, Locator.settings_button)
        settings_page.click()
        sleep(2)
        assert "settings" in driver.current_url
        print("Settings url is: " + driver.current_url)

        # Check list of languages displayed
        choose_language_label = driver.find_element(By.XPATH, Locator.choose_language_tab)
        assert choose_language_label.is_displayed()
        choose_language_label.click()
        sleep(1)
        # Confirm list of languages displayed
        language_list = driver.find_elements(By.XPATH, Locator.settings_language_list)
        assert len(language_list) == 15
        for item in language_list:
            print(item.get_attribute("text"))

        # Test English US switch
        driver.find_element(By.XPATH, Locator.settings_english_us).click()
        sleep(1)

        # Test Czech switch
        choose_language_label.click()
        driver.find_element(By.XPATH, Locator.settings_czech).click()
        sleep(1)

        # Test Danish switch
        choose_language_label.click()
        driver.find_element(By.XPATH, Locator.settings_danish).click()
        sleep(1)

        # Test Dutch switch
        choose_language_label.click()
        driver.find_element(By.XPATH, Locator.settings_dutch).click()
        sleep(1)

        # Test French switch
        choose_language_label.click()
        driver.find_element(By.XPATH, Locator.settings_french).click()
        sleep(1)

        # Test German switch
        choose_language_label.click()
        driver.find_element(By.XPATH, Locator.settings_german).click()
        sleep(1)

        # Test Hungarian switch
        choose_language_label.click()
        driver.find_element(By.XPATH, Locator.settings_hungarian).click()
        sleep(1)

        # Test Italian switch
        choose_language_label.click()
        driver.find_element(By.XPATH, Locator.settings_italian).click()
        sleep(1)

        # Test Polish switch
        choose_language_label.click()
        driver.find_element(By.XPATH, Locator.settings_polish).click()
        sleep(1)

        # Test Slovak switch
        choose_language_label.click()
        driver.find_element(By.XPATH, Locator.settings_slovak).click()
        sleep(1)

        # Test Spanish switch
        choose_language_label.click()
        driver.find_element(By.XPATH, Locator.settings_spanish).click()
        sleep(1)

        # Test Swedish switch
        choose_language_label.click()
        driver.find_element(By.XPATH, Locator.settings_swedish).click()
        sleep(1)

        # Test Turkish switch
        choose_language_label.click()
        driver.find_element(By.XPATH, Locator.settings_turkish).click()
        sleep(1)

        # Test Arabic switch
        choose_language_label.click()
        driver.find_element(By.XPATH, Locator.settings_arabic).click()
        sleep(1)

        # Test English switch
        choose_language_label.click()
        driver.find_element(By.XPATH, Locator.settings_english_uk).click()
        sleep(1)

        # Check Terms & Conditions button
        driver.find_element(By.XPATH, Locator.settings_terms_conditions).click()
        check_content = driver.find_element(By.XPATH, Locator.settings_terms_conditions_content)
        assert check_content.is_displayed()










