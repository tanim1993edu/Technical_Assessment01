import pytest
import json
from playwright.sync_api import Page

def load_test_data():
    with open("d:/CV/Latest CV/Audacity/Assessment3/data/test_data.json", "r") as file:
        return json.load(file)

def test_success_checkout_flow(page: Page):
    data = load_test_data()

    email = data["ecommerce_credentials"]["email"]
    password = data["ecommerce_credentials"]["password"]
    checkout_data = data["checkout_data"]
    
    # Log in to eCommerce site
    page.goto('https://practice.qabrains.com/ecommerce', wait_until="networkidle")
    page.fill('#email', email)
    page.fill('#password', password)
    page.click('button.btn-submit')
    page.wait_for_timeout(5000)
    print("Login successful.")

    # Add items to the cart
    add_to_cart_buttons = page.locator('button:has-text("Add to cart")')
    add_to_cart_buttons.nth(0).click()
    add_to_cart_buttons.nth(1).click()
    print("Items added to cart.")

    # Go to the cart
    page.goto('https://practice.qabrains.com/ecommerce/cart', wait_until="networkidle")
    
    # Proceed to checkout
    checkout_button = page.locator('button:has-text("Checkout")')
    checkout_button.click()
    page.goto('https://practice.qabrains.com/ecommerce/checkout-info', wait_until="networkidle")
    print("Navigated to checkout info page.")

    # Fill in checkout info
    page.fill('input[placeholder="Ex. John"]', checkout_data["first_name"])
    page.fill('input[placeholder="Ex. Doe"]', checkout_data["last_name"])
    page.fill('input[value="1207"]', checkout_data["zip_code"])
    
    # Continue to next page
    continue_button = page.locator('button', has_text="Continue")
    continue_button.click()
    
    # Complete the checkout
    page.goto('https://practice.qabrains.com/ecommerce/checkout-overview', wait_until="networkidle")
    finish_button = page.locator('button', has_text="Finish")
    finish_button.click()
    print("Checkout complete. Thank you for your order!")
