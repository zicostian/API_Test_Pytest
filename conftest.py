import pytest
from playwright.sync_api import sync_playwright
import os

# @pytest.fixture(scope="session")
#def browser():
#    with sync_playwright() as p:
#        browser = p.chromium.launch(headless=False)  # Set to True to hide the browser
#        yield browser
#        browser.close()
        
# @pytest.fixture
#def page(browser):
#    page = browser.new_page()
#    yield page
#    page.close()
    
# Adding customized fixture to accommodate tracing

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture
def page(browser, tmp_path):
    context = browser.new_context()
    page = context.new_page()
    
    # Start tracing
    trace_file = os.path.join("test-results", f"{tmp_path.name}-trace.zip")
    os.makedirs("test-results", exist_ok=True)
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    
    yield page
    
    # Stop and save trace
    context.tracing.stop(path=trace_file)
    page.close()
    context.close()