import time

from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from poms.login_page import LoginPage


@given(u'Employee is on the login page')
def on_login_page(context):
    context.driver.get("file:///C:/Users/Bishwo%20Purkuti/PycharmProjects/ExpenseReimbursement/front_end/login.html")


@when(u'Employee enters their {username} into the username field')
def input_username(context, username: str):
    context.login_page.username().send_keys(username)


@when(u'Employee enters their {password} into the password field')
def input_password(context, password: str):
    context.login_page.password().send_keys(password)


@when(u'Employee clicks on login button')
def submit_login_btn(context):
    context.login_page.login_btn().click()


@then(u'Employee is on the View Reports Page')
def on_view_reports_page(context):
    driver: WebDriver = context.driver
    time.sleep(2)
    title = driver.title
    assert title == 'Reports'


@then(u'Employee\'s manager status is {status}')
def check_manager(context, status: bool):
    # name_input: WebElement = WebDriverWait(context.driver,5).until(EC.presence_of_element_located((By.ID,"nameInput")))
    driver: WebDriver = context.driver
    result = driver.execute_script("return localStorage.getItem('isManager')")
    print(result)
    assert result == status
