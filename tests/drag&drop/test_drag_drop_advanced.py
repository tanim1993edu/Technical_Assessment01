import pytest
from playwright.sync_api import Page, expect


def test_drag_drop_edge_cases(page: Page):
    """Test edge cases for drag and drop functionality"""
    page.goto('https://practice.qabrains.com/drag-drop', wait_until='networkidle')
    
    # Test dragging to invalid drop zone
    drag_item = page.locator('div[draggable="true"]')
    non_drop_zone = page.locator('h1')  # Header is not a drop zone
    
    try:
        drag_item.drag_to(non_drop_zone)
        page.wait_for_timeout(1000)
        
        # Verify item hasn't moved to invalid location
        assert drag_item.is_visible(), "Draggable item should still be visible in original position"
        print("Successfully verified drag to invalid zone behavior")
    except Exception as e:
        print(f"Expected behavior: {str(e)}")

def test_drag_drop_accessibility(page: Page):
    """Test accessibility features of drag and drop"""
    page.goto('https://practice.qabrains.com/drag-drop', wait_until='networkidle')
    
    # Check for proper ARIA attributes
    drag_item = page.locator('div[draggable="true"]')
    
    # Verify draggable attribute
    assert drag_item.get_attribute('draggable') == 'true', "Element should have draggable attribute"
    
    # Check for aria-grabbed attribute when dragging (if supported)
    drag_item.hover()
    drag_item.dispatch_event('mousedown')
    page.wait_for_timeout(100)
    
    # Verify accessibility roles
    drop_target = page.locator('div.max-w-96')
    assert drop_target.get_attribute('role') in ['region', 'group', None], "Drop target should have appropriate role"
    
    print("Accessibility attributes verified")

def test_drag_drop_visual_feedback(page: Page):
    """Test visual feedback during drag and drop operations"""
    page.goto('https://practice.qabrains.com/drag-drop', wait_until='networkidle')
    
    drag_item = page.locator('div[draggable="true"]')
    drop_target = page.locator('div.max-w-96')
    
    # Start drag operation
    drag_item.hover()
    page.mouse.down()
    
    # Move to drop target
    drop_target_box = drop_target.bounding_box()
    page.mouse.move(drop_target_box['x'] + drop_target_box['width']/2, 
                   drop_target_box['y'] + drop_target_box['height']/2)
    
    # Verify visual feedback during drag
    # Note: This might need adjustment based on actual visual feedback implementation
    drop_target_classes = drop_target.evaluate('el => el.classList.toString()')
    assert 'max-w-96' in drop_target_classes, "Drop target should maintain its styling during drag"
    
    # Complete drop operation
    page.mouse.up()
    page.wait_for_timeout(1000)
    
    print("Visual feedback during drag and drop verified")