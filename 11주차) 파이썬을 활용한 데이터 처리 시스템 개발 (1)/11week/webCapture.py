# pip install selenium
# https://chromedriver.chromium.org/ 

import time
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('headless')

driver = webdriver.Chrome('chromedriver.exe', chrome_options=options)

url = "http://www.naver.com/"
driver.get(url)
driver.implicitly_wait(2)

driver.get_screenshot_as_file("webCapture.png")

driver.quit()
