import argparse
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

dirname = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(dirname, 'venv', 'bin', 'chromedriver')
print(filename)
driver = webdriver.Chrome()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()

