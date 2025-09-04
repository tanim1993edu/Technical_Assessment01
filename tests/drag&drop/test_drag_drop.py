import pytest
from playwright.sync_api import Page

def test_drag_drop(page: Page):
    # Navigate to the drag-drop page
    page.goto('https://practice.qabrains.com/drag-drop', wait_until='networkidle')
    print('Navigated to the drag-drop page.')

    # Locate the draggable element
    drag_item = page.locator('div[draggable="true"]')

    # Locate the drop target
    drop_target = page.locator('div.max-w-96')  # max-w-96 is the correct Tailwind class for 24rem/384px width

    # Perform drag and drop action
    drag_item.drag_to(drop_target)

    # Verify the drop content
    drop_content = drop_target.text_content()
    assert "Drag Me" in drop_content, f"Expected 'Drag Me' but got {drop_content}"
    print("Drag and drop successful")
    
    # Wait for 5 seconds after successful drag and drop
    page.wait_for_timeout(5000)  # 5000 milliseconds = 5 seconds
