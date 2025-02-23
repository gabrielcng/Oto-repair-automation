from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from automation_tests import config


class BasePage():
    def __init__(self, driver):
        self.driver = driver

    def _visit(self, url):
        if url.startswith("http"):
            self.driver.get(url)
        else:
            self.driver.get(config.baseurl + url)

    def _find(self, locator):
        return self.driver.find_element(locator["by"], locator["value"])

    def _is_displayed(self, locator):
        try:
            self._find(locator).is_displayed()
        except NoSuchElementException:
            return False
        return True

    def _wait_for_is_displayed(self, locator, timeout):
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(expected_conditions.visibility_of_element_located(
                (locator['by'], locator['value'])))
        except TimeoutException:
            return False
        return True