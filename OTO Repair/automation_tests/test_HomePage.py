import pytest
from pages import home_page
from pages.home_page import HomePage
import time
from sys import version_info

class TestHomePage():

    @pytest.fixture
    def home_page(self, driver):
        return home_page.HomePage(driver)

    def test_homepage_components_are_displayed(self, home_page):
        assert home_page.logo_displayed()

        def quit():
            driver_.quit()