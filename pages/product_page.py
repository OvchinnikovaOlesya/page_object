from .base_page import BasePage
from .locators import AddItemCardLocators


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
        price_basket = self.browser.find_element(*AddItemCardLocators.price_basket).text
        assert price_message == price_basket, 'the price of the book is different'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*AddItemCardLocators.not_element_message), 'Success message is presented, but should not be'

    def test_is_dissapeared(self):
        assert self.is_disappeared(*AddItemCardLocators.not_element_message), 'Success message is disappeared, but should not be'

