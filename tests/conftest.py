import pytest
from selenium import webdriver

driver = 0


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")


@pytest.fixture(scope='class')
def setup(request):
    global driver
    browser_name = request.config.getoption("--browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == 'edge':
        driver = webdriver.Edge()
    driver.maximize_window()
    driver.implicitly_wait(3)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    request.cls.driver = driver
    yield
    driver.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):  # Include 'call' argument for correct behavior
    """
    Extends the pytest plugin to take and embed screenshots in the HTML reports, whenever a test fails
    :param item: The test item
    :param call: The call information for the test
    """

    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield  # Yield control for report generation
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when in ('call', "setup"):  # Use a more concise way to check for both phases
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            try:
                _capture_screenshot(file_name)  # Handle potential errors here
            except Exception as e:
                print(f"Error capturing screenshot: {e}")  # Log any errors
            else:
                if file_name:
                    html = ('<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" '
                            'onclick="window.open(this.src)" align="right"/></div>') % file_name
                    extra.append(pytest_html.extras.html(html))
    report.extras = extra  # Correctly assign the modified extras


def _capture_screenshot(file_name):
    driver.get_screenshot_as_file(file_name)
