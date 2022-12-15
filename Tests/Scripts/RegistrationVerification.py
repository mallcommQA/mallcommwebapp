__author__ = 'Chidozie Amefule'

from selenium import webdriver
from selenium.webdriver.common.by import By
from Tests.TestBase.EnvironmentSetup import EnvironmentSetup
from Tests.PageObject.Pages.Locators import Locator
from Drivers.drivers import driver_service
import unittest
from time import sleep
import TestData


url = "https://www.google.com/gmail/about/"
driver = webdriver.Chrome(service=driver_service)

driver.get(url)

driver.find_element(By.XPATH, "//div[@class='header__aside']//a[text()='Sign in']").click()

driver.find_element(By.XPATH, "//div[@class='Xb9hP']//input[@name='identifier']").send_keys(TestData.gmail_email)
driver.find_element(By.XPATH, "//span[contains(text(),'Next')]").click()
sleep(3)
driver.find_element(By.XPATH, "//div[@id='password']//input").send_keys(TestData.gmail_password)

driver.find_element(By.XPATH, "//span[text()='Next']").click()
sleep(7)

driver.find_element(By.XPATH, "//div[@class='xS']//span[@id=':lc']").click()
sleep(3)
driver.find_element(By.XPATH, "//a[contains(text(),'click here to reset your password')]").click()
sleep(5)









