from behave import given, when, then
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from poms.view_reports_page import ViewReportsPage


@when(u'Manager clicks on the resolve btn')
def click_first_resolve_btn(context):
    context.view_reports_page.resolve_btn().click()


@when(u'Manager selects the {status}')
def select_status(context, status: int):
    if status == 1:
        context.view_reports_page.checkmark_approve().click()
    else:
        context.view_reports_page.checkmark_deny().click()


@when(u'Manager enters their {comment} into the comment field')
def input_comment_field(context, comment: str):
    context.view_reports_page.resolve_comment_box().send_keys(comment)


@when(u'Manager clicks the submit button')
def click_resolve_submit(context):
    context.view_reports_page.resolve_update_btn().click()