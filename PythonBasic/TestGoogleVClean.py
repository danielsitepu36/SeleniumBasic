import time
import unittest

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.keys import Keys

PATH = "C:\Program Files\geckodriver.exe"

class LoginTest(unittest.TestCase):
    query = ""

    def setUp(self):
        LoginTest.query = input("Query: ")
        print("Waiting for results...\n")

        self.driver = webdriver.Firefox(executable_path=PATH)

    def test_login(self):

        driver = self.driver
        driver.get("https://www.google.com")

        searchFieldElement = WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element_by_name("q"))

        searchFieldElement.clear()
        searchFieldElement.send_keys(LoginTest.query)
        # searchFieldElement.send_keys(Keys.RETURN)
        searchFieldElement.submit()

        WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element_by_tag_name("h3"))

        results = driver.find_elements_by_xpath(
            '(//div[contains(@class, "yuRUbf")]/a)')
        links = [link.get_attribute('href') for link in results]

        title = [title.find_element_by_xpath(
            '(h3[contains(@class, "LC20lb DKV0Md")]/span)').text for title in results]

        for i in range(len(links)):
            print(title[i])
            print(links[i], end="\n\n")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
