from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class CartPage:
    quantity_selctor = "select[name='quantity']"

    def __init__(self, driver: webdriver):
        self.driver = driver

    def changeQuantity(self, quantity):
        select_qty = Select(self.driver.find_element(By.CSS_SELECTOR, self.quantity_selctor))
        select_qty.select_by_value(quantity)

    def getQuantity(self):
        return Select(self.driver.find_element(By.CSS_SELECTOR, self.quantity_selctor)).first_selected_option.text
