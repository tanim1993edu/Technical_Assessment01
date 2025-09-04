import pytest
import json
from playwright.sync_api import Page

def load_test_data():
    with open("d:/CV/Latest CV/Audacity/Assessment3/data/test_data.json", "r") as file:
        return json.load(file)

def test_invalid_login(page: Page):
    data = load_test_data()

    # Accessing data from JSON file
    email = data["invalid_login"]["email"]
    password = data["invalid_login"]["password"]
    expected_text = data["invalid_login"]["expected_text"]

    page.goto("https://practice.qabrains.com/", wait_until="networkidle")
    print("Navigated to the login page.")
    
    # Fill the email input
    page.wait_for_selector('#email')
    page.fill('#email', email)

    # Fill the password input
    page.wait_for_selector('#password')
    page.fill('#password', password)

    # Click the Login button
    page.wait_for_selector('button.btn-submit')
    page.click('button.btn-submit')

    page.wait_for_timeout(5000)
    print("Your email is invalid!")

    # Verify the error message
    actual_text = page.locator('div.toaster span.title').text_content()
    assert actual_text == expected_text
