#! /usr/bin/env python
#################################################################################
#     File Name           :     test.py
#     Created By          :     anon
#     Creation Date       :     [2016-05-05 13:34]
#     Last Modified       :     [2016-05-05 14:23]
#     Description         :      
#################################################################################

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pages import googlepage

class PythonSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search(self):
        driver = self.driver
        #Arrange
        google = googlepage.GooglePage(driver)
        #Act
        google.visit()
        #Assert
        google.verify()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

