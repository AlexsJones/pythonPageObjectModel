#! /usr/bin/env python
#################################################################################
#     File Name           :     lib/googlepage.py
#     Created By          :     anon
#     Creation Date       :     [2016-05-05 13:47]
#     Last Modified       :     [2016-05-05 14:12]
#     Description         :      
#################################################################################

import page
from selenium.webdriver.common.by import By
class GooglePage(page.Page):
    def __init__(self, driver):
        super(
                GooglePage, self).__init__(driver,
                "http://www.google.co.uk",
                [(By.ID,"hplogo")]
            )
