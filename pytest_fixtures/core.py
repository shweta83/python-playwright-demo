from playwright.sync_api import sync_playwright
import pytest
import os

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        headless = os.getenv("CI", "false") == "true"
        browser = p.chromium.launch(headless=headless)
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()


