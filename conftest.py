import pytest
from playwright.sync_api import sync_playwright

# Fixture to launch the browser instance
@pytest.fixture(scope="session")
def browser():
    """Fixture to launch a browser instance for the entire test session."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # Running in headless mode
        yield browser
        browser.close()

# Fixture for creating a new page for each test
@pytest.fixture(scope="function")
def page(browser):
    """Fixture to create a new browser context and page for each test."""
    context = browser.new_context()  # Create a new browser context
    page = context.new_page()  # Open a new page
    yield page  # Provide the page to the test
    page.close()  # Close the page after the test is done
    context.close()  # Close the browser context after the test is done
