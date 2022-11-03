from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def implicitly_wait(self, seconds):
        self.driver.implicitly_wait(seconds)

    def wait_visibility_of_element(self, second, xpath):
        wait = WebDriverWait(self.driver, second)
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, xpath)))