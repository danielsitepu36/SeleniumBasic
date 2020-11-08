import time
import unittest

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

PATH = "C:\Program Files\geckodriver.exe"
# driver = webdriver.Firefox(executable_path=PATH)
# driver.set_page_load_timeout(30)
# print("Page loaded")


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=PATH)

    def test_login(self):
        driver = self.driver
        driver.get("https://www.google.com")

        query = "abc"

        searchFieldElement = WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element_by_name("q"))

        searchFieldElement.clear()
        searchFieldElement.send_keys(query)
        # searchFieldElement.send_keys(Keys.RETURN)
        searchFieldElement.submit()

        WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element_by_tag_name("h3"))

        results = driver.find_elements_by_xpath(
            '(//div[contains(@class, "yuRUbf")]/a)')
        links = [link.get_attribute('href') for link in results]
        # print(links)

        # results = driver.find_elements_by_xpath(
        #     '(//h3[contains(@class, "LC20lb DKV0Md")]/span)')
        title = [title.find_element_by_xpath(
            '(h3[contains(@class, "LC20lb DKV0Md")]/span)').text for title in results]
        # print(title)

        for i in range(len(links)):
            print(title[i])
            print(links[i], end="\n\n")

        # title = [result.text for result in results]
        # for i in title:
        #     print(i, end="\n\n")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
