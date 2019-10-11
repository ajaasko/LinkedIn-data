# -*- coding: utf-8 -*
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options  
from urllib.request import urlopen
import time as t#delay
import datetime
import csv
import sys
from resources import *

a1 = "//span[@class='v-align-middle social-details-social-counts__reactions-count']"
a2 = "//*[contains(text(), ' of your post in the feed')]"
a3 = "//*[contains(text(), ' Comments')]"

try:
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument('--log-level=3')
    options.headless = True
    driver = webdriver.Chrome(options=options)		
    last_height = driver.execute_script("return document.body.scrollHeight")

    #driver.implicitly_wait(10) #wait that pages are loaded and elements are visible
    driver.get("http://www.linkedin.com")
    #driver.maximize_window()
    #print(driver.title)
    driver.find_element_by_link_text("Sign in").click() #ok
    elem = driver.find_element_by_id("username").send_keys(userName)
    elem = driver.find_element_by_id("password").send_keys(passWord)
    elem = driver.find_element_by_class_name("login__form_action_container").click()


    t.sleep(5)
    #try:
    element = driver.find_element_by_xpath("//span[contains(.,'Views of your post')]").click() 
    t.sleep(5)
    last_height = driver.execute_script("return document.body.scrollHeight")
    print("jjj", last_height)
    
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        t.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    print(last_height)

    count = 0
    count2 = 0
    count3 = 0
    total_views = []
    total_comments = []
    total_likes = []

    for a in driver.find_elements_by_xpath(a2):
		
    	temp1 = a.text[0:50]
    	data1 = temp1.split(" ")
    	views_temp = data1[0]
    	views = views_temp.replace(',','')
    	total_views.append(int(views))
    	count = count + 1
    	#print(count, views)
	
    for b in driver.find_elements_by_xpath(a1):
        temp2 = b.text[0:50]
        data2 = temp2.split(" ")
        likes_temp = data2[0]
        likes = likes_temp.replace(',','')
        total_likes.append(int(likes))

    for c in driver.find_elements_by_xpath(a3):
    	temp3 = c.text[0:50]
    	#print(temp1)
    	data3 = temp3.split(" ")
    	comments_temp = data3[0]
    	comments = comments_temp.replace(',','')
    	total_comments.append(int(comments))
	
    print("Posts:", count)
    print("Views: {}".format(sum(total_views)))
    print("Average views per post: {}".format(round(sum(total_views)/count),2))
    print("Comments:", sum(total_comments))
    print("Likes:", sum(total_likes))
    driver.close()

except NoSuchElementException:
	print("NoSuchElementException, check your code.")
except WebDriverException:
	print(" ")
except KeyboardInterrupt:
	print("You cancelled the operation.")


