import time
import unittest

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

PATH = "C:\Program Files\geckodriver.exe"
# driver = webdriver.Firefox(executable_path=PATH)
# driver.set_page_load_timeout(30)
# print("Page loaded")


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=PATH)

    def test_login(self):
        driver = self.driver
        driver.get("https://www.facebook.com")

        username = "abc"
        password = "def"

        emailFieldID = 'email'
        passFieldID = 'pass'
        loginButtonID = 'u_0_b'
        fbLogoXpath = '(//a[contains(@href, "logo")])[1]'

        emailFieldElement = WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element_by_id(emailFieldID))
        passFieldElement = WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element_by_id(passFieldID))
        loginButtonElement = WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element_by_id(loginButtonID))

        emailFieldElement.clear()
        emailFieldElement.send_keys(username)
        passFieldElement.clear()
        passFieldElement.send_keys(password)

        loginButtonElement.click()
        WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element_by_xpath(fbLogoXpath))

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
