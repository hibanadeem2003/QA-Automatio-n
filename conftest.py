import pytest
from playwright.sync_api import sync_playwright
import pytest_html

@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        yield page
        browser.close()

@pytest.hookimpl(wrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome
    if report.when == "call":
        page = item.funcargs.get("page")
        extra = getattr(report, "extra", [])

        if report.failed and page:
            screenshot_path = f"failure_{item.name}.png"
            page.screenshot(path=screenshot_path)
            extra.append(pytest_html.extras.image(screenshot_path))
            extra.append(pytest_html.extras.text(
                f"Test failed.\nReason: {call.excinfo.value}",
                name="Failure Reason"
            ))
        elif report.passed:
            extra.append(pytest_html.extras.text(
                "Test passed. Actual result matched expected result.",
                name="Result Summary"
            ))

        report.extra = extra
    return report