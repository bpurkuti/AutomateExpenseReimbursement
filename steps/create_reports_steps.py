from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from poms.view_reports_page import ViewReportsPage
from poms.create_reports_page import CreateReportsPage


@when(u'Employee clicks on Create Reports button')
def create_report_btn(context):
    context.view_reports_page.create_reports_btn().click()


@then(u'Employee is on the Create Reports Page')
def on_create_reports_page(context):
    driver: WebDriver = context.driver
    title = driver.title
    assert title == 'Create Reports'


@when(u'Employee enters their {amount} into the amount field')
def input_amount(context, amount: int):
    context.create_reports_page.amount_input().send_keys(amount)


@when(u'Employee enters their {reason} into the description field')
def input_reason(context, reason: str):
    context.create_reports_page.reason_input().send_keys(reason)


@when(u'Employee clicks on the submit button')
def click_submit_btn(context):
    context.create_reports_page.create_reimbursement_btn().click()


@when(u'Employee clicks on the logout button')
def click_logout_btn(context):
    context.create_reports_page.logout_btn().click()


@then(u'Employee is on the login page')
def on_login_page(context):
    driver: WebDriver = context.driver
    title = driver.title
    assert title == 'Login page'

