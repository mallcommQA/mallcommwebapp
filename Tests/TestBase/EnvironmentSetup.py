__author__ = 'Chidozie Amefule'

import datetime
import unittest
from selenium import webdriver
from Drivers.drivers import driver_service


class EnvironmentSetup(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=driver_service)
        self.driver.set_window_size(1240, 1080)
        self.driver.get("https://staging2-app.mallcommapp.co.uk")
        print('Run started at : ' + str(datetime.datetime.now()))
        print('Test Environment Set Up')
        print('-----------------------')
        self.driver.implicitly_wait(20)

    def tearDown(self):
        print('---------------------')
        print('Test Environment Destroyed')
        print('Run Completed at: ' + str(datetime.datetime.now()))
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()

