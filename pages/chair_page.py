from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ChairPage(BasePage):
    url ="https://home-club.com.ua/ua/sku-90507603?gclid=CjwKCAjwzY2bBhB6EiwAPpUpZhSieA2DRWXhLcbNCpIvJcC9dLHc534Djx5FKNpL9iXaLZlSQaNyLBoCEwYQAvD_BwE"

    vendor_code = "span[id='sku-148136']"

    check_list =[
        "Артикуль",
        "Наявність для поставки",
        "Прогноз наявності в Польщі",
        "Наявність у Львові"
    ]

    availability_for_delivery = "div[class='additional-details'] > div > a[href='/наличие-товаров'] ~ span"
    availability_forecast_in_Poland = "div[class='additional-details'] > div > a[href='/прогноз-наличия'] ~ span"
    availability_in_Lviv= "div[class='additional-details'] > div > a[href='/товары-в-наличии-3'] ~ span"

    def get_vendor_code(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.vendor_code).text

    def get_availability_for_delivery(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.availability_for_delivery).text
    
    def get_availability_forecast_in_Poland(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.availability_forecast_in_Poland).text
    
    def get_availability_in_Lviv(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.availability_in_Lviv).text
