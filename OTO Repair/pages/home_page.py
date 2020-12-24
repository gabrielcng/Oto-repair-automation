from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from automation_tests.config import baseurl


class HomePage(BasePage):
    _page_logo = {"by": By.CSS_SELECTOR, "value": "div.logo.vertical-align-cell"}


    def __init__(self, driver):
        self.driver = driver
        self._visit(baseurl)

    def logo_displayed(self):
        self._wait_for_is_displayed(self._page_logo, 10)
        return self._is_displayed(self._page_logo)


