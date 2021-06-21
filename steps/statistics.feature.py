import time

from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@when(u'Employee clicks on the statistics button')
def click_on_statistics_btn(context):
    context.view_reports_page.statistics_btn().click()

@then(u'Employee is on statistics page')
def on_statistics_page(context):
    driver: WebDriver = context.driver
    time.sleep(1)
    title = driver.title
    assert title == 'Statistics'