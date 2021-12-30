import math
import requests
import socket
from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
import re


# 3. Checks For Internet Connectivity
# 1. test inbox send button
# 2. Data From Wikipedia to frame And Load More Button
# text = input("Enter text To search : ")


# Extraction of Data
def brackets_remover(line):
    return re.sub(r"[d]", line)


def nearest_space_finder(max_line_length, string):
    if max_line_length == (len(string)):
        return -1
    else:
        for f in range(max_line_length, len(string)):
            if string[f] == " ":
                return f
            else:
                max_line_length = max_line_length + 1
                nearest_space_finder(max_line_length, string)


def max_length_config(max_l, line):
    if (max_l + 100) > len(line):
        return len(line)
    else:
        return max_l + 100


def string_config(line):
    line = brackets_remover(0, line, "")
    max_line_length = max_length_config(0, line)
    print(max_line_length)
    cur_string_length = len(line)
    new_string = ""
    max_exe = math.ceil(cur_string_length / max_line_length)
    last_index = 0
    for exe in range(max_exe):
        if nearest_space_finder(max_line_length, line) == None:
            new_string = new_string + line[last_index: max_line_length] + "\n"
            last_index = max_line_length
            max_line_length = max_length_config(max_line_length, line)
        else:
            new_string = new_string + line[last_index: max_line_length] + line[max_line_length:nearest_space_finder(max_line_length, line)] + "\n"
            last_index = nearest_space_finder(max_line_length, line) + 1
            max_line_length = max_length_config(max_line_length, line)

        
    return new_string


# Fetching Data
def fetch_ex_wiki(search):
    dr = wd.Chrome("C:\\Program Files (x86)\\chromedriver.exe")
    dr.get("https://www.wikipedia.org/")
    dr.implicitly_wait(10)
    search_obj = dr.find_element_by_id("searchInput")
    search_obj.send_keys(search)
    search_obj.send_keys(Keys.RETURN)
    dr.implicitly_wait(10)
    m_h = dr.find_element_by_id("firstHeading")
    major_heading = m_h.text
    all_elements = dr.find_element_by_class_name("mw-parser-output")
    all_para_0 = all_elements.find_elements_by_tag_name("p")
    all_para = []
    for i in range(len(all_para_0)):
        if i == 0:
            pass
        else:
            all_para.append(all_para_0[i])
    all_strings = [string_config(para.text) for para in all_para]
    dr.quit()
    return [major_heading, all_strings]


# print(fetch_ex_wiki(text))


def check_internet():
    ip = socket.gethostbyname(socket.gethostname())
    if ip == "127.0.0.1":
        return False
    else:
        return True


def check_wiki_up():
    try:
        status_code = requests.request("get", "https://www.wikipedia.org/").status_code
        if status_code == 200:
            return True
        else:
            return False
    except:
        return False


def com_checker():
    if check_internet() and check_wiki_up():
        return True
    else:
        return False

para1 = "The total market capitalization of equity backed securities worldwide rose from US$2.5 trillion in 1980 to US$68.65 trillion at the end of 2018.[1] As of December 31, 2019, the total market capitalization of all stocks worldwide was approximately US$70.75 trillion.[1]"
print(re.sub(r"[]", "", para1))
#print(brackets_remover(para1, ""))