from selenium import webdriver
from selenium.webdriver.common.by import By


class ConfirmationPage:
    click_cart = "#nav-cart-count"

    def __init__(self, driver: webdriver):
        self.driver = driver

    def openCart(self):
        self.driver.find_element(By.CSS_SELECTOR, self.click_cart).click()
