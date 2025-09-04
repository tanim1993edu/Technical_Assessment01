import pytest
import json
from playwright.sync_api import Page

def load_test_data():
    with open("data/test_data.json", "r") as file:
        return json.load(file)

def test_login_and_leave_feedback(page: Page):
    data = load_test_data()

    # Accessing login and feedback data from JSON
    email = data["feedback"]["email"]
    password = data["feedback"]["password"]
    comment = data["feedback"]["comment"]

    # Go to login page
    page.goto("https://qabrains.com/auth/login", wait_until="networkidle")
    print("Navigated to the login page.")
    
    # Fill the email field
    page.fill('input[name="email"]', email)
    
    # Fill the password field
    page.fill('input[name="password"]', password)

    page.wait_for_selector('button:has-text("Sign In")', state='visible')
    page.click('button:has-text("Sign In")')

    page.wait_for_timeout(2000)

    # Navigate to the main page
    page.goto("https://practice.qabrains.com/", wait_until="networkidle")
    
    # Wait for the textarea to appear and fill it
    page.wait_for_selector('textarea[placeholder="Write Comment..."]')
    page.fill('textarea[placeholder="Write Comment..."]', comment)

    button_selector = 'button[data-slot="dialog-trigger"]'
    page.wait_for_selector(button_selector, state='visible')

        # Wait for the button to be enabled and clickable
    page.wait_for_selector(button_selector + ':not([disabled])', state='visible')
    page.click(button_selector)    # Click the feedback button
