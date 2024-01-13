from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(10)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how: object, what: object) -> object:
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True



