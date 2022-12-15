__author__ = 'Chidozie Amefule'

from selenium.webdriver.common.by import By
from Tests.TestBase.EnvironmentSetup import EnvironmentSetup
from Tests.PageObject.Pages.Locators import Locator
from time import sleep


class TestChangeLanguage(EnvironmentSetup):

    # Check list of languages
    def test_change_language_list(self):
        driver = self.driver
        driver.find_element(By.XPATH, Locator.change_language).click()
        sleep(2)
        all_languages = driver.find_elements(By.XPATH, Locator.language_list)
        assert all_languages is not None

        # Check that every language can be selected
        # Test English US switch
        driver.find_element(By.XPATH, Locator.english_us).click()
        sleep(1)
        us_flag_check = driver.find_element(By.XPATH, Locator.flag)
        print(us_flag_check.get_attribute("src"))

        # Test Czech switch
        driver.find_element(By.XPATH, Locator.change_language).click()
        sleep(1)
        driver.find_element(By.XPATH, Locator.czech).click()
        czech_flag_check = driver.find_element(By.XPATH, Locator.flag)
        print(czech_flag_check.get_attribute("src"))

        # Test Danish switch
        driver.find_element(By.XPATH, Locator.change_language).click()
        sleep(1)
        driver.find_element(By.XPATH, Locator.danish).click()
        danish_flag_check = driver.find_element(By.XPATH, Locator.flag)
        print(danish_flag_check.get_attribute("src"))

        # Test Dutch switch
        driver.find_element(By.XPATH, Locator.change_language).click()
        sleep(1)
        driver.find_element(By.XPATH, Locator.dutch).click()
        dutch_flag_check = driver.find_element(By.XPATH, Locator.flag)
        print(dutch_flag_check.get_attribute("src"))

        # Test French switch
        driver.find_element(By.XPATH, Locator.change_language).click()
        sleep(1)
        driver.find_element(By.XPATH, Locator.french).click()
        french_flag_check = driver.find_element(By.XPATH, Locator.flag)
        print(french_flag_check.get_attribute("src"))

        # Test German switch
        driver.find_element(By.XPATH, Locator.change_language).click()
        sleep(1)
        driver.find_element(By.XPATH, Locator.german).click()
        german_flag_check = driver.find_element(By.XPATH, Locator.flag)
        print(german_flag_check.get_attribute("src"))

        # Test Hungarian switch
        driver.find_element(By.XPATH, Locator.change_language).click()
        sleep(1)
        driver.find_element(By.XPATH, Locator.hungarian).click()
        hungarian_flag_check = driver.find_element(By.XPATH, Locator.flag)
        print(hungarian_flag_check.get_attribute("src"))

        # Test Italian switch
        driver.find_element(By.XPATH, Locator.change_language).click()
        sleep(1)
        driver.find_element(By.XPATH, Locator.italian).click()
        italian_flag_check = driver.find_element(By.XPATH, Locator.flag)
        print(italian_flag_check.get_attribute("src"))

        # Test Polish switch
        driver.find_element(By.XPATH, Locator.change_language).click()
        sleep(1)
        driver.find_element(By.XPATH, Locator.polish).click()
        polish_next_button = driver.find_element(By.XPATH, Locator.polish_next_button)
        polish_flag_check = driver.find_element(By.XPATH, Locator.flag)
        print(polish_flag_check.get_attribute("src"))

        # Test Slovak switch
        driver.find_element(By.XPATH, Locator.change_language).click()
        sleep(1)
        driver.find_element(By.XPATH, Locator.slovak).click()
        slovak_flag_check = driver.find_element(By.XPATH, Locator.flag)
        print(slovak_flag_check.get_attribute("src"))

        # Test Spanish switch
        driver.find_element(By.XPATH, Locator.change_language).click()
        sleep(1)
        driver.find_element(By.XPATH, Locator.spanish).click()
        spanish_flag_check = driver.find_element(By.XPATH, Locator.flag)
        print(spanish_flag_check.get_attribute("src"))

        # Test Swedish switch
        driver.find_element(By.XPATH, Locator.change_language).click()
        sleep(1)
        driver.find_element(By.XPATH, Locator.swedish).click()
        swedish_flag_check = driver.find_element(By.XPATH, Locator.flag)
        print(swedish_flag_check.get_attribute("src"))

        # Test Turkish switch
        driver.find_element(By.XPATH, Locator.change_language).click()
        sleep(1)
        driver.find_element(By.XPATH, Locator.turkish).click()
        turkish_flag_check = driver.find_element(By.XPATH, Locator.flag)
        print(turkish_flag_check.get_attribute("src"))

        # Test Arabic switch
        driver.find_element(By.XPATH, Locator.change_language).click()
        sleep(1)
        driver.find_element(By.XPATH, Locator.arabic).click()
        arabic_flag_check = driver.find_element(By.XPATH, Locator.flag)
        print(arabic_flag_check.get_attribute("src"))

        # Test English switch
        driver.find_element(By.XPATH, Locator.change_language).click()
        sleep(1)
        driver.find_element(By.XPATH, Locator.english_uk).click()
        uk_flag_check = driver.find_element(By.XPATH, Locator.flag)
        print(uk_flag_check.get_attribute("src"))
