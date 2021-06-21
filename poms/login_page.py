from selenium.webdriver.chrome.webdriver import WebDriver

# A class that will contain the important elements on a web page
from selenium.webdriver.remote.webelement import WebElement

class LoginPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def username(self):
        element: WebElement = self.driver.find_element_by_id("uname")
        return element

    def password(self):
        element: WebElement = self.driver.find_element_by_id("pass")
        return element

    def login_btn(self):
        element: WebElement = self.driver.find_element_by_id("loginBtn")
        return element

    def login_error(self):
        element: WebElement = self.driver.find_element_by_id("loginError")
        return element