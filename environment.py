# Environment is like a configuration for your cucumber tests
# Its an actual python code
from selenium import webdriver
from behave.runner import Context
from selenium.webdriver.chrome.webdriver import WebDriver

from poms.create_reports_page import CreateReportsPage
from poms.login_page import LoginPage

# the context object passed into our step implementations and environment set up and tear down functions
# is SHARED between every function
# context is a singleton meaning there is only ONE context obj for the entirety of the program
# @ context is the primary way to share info or objs in code
from poms.view_reports_page import ViewReportsPage


def before_all(context: Context):
    driver: WebDriver = webdriver.Chrome('C:\\Drivers\\chromedriver.exe')
    context.driver = driver
    context.login_page = LoginPage(context.driver)
    context.view_reports_page = ViewReportsPage(context.driver)
    context.create_reports_page = CreateReportsPage(context.driver)

    print("I run before ANY scenarios")


def after_all(context):
    print("I run after all scenarios")
    context.driver.quit()
