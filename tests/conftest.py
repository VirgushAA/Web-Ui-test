import pytest
from playwright.sync_api import sync_playwright
from pages.main_page import MainPage


@pytest.fixture(scope="function")
def browser_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            locale="en-US",
            timezone_id="Europe/Moscow",
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
                (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            extra_http_headers={},
            ignore_https_errors=False,
        )

        page = context.new_page()
        yield page

        browser.close()

@pytest.fixture
def main_page(browser_page):
    return MainPage(browser_page)
