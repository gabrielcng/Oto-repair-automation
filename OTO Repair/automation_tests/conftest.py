import pytest
from selenium import webdriver
import config
import os


def pytest_addoption(parser):
    parser.addoption("--baseurl",
                     action="store",
                     default="https://oto.repair/",
                     help="base URL for the application under test")

    parser.addoption("--browser",
                     action="store",
                     default="chrome",
                     help="the name of the browser you want to test with")
@pytest.fixture
def driver(request):
    config.baseurl = request.config.getoption("--baseurl")
    config.browser = request.config.getoption("--browser").lower()

    if config.browser == "firefox":
        _geckodriver = os.path.join(os.getcwd(), 'vendor', 'geckodriver')
        driver_ = webdriver.Firefox(executable_path=_geckodriver)
    elif config.browser == "chrome":
        binary = r'C:\Users\gabrielc\Downloads\OTO Repair\/automation_tests\/vendor\chromedriver\/chromedriver.exe'
        driver_= webdriver.Chrome(binary)
        driver_.set_window_size(1920, 1080)

    def quit():
        driver_.quit()

    request.addfinalizer(quit)
    return driver_
