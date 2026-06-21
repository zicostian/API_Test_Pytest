import pytest
import os

@pytest.fixture
def api_request_context(playwright):
    """Provide a reusable Playwright APIRequestContext for API tests."""
    request = playwright.request.new_context()
    yield request
    request.dispose()

@pytest.fixture
def page(playwright, tmp_path):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    trace_file = os.path.join("test-results", f"{tmp_path.name}-trace.zip")
    os.makedirs("test-results", exist_ok=True)
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    yield page

    context.tracing.stop(path=trace_file)
    page.close()
    context.close()
    browser.close()
