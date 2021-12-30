from selenium import webdriver


def check_cookies():
    counter_tag = driver.find_element_by_id("cookies")
    text = counter_tag.text
    num_cook = int(text.split()[0])
    print(num_cook)


def check_products():
    product = driver.find_elements_by_css_selector("#products .unlocked")
    if len(product) != 0:
        product[len(product)-1].click()


driver_path = "C:\\Dev\\edgedriver_win64\\msedgedriver.exe"
url = "https://orteil.dashnet.org/cookieclicker/"
driver = webdriver.Edge(driver_path)
driver.get(url)
driver.implicitly_wait(5)
tag = driver.find_element_by_id("bigCookie")
ex = 1
while True:
    tag.click()
    if ex > 50:
        check_products()
        ex = 0
    ex += 1
# tag.click()
# driver.implicitly_wait(1)
# tag.click()

# driver.close()