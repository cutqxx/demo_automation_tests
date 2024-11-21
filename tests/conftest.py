import pytest
from playwright.sync_api import Page, Browser, sync_playwright
import settings


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=settings.browser_headless)
        yield browser  # Возвращаем браузер, чтобы он использовался в тестах
        browser.close()  # Закрываем браузер после завершения всех тестов


@pytest.fixture
def page(browser: Browser, request):
    params = {"viewport": {"width": 1920, "height": 1080}}
    context = browser.new_context(**params)  # Создаём новый контекст для изоляции теста
    page: Page = context.new_page()
    page.set_default_timeout(15_000)
    yield page
    page.close()
    context.close()
