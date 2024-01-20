import pytest
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from Config.config import TestData


@pytest.fixture(params=['firefox', 'chrome'], scope='class')
def init_driver(request):
    if request.param == "chrome":
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--headless")  # turn on headless mode
        web_driver = RemoteWebDriver(command_executor=TestData.SELENIUM_GRID_CHROME_URL, options=chrome_options)
    if request.param == "firefox":
        firefox_options = FirefoxOptions()
        firefox_options.headless = True  # turn on headless mode
        web_driver = RemoteWebDriver(command_executor=TestData.SELENIUM_GRID_FIREFOX_URL, options=firefox_options)

    # web_driver.implicitly_wait(15)
    request.cls.driver = web_driver
    yield
    web_driver.quit()


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_makereport(item, call):
    if "init_driver" in item.fixturenames:
        try:
            web_driver = item.cls.driver
        except AttributeError:
            # Handle the case where the driver is not available
            return

        if call.excinfo is not None:
            # Test failed, take a screenshot
            screenshot_path = f"Reports/screenshots/{item.name}_failure_hook.png"
            try:
                web_driver.save_screenshot(screenshot_path)
            except Exception as e:
                # Handle errors while saving the screenshot
                print(f"Error saving screenshot: {e}")
                return

            # Use result log path if available, otherwise use a default path
            result_log_path = getattr(item.config.option, 'resultlog', 'default_log.txt')
            with open(result_log_path, "a") as log:
                log.write(f"\nScreenshot (from hook): {screenshot_path}")
