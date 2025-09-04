import pytest
import json
from playwright.sync_api import Page

def load_test_data():
    with open("d:/CV/Latest CV/Audacity/Assessment3/data/test_data.json", "r") as file:
        return json.load(file)

def test_add_cart_item(page: Page):
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
    
    # Add products to the cart
    add_to_cart_buttons = page.locator('button:has-text("Add to cart")')
    add_to_cart_buttons.nth(0).click()  # Add first product to cart
    add_to_cart_buttons.nth(1).click()  # Add second product to cart
    print("Added to cart.")

    # Go to the cart page
    page.goto("https://practice.qabrains.com/ecommerce/cart", wait_until="networkidle")
    print("Navigated to the Ecommerce-cart page.")
