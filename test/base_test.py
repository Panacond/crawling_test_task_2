import unittest
from selenium import webdriver

from pages.chair_page import ChairPage

class BaseTest(unittest.TestCase):
    DEFAULT_TIMEOUT = 10

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.get(ChairPage.url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.close()