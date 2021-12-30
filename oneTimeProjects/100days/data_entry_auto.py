from bs4 import BeautifulSoup as soup
from selenium import webdriver
import requests

driver_path = "C:\\Dev\\edgedriver_win64\\msedgedriver.exe"
# zillow_url = "https://www.zillow.com/homes/Los-Angeles,-CA_rb/"
zillow_url = "https://www.zillow.com/los-angeles-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22Los%20Angeles%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-118.78252157421876%2C%22east%22%3A-118.05467733593751%2C%22south%22%3A33.78214897805991%2C%22north%22%3A34.32600608223679%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A12447%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A0%2C%22max%22%3A880312%7D%2C%22mp%22%3A%7B%22min%22%3A0%2C%22max%22%3A3000%7D%2C%22beds%22%3A%7B%22min%22%3A1%2C%22max%22%3A1%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22land%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.74 Safari/537.36 Edg/79.0.309.43",
    "Accept-Language": "en-US,en;q=0.5"
}
form_url = "https://forms.gle/LfPLWRKCMegnL9Ue7"
response = requests.get(url=zillow_url, headers=header)
full_html = response.text.encode("utf-8")
html = soup(full_html, "html.parser")
tags = html.select(selector=".photo-cards li")
# print(tags)
data = {}
# i=2
for i in range(len(tags)):
    try:
        art = tags[i].find(name="article", class_="list-card")
        addr_a = art.select_one(".list-card-info a")
    except AttributeError:
        continue
    else:
        link = addr_a.get("href")
        # print(addr.getText())
        de_price = art.select_one(".list-card-info .list-card-heading")
        price = de_price.find(name="div", class_="list-card-price")
        # print(price.getText())
        house_de = de_price.find(name="ul", class_="list-card-details")
        # print(house_de.getText())
        data[i] = {"Address": addr_a.getText(), "Room_Details": house_de.getText(), "Price": price.getText(),
                   "Link": link}

driver = webdriver.Edge(driver_path)
driver.get(form_url)
for k in data.keys():
    add_tag = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    rd_tag = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    pr_tag = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    lk_tag = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea')
    sub_tag = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
    add_tag.send_keys(data[k]["Address"])
    rd_tag.send_keys(data[k]["Room_Details"])
    pr_tag.send_keys(data[k]["Price"])
    lk_tag.send_keys(data[k]["Link"])
    sub_tag.click()
    resp_tag = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    resp_tag.click()
driver.close()
