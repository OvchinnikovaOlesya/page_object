from .pages.product_page import ProductPage
from .pages.base_page import BasePage
import time


def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    page.test_should_adding_item_to_cart()
    page.solve_quiz_and_get_code()
    page.test_product_name_check()
    page.test_checking_the_cost_of_goods()





