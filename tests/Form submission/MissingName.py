import pytest
import json
from playwright.sync_api import Page

def load_test_data():
    with open("data/test_data.json", "r") as file:
        return json.load(file)

def test_form_submission(page: Page):
    data = load_test_data()

    # Accessing data from JSON
    email = data["form_submission_missing_name"]["email"]
    contact = data["form_submission_missing_name"]["contact"]
    date = data["form_submission_missing_name"]["date"]
    file_path = data["form_submission_missing_name"]["file_path"]
    expected_file_name = data["form_submission_missing_name"]["expected_file_name"]
    colors = data["form_submission_missing_name"]["colors"]
    menu = data["form_submission_missing_name"]["menu"]
    country = data["form_submission_missing_name"]["country"]

    page.goto("https://practice.qabrains.com/form-submission", wait_until="networkidle")
    print("Navigated to the Form Submission page.")

    # Skip filling the name input to simulate missing name
    page.wait_for_selector('#email')
    page.fill('#email', email)

    page.wait_for_selector('#contact')
    page.fill('#contact', contact)

    page.wait_for_selector('#date')
    page.fill('#date', date)

    # Upload File
    page.set_input_files('#file', file_path)

    # Verify uploaded file name
    uploaded_file_name = page.locator('#file').get_attribute('value')
    assert expected_file_name in uploaded_file_name, f"Expected file name '{expected_file_name}', but got '{uploaded_file_name}'"

    # Select colors (Checkboxes)
    for color in colors:
        page.wait_for_selector(f'input[type="checkbox"]#{color}')
        page.check(f'input[type="checkbox"]#{color}')

    # Select menu items (Checkboxes)
    for item in menu:
        page.wait_for_selector(f'input[type="checkbox"]#{item}')
        page.check(f'input[type="checkbox"]#{item}')

    # Select Country
    page.wait_for_selector('#country')
    page.select_option('#country', country)

    # Submit the form
    page.wait_for_selector('button.btn-submit')
    page.click('button.btn-submit')
    page.wait_for_timeout(5000)

    # We expect the name to be required and the form should not submit successfully
    error_message = page.locator('.error-message').text_content()
    assert "Name is a required field" in error_message
    print("Form submission failed due to missing name.")
