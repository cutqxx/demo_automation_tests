import pytest
from playwright.sync_api import Page, Browser, BrowserContext, expect, sync_playwright
from settings import browser_headless


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=browser_headless)
        page = browser.new_page()
        page.goto("http://playwright.dev")
        print(page.title())
        browser.close()
    yield browser


@pytest.fixture
def page(browser: Browser, request):
    context = browser.new_context(**params)
    page: Page = context.new_page()
    page.set_default_timeout(10_000)
    failed_requests = []
    page.on(
        "requestfailed",
        lambda request: failed_requests.append(
            {
                "url": request.url,
                "method": request.method,
                "failure": request.failure,
                "timing": request.timing,
            }
        ),
    )
    yield page
    page.close()
    context.close()
