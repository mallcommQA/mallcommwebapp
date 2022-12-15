__author__ = 'Chidozie Amefule'

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from Tests.TestBase.EnvironmentSetup import EnvironmentSetup
from Tests.PageObject.Pages.Locators import Locator
from time import sleep


class TestURLLaunch(EnvironmentSetup):

    # Check that url is loaded successfully
    def test_url_display(self):
        driver = self.driver
        sleep(3)
        # Take screenshot of loaded page
        driver.get_screenshot_as_file("ScreenShots/launch_url.png")

        logo = driver.find_element(By.XPATH, Locator.logo).get_attribute("class")
        if logo == "app_logo":
            print("Web App logo is displayed - Web App URL is successfully launched.")
        else:
            print("Unsuccessful Web App launch.")


