import codecs
import pandas as pd
from variables import *
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import requests
import string
import re
import sys

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(chrome_options=chrome_options)

driver.get(url)

# Loging In
assert "Facebook" in driver.title
elem = driver.find_element_by_id("email")
elem.send_keys(usr)
elem = driver.find_element_by_id("pass")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)

'''
while (True):
    try:
        driver.execute_script(getID)
        break
    except:
        print("Waiting")
        time.sleep(0.5)
'''
# Get scroll height
last_height = driver.execute_script(last)

while True:
    # Scroll down to bottom
    try:
        driver.execute_script(scroll)
        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script(last)
        if new_height == last_height:
            break
        last_height = new_height
    except:
        print("Waiting")
        time.sleep(0.5)

list = []
for i in range(50):
    print(i)
    print("return document.getElementsByClassName('_7ty')[" + str(i) + "].href")
    try:
        getID = "return document.getElementsByClassName('_7ty')[" + str(i) + "].href"
        temp = driver.execute_script(getID)
        # first = temp.split("/events/")
        # id = first[1].split("/?")[0]
        list.append(temp)
    except:
        print("Broke On Event Number: " + str(i))
        break
print("List Length: " + str(len(list)))
allEvents = []

for link in list:
    driver.get(link)
    try:
        name = driver.execute_script(getName)
    except:
        name = "-"
    try:
        start = driver.execute_script(getStartingTime)
    except:
        start = "-"
    try:
        end = driver.execute_script(getEndingTime)
    except:
        end = "-"
    try:
        addr = driver.execute_script(getAddr)
    except:
        addr = "-"
    try:
        place = driver.execute_script(getPlace)
    except:
        place = "-"
    try:
        img = driver.execute_script(getImage)
        img = "<img src=" + "\"" + img + "\"" + "></img>"
    except:
        try:
            img = driver.execute_script(getImage2)
            img = "<img src=" + "\"" + img + "\"" + "></img>"
        except:
            img = "-"
    event = [name,img,start,end,addr,place]
    allEvents.append(event)

print("Total Events: " + str(len(allEvents)))
# Erase Old Data
f = open("csvfile.csv", "w")
f.write("")
f.close()

with open('csvfile.csv','wb') as file:
    file.write(b"Name,Image,Start Time,End Time,Address,Place")
    file.write(b"\n")
    for event in allEvents:
        newEvent = []
        for text in event:
            if text == None or text == "":
                text = "No_Info"
                newEvent.append(text)
            else:
                if text.__contains__(","):
                    text = text.replace(",","")
                newEvent.append(text)
        file.write(bytes(newEvent[0], encoding = "utf-8") + b"," + bytes(newEvent[1], encoding = "utf-8") + b"," + bytes(newEvent[2], encoding = "utf-8") + b"," + bytes(newEvent[3], encoding = "utf-8")
         + b"," + bytes(newEvent[4], encoding = "utf-8") + b"," + bytes(newEvent[5], encoding = "utf-8"))
        file.write(b'\n')

file.close()
driver.close()

df = pd.read_csv("csvfile.csv",encoding='utf-8')
pd.set_option('display.max_colwidth', -1)
HTML_file = df.to_html(classes='utf8')
HTML_file += styling

file = codecs.open('utf8html.html','w','utf-8')
file.write('<meta http-equiv=\"Content-Type\" content=\"text/html;charset=UTF-8\">')
file.write(HTML_file)
file.close()

with codecs.open("utf8html.html", "r",'utf-8') as fin:
    with codecs.open("index.html", "w",'utf-8') as fout:
        for line in fin:
            fout.write(line.replace("&lt;","<").replace("&gt;",">"))

fout.close()
