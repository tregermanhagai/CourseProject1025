import re
from playwright.sync_api import Page, expect


def test_positive_login(page: Page) -> None:
    """Verify that the login page works correctly."""
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()
    assert page.locator(".app_logo").text_content() == "Swag Labs"
    page.get_by_role("button", name="Open Menu").click()
    page.locator("[data-test=\"logout-sidebar-link\"]").click()
    print("\n ******* Successfully logged in ********* \n")