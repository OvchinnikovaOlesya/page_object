from basket_page import BasketPage
from .pages.product_page import ProductPage
from .pages.main_page import MainPage



def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    browser.get(link)
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_login_and_registration_form(browser):
    new_link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
    page = MainPage(browser, new_link)
    page.open()
    login_page = page.go_to_login_page()
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = BasketPage(browser, link)
    page.open()
    page.go_to_cart()
    page.should_be_empty_basket()
    product_page = ProductPage(browser, browser.current_url)
    product_page.should_not_be_success_message()



