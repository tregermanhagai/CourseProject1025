import re
from datetime import datetime
from pathlib import Path

import pytest
from playwright.sync_api import Page, expect



def test_positive_login(navigate_to_login: Page) -> None:
    """Verify that the login page works correctly."""
    page = navigate_to_login
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

def test_negative_login(navigate_to_login: Page) -> None:
    """Verify that the login page works correctly when incorrect password is entered."""
    page= navigate_to_login
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").fill("secret_sauce1")
    page.locator("[data-test=\"login-button\"]").click()
    img_dir = Path("img")
    file_name = f"negative_login_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    page.screenshot(path=str(img_dir / file_name), full_page=True)
    error_msg = page.locator("[data-test=\"error\"]")
    expect(error_msg).to_be_visible()

@pytest.mark.sanity
def test_checkout(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()
    page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
    page.locator("[data-test=\"shopping-cart-link\"]").click()
    page.locator("[data-test=\"checkout\"]").click()
    page.locator("[data-test=\"firstName\"]").fill("Moshe")
    page.locator("[data-test=\"lastName\"]").fill("Cohen")
    page.locator("[data-test=\"postalCode\"]").fill("55555")
    page.locator("[data-test=\"continue\"]").click()
    page.locator("[data-test=\"finish\"]").click()
    assert page.locator("[data-test=\"complete-header\"]").text_content() == "Thank you for your order!"
    img_dir = Path("img")
    file_name = f"negative_login_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    page.screenshot(path=str(img_dir / file_name), full_page=True)
    page.locator("[data-test=\"back-to-products\"]").click()
    page.get_by_role("button", name="Open Menu").click()
    page.locator("[data-test=\"logout-sidebar-link\"]").click()