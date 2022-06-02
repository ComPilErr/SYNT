from selenium.webdriver.common.by import By


class IndexPageLocators:
    URL = "https://dev-dash.syngentaaws.org/lg/lead_generation"
    LOGIN = (By.ID, "user-name-input")
    PASS = (By.ID, "user-pwd-input")
    ENTER_BUT = (By.ID, "submit-indication")

