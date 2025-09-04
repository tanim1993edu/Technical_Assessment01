import pytest
import json
from playwright.sync_api import Page

def load_test_data():
    with open("data/test_data.json", "r") as file:
        return json.load(file)

def test_reset_password(page: Page):
    data = load_test_data()

    # Accessing forgot password data from JSON
    email = data["forgot_password"]["email"]

    page.goto("https://practice.qabrains.com/forgot-password", wait_until="networkidle")
    print("Navigated to the Forget Password page.")
    
    # Fill the email address for password reset
    page.wait_for_selector('#email')
    page.fill('#email', email)

    # Click the Reset Password button
    page.wait_for_selector('button.btn-submit')
    page.click('button.btn-submit')

    page.wait_for_timeout(5000)
    print("Password reset request was successful.")
