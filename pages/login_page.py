from .base_page import BasePage
from .locators import LoginPageLocators, BasePageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, f'the login substring is not in the current link'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.login_form), 'Login form is not presented'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.registration_form), 'Registration form is not presented'

    def register_new_user(self, email, password):
        user_email = self.browser.find_element(*BasePageLocators.email_address)
        user_email.send_keys(email)
        user_password = self.browser.find_element(*BasePageLocators.password)
        user_password.send_keys(password)
        user_password2 = self.browser.find_element(*BasePageLocators.repeat_password)
        user_password2.send_keys(password)
        button_registration = self.browser.find_element(*BasePageLocators.button_registration)
        button_registration.click()

