
from selenium import webdriver
import browser_cookie3
import time
import json
import requests

driver = webdriver.Firefox(executable_path='../blogService/drivers/platform/firefox/geckodriver-v0.28.0-linux64/geckodriver')

url = "https://mp.toutiao.com/profile_v4/graphic/publish?pgc_id=6914824442329907715"


# 必须先打开才能添加cookie
driver.get(url)

for c in browser_cookie3.firefox():
    isScure = True
    if (c.secure == 0):
        isScure = False
    driver.add_cookie({'name' : c.name, 'value' : c.value, 'path' : c.path, 'secure': isScure})

driver.get(url)

title = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/section/main/div[2]/div/div/div[1]/div[3]/div/div/div[2]/div/div/div/textarea')
title.clear()
title.send_keys("xxxxxxxxxxxxxxxx")

content = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/section/main/div[2]/div/div/div[1]/div[4]/div/div[1]')
my_desired_text="lzylzylzy" 
driver.execute_script("document.getElementsByClassName('ProseMirror')[0].innerHTML='"+my_desired_text+"'")