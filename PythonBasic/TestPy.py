import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PATH = "C:\Program Files\geckodriver.exe"
# driver = webdriver.Firefox(executable_path=PATH)
# driver.set_page_load_timeout(30)
# print("Page loaded")

class PythonOrgSearch(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Firefox(executable_path=PATH)

    def test_search_in_python_org(self):
        driver = self.driver
        driver.set_page_load_timeout(30)
        driver.get("https://www.python.org")
        print("Page loaded")

        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name('q')
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)

        assert "No results found" not in driver.page_source

    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()