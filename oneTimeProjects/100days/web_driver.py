from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver_path = "C:\\Dev\\edgedriver_win64\\msedgedriver.exe"
# time.sleep(5)
# tag = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
# tag = driver.find_element_by_name("q")
# print(tag.get_attribute("class"))
# url = "https://en.wikipedia.org/wiki/Main_Page"
# driver = webdriver.Edge(driver_path)
# driver.get(url)
# tag = driver.find_element_by_xpath('//*[@id="content"]/div/section/div[3]/div[2]/div/ul')
# li_tags = tag.find_elements_by_tag_name("li")
# ind = 0
# data = {}
# for li in li_tags:
#     time = li.find_element_by_tag_name("time")
#     a = li.find_element_by_tag_name("a")
#     data[ind] = {time.text: a.text}
#     ind += 1
# print(data)
# url = "https://en.wikipedia.org/wiki/Main_Page"
# driver = webdriver.Edge(driver_path)
# driver.get(url)
# tag = driver.find_element_by_xpath('//*[@id="articlecount"]/a[1]')
# print(tag.text)
url = "https://en.wikipedia.org/wiki/Main_Page"
driver = webdriver.Edge(driver_path)
driver.get(url)
tag = driver.find_element_by_xpath('//*[@id="searchInput"]')
tag.click()
tag.send_keys("Python")
tag.send_keys(Keys.ENTER)
driver.close()
