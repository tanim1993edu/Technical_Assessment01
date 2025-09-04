import pytest
from playwright.sync_api import Page
import json

def load_test_data():
    with open("data/test_data.json", "r") as file:
        return json.load(file)

def test_invalid_email_format(page: Page):
    """Test form validation with invalid email format"""
    data = load_test_data()
    
    page.goto("https://practice.qabrains.com/form-submission", wait_until="networkidle")
    
    # Fill with invalid email format
    page.fill('#name', "John Doe")
    page.fill('#email', "invalid-email-format")  # Invalid email
    page.fill('#contact', "1234567890")
    
    # Submit form
    page.click('button.btn-submit')
    
    # Verify error message for invalid email
    error_message = page.locator('.text-red-500.text-sm.mt-1').filter(has_text="Please enter a valid email")
    assert error_message.is_visible(), "Email validation error message not shown"

def test_invalid_phone_format(page: Page):
    """Test form validation with invalid phone format"""
    page.goto("https://practice.qabrains.com/form-submission", wait_until="networkidle")
    
    # Fill with invalid phone format
    page.fill('#name', "John Doe")
    page.fill('#email', "valid@email.com")
    page.fill('#contact', "abc123")  # Invalid phone number
    
    # Submit form
    page.click('button.btn-submit')
    
    # Verify error message for invalid phone
    error_message = page.locator('.text-red-500.text-sm.mt-1').filter(has_text="Please enter a valid contact number")
    assert error_message.is_visible(), "Phone validation error message not shown"

def test_form_accessibility(page: Page):
    """Test form fields accessibility and labels"""
    page.goto("https://practice.qabrains.com/form-submission", wait_until="networkidle")
    
    # Test required field labels are present and visible
    required_fields = {
        'name': 'Name',
        'email': 'Email',
        'contact': 'Contact Number',
        'file': 'Upload File',
        'country': 'Select Country'
    }
    
    for field_id, expected_label in required_fields.items():
        # Check if field exists and is enabled
        field = page.locator(f'#{field_id}')
        assert field.is_enabled(), f"Field {field_id} is not enabled"
        
        # Check if field is focusable
        field.focus()
        assert page.evaluate('document.activeElement.id') == field_id, f"Field {field_id} cannot be focused"
        
        # Get parent form-group and check label
        form_group = field.locator('xpath=ancestor::div[contains(@class, "form-group")]')
        label = form_group.locator('xpath=./*[contains(@class, "form-label") or self::label]').first
        assert label.is_visible(), f"Label for {field_id} is not visible"
        assert expected_label in label.text_content(), f"Label for {field_id} does not contain expected text"

def test_keyboard_navigation(page: Page):
    """Test keyboard navigation through form fields"""
    page.goto("https://practice.qabrains.com/form-submission", wait_until="networkidle")
    
    # List of focusable elements in expected tab order
    focusable_elements = ['name', 'email', 'contact', 'date', 'file', 'Red', 'Green', 'Blue', 
                         'Yellow', 'Pasta', 'Pizza', 'Burger', 'Sandwich', 'country']
    
    # Focus first field
    page.press('body', 'Tab')
    
    # Check tab navigation
    for element_id in focusable_elements:
        active_element = page.evaluate('document.activeElement.id')
        assert active_element == element_id, f"Expected focus on {element_id}, but got {active_element}"
        page.press('body', 'Tab')

def test_form_field_restrictions(page: Page):
    """Test form field input restrictions"""
    page.goto("https://practice.qabrains.com/form-submission", wait_until="networkidle")
    
    # Test email field type
    email_type = page.evaluate('document.getElementById("email").type')
    assert email_type == "email", "Email field should be of type 'email'"
    
    # Test file upload restrictions
    file_accept = page.evaluate('document.getElementById("file").accept')
    assert file_accept, "File input should have accepted file types specified"
    
    # Test country dropdown is not free text
    country_element = page.locator('#country')
    assert country_element.evaluate('el => el.tagName.toLowerCase()') == 'select', \
           "Country field should be a select dropdown"