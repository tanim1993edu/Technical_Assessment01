import pytest
import json
from playwright.sync_api import Page

def load_test_data():
    with open("d:/CV/Latest CV/Audacity/Assessment3/data/test_data.json", "r") as file:
        return json.load(file)

def test_add_favorites(page: Page):
    data = load_test_data()
    
    # Use valid login credentials from test data
    email = data["ecommerce_credentials"]["email"]
    password = data["ecommerce_credentials"]["password"]
    ecommerce_url = data["ecommerce_credentials"]["ecommerce_url"]
    
    # Go to the eCommerce login page
    page.goto(ecommerce_url, wait_until="networkidle")
    print("Navigated to the Ecommerce-site login page.")

    # Log in
    page.fill('#email', email)
    page.fill('#password', password)
    page.click('button.btn-submit')
    page.wait_for_timeout(5000)
    print("Login successful.")

    # Navigate to the products page
    page.goto('https://practice.qabrains.com/ecommerce', wait_until="networkidle")
    print("Navigated to the Ecommerce-site page.")
    
    # Add products to favorites
    fav_buttons = page.locator('div.products div.group span[role="button"] button')
    fav_buttons.nth(0).click()  # Add first product to favorites
    fav_buttons.nth(1).click()  # Add second product to favorites
    print("Added to favorites.")
