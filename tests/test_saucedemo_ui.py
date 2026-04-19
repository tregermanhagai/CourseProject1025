import re
from datetime import datetime
from pathlib import Path
from playwright.sync_api import Page, expect


def test_positive_login(page: Page) -> None:
    """Verify that the login page works correctly."""
    page.goto("")
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()
    img_dir = Path("img")
    file_name = f"positive_login_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    page.screenshot(path=str(img_dir / file_name), full_page=True)
    assert page.locator(".app_logo").text_content() == "Swag Labs"
    page.get_by_role("button", name="Open Menu").click()
    page.locator("[data-test=\"logout-sidebar-link\"]").click()
    print("\n ******* Successfully logged in ********* \n")


