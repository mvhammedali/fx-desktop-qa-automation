import pytest
from time import sleep
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from modules.util import BrowserActions
from modules.page_object import Navigation


def test_search_modes_for_sites(driver: Firefox, search_modes: dict):
    # C2234690
    # C1365213 (potentially)
    nav = Navigation()
    wait = WebDriverWait(driver, 10)
    with driver.context(driver.CONTEXT_CHROME):
        awesome_bar = driver.find_element(*nav.awesome_bar)
        for site in search_modes["site"]:
            awesome_bar.send_keys(site[:2].lower())
            wait.until(EC.visibility_of_element_located(nav.tab_to_search_text_span))
            awesome_bar.send_keys(Keys.TAB)
            wait.until(EC.text_to_be_present_in_element(nav.search_mode_span, site))
            awesome_bar.send_keys("soccer" + Keys.RETURN)
            with driver.context(driver.CONTEXT_CONTENT):
                wait.until(EC.url_contains(site.lower()))
            awesome_bar.clear()


def test_test_intervention_card(driver: Firefox):
    nav = Navigation()
    wait = WebDriverWait(driver, 5)
    with driver.context(driver.CONTEXT_CHROME):
        awesome_bar = driver.find_element(*nav.awesome_bar)
        awesome_bar.send_keys("refresh firefox")
        # wait.until(EC.visibility_of_element_located(nav.quick_actions_refresh_button))
        wait.until(EC.visibility_of_element_located(nav.fx_refresh_text))
        wait.until(EC.visibility_of_element_located(nav.fx_refresh_button))
        wait.until(EC.visibility_of_element_located(nav.fx_refresh_menu))
        driver.find_element(*nav.fx_refresh_menu).click()
        wait.until(EC.presence_of_element_located(nav.fx_refresh_menu_get_help_item))
