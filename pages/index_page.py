from .locators import IndexPageLocators
from .base_page import BasePage


class IndexPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def load_page(self):
        self.driver.get(IndexPageLocators.URL)
        self.driver.maximize_window()

    def fill_login(self, creds):
        self.driver.find_element(*IndexPageLocators.LOGIN).send_keys(creds)

    def fill_passw(self, creds):
        self.driver.find_element(*IndexPageLocators.PASS).send_keys(creds)

    def press_enter(self):
        self.driver.find_element(*IndexPageLocators.ENTER_BUT).click()

    def login_user(self, user_login, user_pwd):
        self.fill_login(user_login)
        self.fill_passw(user_pwd)
        self.press_enter()
