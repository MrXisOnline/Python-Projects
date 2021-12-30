import time

from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

driver = wd.Chrome("C:\\Program Files (x86)\\chromedriver.exe")

driver.get("https://en.wikipedia.org/wiki/Stock_market")
print("\nthis is title :", driver.title, "\n")
all_text = driver.find_elements_by_tag_name("p")
for text in all_text:
    print(text.text)
'''
try:
    des = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.TAG_NAME, "p"))
    )
    print(des.test)
finally:
    driver.quit()
'''
time.sleep(5)
driver.quit()
