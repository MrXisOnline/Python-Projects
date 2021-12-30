from selenium import webdriver

driver_path = "C:\\Dev\\edgedriver_win64\\msedgedriver.exe"
url = "http://secure-retreat-92358.herokuapp.com/"
driver = webdriver.Edge(driver_path)
driver.get(url)
btn = driver.find_element_by_class_name("btn")
fn = driver.find_element_by_name("fName")
ln = driver.find_element_by_name("lName")
em = driver.find_element_by_name("email")
fn.send_keys("Suraj")
ln.send_keys("Gupta")
em.send_keys("testmail@gmail.com")
# print(input_tags)
btn.click()