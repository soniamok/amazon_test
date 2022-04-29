from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class ProductPage:
    cart = "input#add-to-cart-button"

    def __init__(self, driver: webdriver):
        self.driver = driver

    def addToCart(self):
        wait = WebDriverWait(self.driver, 5)
        wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, self.cart))).click()

