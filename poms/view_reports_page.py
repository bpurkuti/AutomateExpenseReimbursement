from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver

# A class that will contain the important elements on a web page
from selenium.webdriver.remote.webelement import WebElement


class ViewReportsPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def create_reports_btn(self):
        element: WebElement = self.driver.find_element_by_id("createReportsPage")
        return element

    def statistics_btn(self):
        element: WebElement = self.driver.find_element_by_id("statisticsPageLink")
        return element

    def logout_btn(self):
        element: WebElement = self.driver.find_element_by_id("logout")
        return element

    def resolve_btn(self):
        for i in range(20):
            try:
                element: WebElement = self.driver.find_element_by_id(f"resolveBtn{i}")
                return element
            except NoSuchElementException:
                print(f"No such button found")

    def checkmark_approve(self):
        element: WebElement = self.driver.find_element_by_id("cApproved")
        return element

    def checkmark_deny(self):
        element: WebElement = self.driver.find_element_by_id("cDenied")
        return element

    def resolve_comment_box(self):
        element: WebElement = self.driver.find_element_by_id("rComment")
        return element

    def resolve_update_btn(self):
        element: WebElement = self.driver.find_element_by_id("rUpdateBtn")
        return element

    def close_resolve_form(self):
        element: WebElement = self.driver.find_element_by_id("closeForm")
        return element

    def check_manager(self):
        return self.driver.execute_script("return localStorage.getItem('isManager')")
