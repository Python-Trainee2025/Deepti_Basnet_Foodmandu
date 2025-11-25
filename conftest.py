import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="class")
def setup(request):                                                 #creates browsers and prepares config
    chrome_options = Options()                                      #set up how chrome should launch
    chrome_options.add_argument('--start-maximized')
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--disable-popup-blocking')
    chrome_options.add_argument('--disable-infobars')
    chrome_options.add_argument('--guest')

    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection_enabled": False
    }
    chrome_options.add_experimental_option("prefs", prefs)
    # Create the browser
    driver = webdriver.Chrome(options=chrome_options)
    # Attach driver to class so tests can use self.driver

    request.cls.driver = driver
    # Give the driver to the tests
    yield driver
    # Close the browser when all tests in the class are done
    driver.quit()