__author__ = 'Chidozie Amefule'

from selenium import webdriver


class SS(object):

    def __init__(self, driver):
        self.driver = driver

    def screenshot(self, path):
        directory = "User/admin/Documents/Screenshots"
        self.driver.get_screenshot_as_file(directory + path)

