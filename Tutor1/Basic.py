from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PATH = "C:\Program Files\geckodriver.exe"
driver = webdriver.Firefox(executable_path=PATH)
driver.set_page_load_timeout(30)

driver.get("https://www.python.org")
print("Page loaded")

# print(driver)
# print(driver.title)

assert "Python" in driver.title

# print("test")
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)

assert "No result found." not in driver.page_source

# driver.quit()
