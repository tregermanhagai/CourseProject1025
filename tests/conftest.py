import pytest
from playwright.sync_api import Page


@pytest.fixture
def prepare_and_tear_down(page: Page):
    """Login fixture: authenticates to Saucedemo and logs out after test."""
    page.goto("")
    page.locator('[data-test="username"]').fill("standard_user")
    page.locator('[data-test="password"]').fill("secret_sauce")
    page.locator('[data-test="login-button"]').click()
    yield
    page.get_by_role("button", name="Open Menu").click()
    page.locator('[data-test="logout-sidebar-link"]').click()

