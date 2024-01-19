import time
import unittest
import configuration as conf
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class Test(unittest.TestCase):
    def setUp(self):
        # Create a new instance of the browser
        self.options = Options()

        # Firefox/Nightly location
        self.options.binary_location = conf.app_location()

        if conf.run_headless() is True:
            self.options.add_argument("--headless")

        self.driver = webdriver.Firefox(options=self.options)

    def test_click_star(self):

        print(" - TEST: Verify page can be Bookmarked")
        try:
            # Navigate to a common URL
            test_url = 'https://mozilla.com'
            self.driver.get(test_url)
            WebDriverWait(self.driver, 10).until(ec.url_changes(test_url))

            # Click Star button
            with self.driver.context(self.driver.CONTEXT_CHROME):
                # Bookmark star element: id="star-button" class="urlbar-icon" starred="true"
                # WORKS: self.driver.find_element(By.XPATH, '//*[@id="star-button"]').click()
                # WORKS: self.driver.find_element(By.CSS_SELECTOR, '#star-button').click()
                star_button = self.driver.find_element(By.ID, "star-button")
                star_button.click()

                # Wait for the bookmark dialog to open then Save bookmark
                save_button = WebDriverWait(self.driver, 10).until(
                    ec.presence_of_element_located((By.ID, "editBookmarkPanelDoneButton")))
                save_button.click()

                # Check to confirm the Star button is filled in
                starred_value = star_button.get_attribute("starred")
                self.assertEqual(starred_value, "true")
                print("The value of the starred attribute is '" + starred_value + "'")

            # Add a check for the presence of the bookmark. This is much more challenging
            # as we can't get access to the bookmark Sidebar nor the Library via DOM. As such,
            # our option here is to open a new tab, visit the same URL that was bookmarked, then
            # confirm the star is filled in, indicating the bookmark exist in Firefox.

            # Open a new Tab with the previously bookmarked page
            with self.driver.context(self.driver.CONTEXT_CONTENT):
                # Open a new tab after making first tab blank
                self.driver.get('about:blank')
                self.assertEqual(self.driver.title, "")
                print('The title of the page should be blank !' + self.driver.title + '! <- Nothing between those')
                self.driver.execute_script("window.open('');")

                # Switch to the new tab and open the Mozilla URL
                self.driver.switch_to.window(self.driver.window_handles[1])
                self.driver.get(test_url)
                WebDriverWait(self.driver, 10).until(ec.url_changes('https://mozilla.com'))

            with self.driver.context(self.driver.CONTEXT_CHROME):
                self.assertEqual(starred_value, "true")
                print("2nd check: The value of the starred attribute is '" + starred_value + "'")

        finally:
            # Close the browser after the test is complete
            self.driver.quit()


if __name__ == "__main__":
    unittest.main()
