# pip install selenium

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
#options.add_argument('headless')
options.add_argument("user-agent=Mozilla/5.0")
options.add_argument("--start-maximized")

driver = webdriver.Chrome('chromedriver.exe', chrome_options=options)
#driver = webdriver.Chrome('chromedriver.exe')

url = "https://www.naver.com/"

driver.get(url)
time.sleep(2)

inputElement = driver.find_element(By.NAME,"query")
inputElement.clear()
time.sleep(1)
inputElement.send_keys("개발자")
time.sleep(1)
inputElement.submit()
time.sleep(1)

results = driver.find_elements(By.CLASS_NAME,'total_tit')
time.sleep(1)
for one in results:
	print(one.text)
time.sleep(1)

results[0].click()
time.sleep(2)

# WebDriver를 종료합니다. (브라우저 닫기)
driver.quit()

