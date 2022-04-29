from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class HomePage:
    cookies_accept = "input#sp-cc-accept"
    hamburger_menu_selector = "#nav-hamburger-menu"
    side_menu_selector = "#hmenu-canvas"
    livres_menu_selector = "a[data-menu-id='10']"
    tous_les_livres = "ul.hmenu-visible li:nth-of-type(3)"

    def __init__(self, driver: webdriver):
        self.driver = driver

    def closeCookiesPopup(self):
        wait = WebDriverWait(self.driver, 3)
        wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, self.cookies_accept)))
        self.driver.find_element(By.CSS_SELECTOR, self.cookies_accept).click()

    def openAllMenu(self):
        self.driver.find_element(By.CSS_SELECTOR, self.hamburger_menu_selector).click()
        wait = WebDriverWait(self.driver, 3)
        wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, self.side_menu_selector)))

    def openBookCategory(self):
        self.driver.find_element(By.CSS_SELECTOR, self.livres_menu_selector).click()
        wait = WebDriverWait(self.driver, 3)
        wait.until(expected_conditions.invisibility_of_element_located((By.CSS_SELECTOR, self.livres_menu_selector)))
        wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, self.tous_les_livres)))

    def openAllBooks(self):
        self.driver.find_element(By.CSS_SELECTOR, self.tous_les_livres).click()
