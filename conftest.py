import pytest
from selenium import webdriver
from pages.index_page import IndexPage

@pytest.fixture(scope="module")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=800,600")
    webd = webdriver.Remote(
        command_executor = 'http://localhost:4444/wd/hub',
        options=options
    )
    webd.implicitly_wait(10)
    yield webd
    webd.quit()


@pytest.fixture(scope="module")
def main_page(driver):
    main_page = IndexPage(driver)
    main_page.load_page()
    main_page.login_user("Login", "PASSWORD")
    yield main_page

