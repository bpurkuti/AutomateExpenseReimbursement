from selenium.webdriver.chrome.webdriver import WebDriver

# A class that will contain the important elements on a web page
from selenium.webdriver.remote.webelement import WebElement

class CreateReportsPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def view_reports_btn(self):
        element: WebElement = self.driver.find_element_by_id("viewReportsPage")
        return element

    def statistics_btn(self):
        element: WebElement = self.driver.find_element_by_id("statisticsPageLink")
        return element

    def create_report_page_title(self):
        element: WebElement = self.driver.find_element_by_id("statisticsPageLink")
        return element

    def logout_btn(self):
        element: WebElement = self.driver.find_element_by_id("logout")
        return element

    def amount_input(self):
        element: WebElement = self.driver.find_element_by_id("cAmount")
        return element

    def reason_input(self):
        element: WebElement = self.driver.find_element_by_id("cReason")
        return element

    def create_reimbursement_btn(self):
        element: WebElement = self.driver.find_element_by_class_name("cbutton")
        return element
