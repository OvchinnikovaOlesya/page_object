from .base_page import BasePage
from .locators import AddItemCardLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        empty_basket = self.browser.find_element(*AddItemCardLocators.empty_basket)
        assert self.is_element_present(*AddItemCardLocators.empty_basket), 'Сart is not empty'
