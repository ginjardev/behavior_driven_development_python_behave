from multiprocessing import context
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def wait_for_element(context, by, value, timeout=10):
    return WebDriverWait(context.browser, timeout).until(
        EC.presence_of_element_located((by, value))
)

def wait_for_clickable_element(context, by, value, timeout=10):
    return WebDriverWait(context.browser, timeout).until(
        EC.element_to_be_clickable((by, value))
    )


@given('the user is on the product page link "{url}"')
def step_open_product_page(context, url):
    context.browser.get(url)

@when('the user clicks the "Buy Now" button')
def step_click_buy_now(context):
    product = wait_for_element(context, By.CSS_SELECTOR, "div#entry_216843 button.button-buynow")
    product.click()


@when('the user fills in billing and payment details')
def step_fill_checkout_form(context):
    # fill in the billing and payment details
    context.browser.find_element(By.ID, 'input-payment-firstname').send_keys('Giga')
    context.browser.find_element(By.ID, 'input-payment-lastname').send_keys('Doe')
    context.browser.find_element(By.ID, 'input-payment-email').send_keys('gigadoe@gmail.com')
    context.browser.find_element(By.ID, 'input-payment-telephone').send_keys('98765432')
    context.browser.find_element(By.ID, 'input-payment-password').send_keys('password')
    context.browser.find_element(By.ID, 'input-payment-confirm').send_keys('password')
    context.browser.find_element(By.ID, 'input-payment-address-1').send_keys('password')
    context.browser.find_element(By.ID, 'input-payment-city').send_keys('Preston')
    context.browser.find_element(By.ID, 'input-payment-postcode').send_keys('4567')
    
    # select the privacy policy checkbox
    context.browser.find_element(By.CSS_SELECTOR, "label[for='input-account-agree']").click() #second

    #scroll and select the terms and conditions checkbox
    checkbox = wait_for_element(context, By.ID, "input-agree")
    context.browser.execute_script("arguments[0].scrollIntoView(true);", checkbox)
    context.browser.execute_script("arguments[0].click();", checkbox)

    # click the "Continue" button to the confirm the order
    context.browser.find_element(By.ID, "button-save").click()


@when('the user confirms the order')
def step_confirm_order(context):
    # click the "Confirm Order" button
    confirm_button = wait_for_clickable_element(context, By.ID, "button-confirm")
    context.browser.execute_script("arguments[0].scrollIntoView(true);", confirm_button)
    context.browser.execute_script("arguments[0].click();", confirm_button)

@then('the order should be successfully placed')
def step_redirect_to_dashboard(context):
    # wait for the order confirmation page to load
    title = context.browser.title
    print(f"Page title: {title}")
    assert "Your order has been placed!" in title, "Your order placement failed"