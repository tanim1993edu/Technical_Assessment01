import pytest
import json
from playwright.sync_api import Page

def load_test_data():
    with open("data/test_data.json", "r") as file:
        return json.load(file)

def test_form_submission(page: Page):
    data = load_test_data()

    # Accessing data from JSON
    name = data["valid_form_submission"]["name"]
    email = data["valid_form_submission"]["email"]
    contact = data["valid_form_submission"]["contact"]
    date = data["valid_form_submission"]["date"]
    file_path = data["valid_form_submission"]["file_path"]
    expected_file_name = data["valid_form_submission"]["expected_file_name"]
    colors = data["valid_form_submission"]["colors"]
    menu = data["valid_form_submission"]["menu"]
    country = data["valid_form_submission"]["country"]

    page.goto("https://practice.qabrains.com/form-submission", wait_until="networkidle")
    print("Navigated to the Form Submission page.")

    # Fill the name input
    page.wait_for_selector('#name')
    page.fill('#name', name)

    # Fill the email input
    page.wait_for_selector('#email')
    page.fill('#email', email)

    # Fill the contact input
    page.wait_for_selector('#contact')
    page.fill('#contact', contact)

    # Set the date (format: YYYY-MM-DD)
    page.wait_for_selector('#date')
    page.fill('#date', date)

    # Upload File
    page.wait_for_selector('#file')
    page.set_input_files('#file', file_path)
    
    # Verify file input is not empty
    file_input = page.locator('#file')
    assert file_input.evaluate('el => el.files.length') > 0, "No file was uploaded"

    # Select color (Radio)
    for color in colors:
        page.wait_for_selector(f'input[type="radio"][name="color"][value="{color}"]')
        page.check(f'input[type="radio"][name="color"][value="{color}"]')

    # Select menu items (Checkboxes)
    for item in menu:
        page.wait_for_selector(f'input[type="checkbox"][name="food"][value="{item}"]')
        page.check(f'input[type="checkbox"][name="food"][value="{item}"]')

    # Select Country
    page.wait_for_selector('#country')
    page.select_option('#country', country)

    # Submit the form
    page.wait_for_selector('button.btn-submit')
    page.click('button.btn-submit')
    page.wait_for_timeout(5000)
    print("Form submitted successfully.")
