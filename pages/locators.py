from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link')
    email_address = (By.CSS_SELECTOR, '#id_registration-email')
    password = (By.CSS_SELECTOR, '#id_registration-password1')
    repeat_password = (By.CSS_SELECTOR, '#id_registration-password2')
    button_registration = (By.CSS_SELECTOR, '[value="Register"]')
    USER_UCON = (By.CLASS_NAME, 'icon-user')


class LoginPageLocators:
    login_form = (By.ID, 'login_form')
    registration_form = (By.ID, 'register_form')


class AddItemCardLocators:
    add_item = (By.CLASS_NAME, 'btn.btn-lg.btn-primary.btn-add-to-basket')
    name_product_message = (By.CSS_SELECTOR, '.col-sm-6 h1')
    name_product_basket = (By.CSS_SELECTOR, '.alert.alert-success strong')
    price_message = (By.CSS_SELECTOR, '.col-sm-6 .price_color')
    price_basket = (By.CSS_SELECTOR, '.alert.alert-info strong')
    not_element_message = (By.CSS_SELECTOR, '#messages > :nth-child(1)')
    empty_basket = (By.CSS_SELECTOR, '#content_inner :nth-child(1)')
    go_to_basket = (By.CSS_SELECTOR, '.btn-group a')

