[![Playwright Tests CI](https://github.com/zicostian/API_Test_Pytest/actions/workflows/playwright.yml/badge.svg)](https://github.com/zicostian/API_Test_Pytest/actions/workflows/playwright.yml)

# API Test Pytest

This repository contains API test examples using Python, the `pytest` framework, and Playwright's `APIRequestContext` for HTTP requests.

## Description

This project demonstrates API automation using Playwright's request capabilities combined with Python `pytest` for test execution and reporting. It includes sample API tests for a hotel booking-style service and shows how to send both `GET` and `POST` requests, validate responses, and generate HTML reports.

## Prerequisites

- Python 3.14
- Git
- A terminal or shell environment
- (Optional) VS Code or another IDE for editing and running tests

## Installation

1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd API_Test_Pytest
   ```
2. Create and install dependencies in a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

## Activate Virtual Environment

Activate the virtual environment before running tests:

```bash
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

## Run the tests

Execute all tests with:

```bash
pytest tests/ -v
```

Run a specific file:

```bash
pytest tests/api_get_test.py -v
```

The test suite is configured to generate an HTML report at `reports/report.html`.

## Key Highlights

- Uses `pytest` as the test runner and assertion framework
- Uses Playwright's `APIRequestContext` for API requests and response validation
- Demonstrates API test patterns for both `GET` and `POST` calls
- Generates HTML reports via `pytest-html`
- Includes standalone test files and a GitHub Actions workflow for CI

## Example test pattern

A typical test in this project follows these steps:

1. Create a Playwright request context
2. Send an API request (`GET`, `POST`, etc.)
3. Validate the status code
4. Parse the JSON response
5. Assert expected response fields or behavior
6. Clean up the request context

Example snippet:

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    request = p.request.new_context()
    response = request.get("https://example.com/api/resource")
    assert response.status == 200
    data = response.json()
    assert data["key"] == "value"
    request.dispose()
```

## Notes

- The current project includes API tests for hotel booking endpoints and a Playwright sample request test.
- Use the `.venv` virtual environment to ensure dependencies are loaded correctly.
- The GitHub Actions workflow is configured to run on pushes to `main` and pull requests.

## Author

[Zico Agustian Rusdy](https://linkedin.com/in/zicostian)
