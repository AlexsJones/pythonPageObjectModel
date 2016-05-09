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
    
    def awaitpageload(self, time):
        WebDriverWait(self.driver, time).until(lambda x: x.execute_script("return document.readyState") == "complete")

    def get_element(self, element_tuple):
        waitexist(self.driver, element_tuple, 10)
        return self.driver.find_element(element_tuple[0], element_tuple[1])

    def get_elements(self, element_tuple):
        waitelementsexist(self.driver, element_tuple, 10)
        return self.driver.find_elements(element_tuple[0], element_tuple[1])
