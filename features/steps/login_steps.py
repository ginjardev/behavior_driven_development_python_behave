"""
Selenium steps to configure behave test scenarios
"""
from behave import *
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_for_element(context, by, value, timeout=10):
    return WebDriverWait(context.browser, timeout).until(
        EC.presence_of_element_located((by, value))
    )

@given('the LambdaTest e-commerce login page is open "{url}"')
def step_open_ecommerce_login_page(context, url):
    context.browser.get(url)

@when('check if page title is "{title}"')
def step_check_page_title(context, title):
    assert context.browser.title == title

@when('I enter valid email and password')
def step_enter_email_password(context):
    context.browser.find_element(By.ID, 'input-email').send_keys('kentb@gmail.com')
    context.browser.find_element(By.ID, 'input-password').send_keys('password')

@when('I click the Login button')
def step_click_login_button(context):
    login_button = wait_for_element(context, By.XPATH, "//input[@type='submit' and @value='Login']")
    login_button.click()

@then('I should be redirected to the dashboard')
def step_redirect_to_dashboard(context):
    assert context.browser.title == "My Account", "Redirection to dashboard failed"