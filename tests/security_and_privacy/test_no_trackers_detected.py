from time import sleep
import pytest
from selenium.webdriver import Firefox
from modules.browser_object_navigation import Navigation

NOTRACKERS_URL = "http://example.com/"

@pytest.fixture()
def add_prefs():
    return []


def test_no_trackers_detected(driver: Firefox):
    """
    C446391 No trackers are detected
    """
    nav = Navigation(driver)
    sleep(4)
    driver.get(NOTRACKERS_URL)

    # Click on the shield icon and verify that trackers are detected
    with driver.context(driver.CONTEXT_CHROME):
        nav.get_element("shield-icon").click()
        assert nav.get_element("no-trackers-detected").is_displayed()