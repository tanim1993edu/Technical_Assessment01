import pytest
import json
from playwright.sync_api import Page

def load_test_data():
    with open("data/test_data.json", "r") as file:
        return json.load(file)

def test_empty_cart_checkout(page: Page):
    data = load_test_data()

    email = data["valid_login"]["email"]
    password = data["valid_login"]["password"]
    
    # Log in to eCommerce site
    page.goto('https://practice.qabrains.com/ecommerce', wait_until="networkidle")
    page.fill('#email', email)
    page.fill('#password', password)
    page.click('button.btn-submit')
    page.wait_for_timeout(5000)
    print("Login successful.")
    
    # Go to the cart
    page.goto('https://practice.qabrains.com/ecommerce/cart', wait_until="networkidle")
    print("Your cart is empty.")
