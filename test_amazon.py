from selenium import webdriver
from page_object.BooksPage import BooksPage
from page_object.CartPage import CartPage
from page_object.ConfirmationPage import ConfirmationPage
from page_object.HomePage import HomePage
from page_object.ProductPage import ProductPage


def test__page__object():
    driver = webdriver.Chrome()
    driver.get("https://www.amazon.fr/")
    target_qty = "2"
    homePage = HomePage(driver)
    homePage.closeCookiesPopup()
    homePage.openAllMenu()
    homePage.openBookCategory()
    homePage.openAllBooks()
    booksPage = BooksPage(driver)
    booksPage.selectFirstBookNouveautes()
    productPage = ProductPage(driver)
    productPage.addToCart()
    confirmationPage = ConfirmationPage(driver)
    confirmationPage.openCart()
    cartPage = CartPage(driver)
    cartPage.changeQuantity("2")
    assert cartPage.getQuantity() == target_qty
    driver.quit()
