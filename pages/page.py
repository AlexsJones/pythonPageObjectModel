#! /usr/bin/env python
#################################################################################
#     File Name           :     lib/page.py
#     Created By          :     anon
#     Creation Date       :     [2016-05-05 13:45]
#     Last Modified       :     [2016-05-05 14:25]
#     Description         :      
#################################################################################
from selenium.webdriver.common.by import By


class Page(object):

    def __init__(self, driver, url, identifiers):
        self.driver = driver
        self.url = url
        self.identifiers = identifiers
    
    def visit(self):
        self.driver.get(self.url)

    def verify(self):
        for key in self.identifiers:
            self.driver.find_element(*key)
