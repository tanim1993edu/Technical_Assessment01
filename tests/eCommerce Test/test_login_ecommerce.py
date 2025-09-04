import pytest
import json
from playwright.sync_api import Page

def load_test_data():
    with open("data/test_data.json", "r") as file:
        return json.load(file)

def test_login_ecommerce(page: Page):
    data = load_test_data()
    
    email = data["valid_login"]["email"]
    password = data["valid_login"]["password"]
    ecommerce_url = data["ecommerce_flow"]["ecommerce_site_url"]
    
    # Go to the eCommerce login page
    page.goto(ecommerce_url, wait_until="networkidle")
    print("Navigated to the Ecommerce-site login page.")

    # Log in
    page.fill('#email', email)
    page.fill('#password', password)
    page.click('button.btn-submit')
    page.wait_for_timeout(5000)
    print("Login successful.")
