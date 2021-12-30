import pandas as pd
from selenium import webdriver

path = "C:\\Dev\\edgedriver_win64\\msedgedriver.exe"

driver = webdriver.Edge(path)
driver.get("https://steamdb.info/graph/")
element = driver.find_element_by_xpath('//*[@id="table-apps"]/tbody')
tr = element.find_elements_by_tag_name("tr")
rank = []
name = []
img = []
for t in tr:
    tds = t.find_elements_by_tag_name("td")
    rank.append(tds[0].text)
    name.append(tds[3].text)
    img.append(tds[2].find_element_by_tag_name("a").find_element_by_tag_name("img").get_attribute("src"))
driver.close()
data_dict = {
    "Rank": rank,
    "Name": name,
    "Img": img
}
data = pd.DataFrame(data_dict)
data.to_csv("data.csv")
