from selenium import webdriver as wd
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = wd.Chrome("C:\\Program Files (x86)\\chromedriver.exe")
driver.get("https://orteil.dashnet.org/cookieclicker/")
driver.implicitly_wait(10)
cookie = driver.find_element_by_id("bigCookie")
# cookie.click()
actions = ActionChains(driver)
actions.click(cookie)

for i in range(1000):
    actions.perform()
