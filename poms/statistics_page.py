from selenium.webdriver.chrome.webdriver import WebDriver

# A class that will contain the important elements on a web page
from selenium.webdriver.remote.webelement import WebElement

class StatisticsPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def view_reports_btn(self):
        element: WebElement = self.driver.find_element_by_id("viewReportsPage")
        return element

    def create_reports_btn(self):
        element: WebElement = self.driver.find_element_by_id("createReportsPage")
        return element

    def logout_btn(self):
        element: WebElement = self.driver.find_element_by_id("logout")
        return element

