from datetime import datetime
from pathlib import Path

import pytest
from playwright.sync_api import Page, expect


class TestSaucedemoUIWithFixture:


    @pytest.mark.sanity
    @pytest.mark.usefixtures("prepare_and_tear_down")
    def test_positive_login(self, page: Page) -> None:
        """Verify that the login page works correctly."""

        img_dir = Path(__file__).resolve().parents[1] / "img"
        img_dir.mkdir(parents=True, exist_ok=True)
        file_name = f"positive_login_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        page.screenshot(path=str(img_dir / file_name), full_page=True)
        assert page.locator(".app_logo").text_content() == "Swag Labs"

    @pytest.mark.sanity
    def test_negative_login(self, page: Page) -> None:
        """Verify that the login page works correctly."""
        page.goto("")
        page.locator('[data-test="username"]').fill("standard_user")
        page.locator('[data-test="password"]').fill("wrong_password")
        page.locator('[data-test="login-button"]').click()

        # Verify error message appears
        expect(page.locator('[data-test="error"]')).to_be_visible()

        img_dir = Path(__file__).resolve().parents[1] / "img"
        img_dir.mkdir(parents=True, exist_ok=True)
        file_name = f"negative_login_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        page.screenshot(path=str(img_dir / file_name), full_page=True)


