from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BaseDriver():
    def __init__(self, driver):
        self.driver = driver

    def wait_for_presence_of_all_elements(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 20)
        list_of_elements = wait.until(EC.presence_of_all_elements_located((locator_type, locator)))
        return list_of_elements
    def wait_until_element_is_clickable(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(EC.element_to_be_clickable((locator_type, locator)))
        return element
    def wait_until_element_is_selected(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 20)
        element_2 = wait.until(EC.element_located_to_be_selected((locator_type, locator)))
        # element_2 = wait.until(EC.((locator_type, locator)))
        return element_2

