from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import AddItemCardLocators
import time


class ProductPage(BasePage):
    def test_should_adding_item_to_cart(self):
        self.browser.execute_script("window.scrollBy(0, 100);")
        add_to_card = self.browser.find_element(*AddItemCardLocators.add_item)
        add_to_card.click()

    def test_product_name_check(self):
        name_product_basket = self.browser.find_element(*AddItemCardLocators.name_product_basket).text
        name_product_message = self.browser.find_element(*AddItemCardLocators.name_product_message).text
        assert name_product_message == name_product_basket, 'the title of the book is different'

    def test_checking_the_cost_of_goods(self):
        price_message = self.browser.find_element(*AddItemCardLocators.price_message).text
        print(price_message)
        price_basket = self.browser.find_element(*AddItemCardLocators.price_basket).text
        print(price_basket)
        assert price_message == price_basket, 'the price of the book is different'
