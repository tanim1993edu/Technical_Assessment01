import pytest
import json
from playwright.sync_api import Page

def load_test_data():
    with open("data/test_data.json", "r") as file:
        return json.load(file)

def test_user_registration(page: Page):
    data = load_test_data()

    # Accessing registration data from JSON
    name = data["registration"]["name"]
    country = data["registration"]["country"]
    account_type = data["registration"]["account_type"]
    email = data["registration"]["email"]
    password = data["registration"]["password"]
    confirm_password = data["registration"]["confirm_password"]

    page.goto("https://practice.qabrains.com/registration", wait_until="networkidle")
    print("Navigated to the registration page.")
    
    # Fill Name
    page.wait_for_selector('#name')
    page.fill('#name', name)

    # Select Country
    page.wait_for_selector('#country')
    page.select_option('#country', country)

    # Select Account Type
    page.wait_for_selector('#account', state='visible')
    
    # Evaluate the dropdown options
    options = page.eval_on_selector_all('#account option', '''options => {
        return options.map(option => ({
            value: option.value,
            text: option.textContent
        }));
    }''')
    print(f"Available options: {options}")
    
    # Select by matching the account_type with option text
    found = False
    for option in options:
        if option['text'].lower() == account_type.lower():
            page.select_option('#account', value=option['value'])
            found = True
            break
            
    if not found:
        raise Exception(f"Could not find account type '{account_type}' in available options: {options}")
    
    # Fill Email
    page.wait_for_selector('#email')
    page.fill('#email', email)

    # Fill Password
    page.wait_for_selector('#password')
    page.fill('#password', password)

    # Fill Confirm Password
    page.wait_for_selector('#confirm_password')
    page.fill('#confirm_password', confirm_password)

    # Click Signup button
    page.wait_for_selector('button.btn-submit')
    page.click('button.btn-submit')

    page.wait_for_timeout(5000)
    print("User registration completed successfully")
