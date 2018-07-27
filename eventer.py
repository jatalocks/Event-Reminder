import codecs
import pandas as pd
#import urllib2
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import requests
import string
import re
import sys

# Variables:
haifa = "110619208966868"
tel_aviv = "106371992735156"
usr = "amitai333@gmail.com"
pwd = "Amitai321"
url = 'https://www.facebook.com/events/discovery/?suggestion_token={"time":"today","city":"'
url += haifa
url += '"}&acontext={"source":2,"source_dashboard_filter":"discovery","action_history":"[{\"surface\":\"dashboard\",\"mechanism\":\"dashboard_home_discovery_filter\"},{\"surface\":\"discover_filter_list\",\"mechanism\":\"surface\",\"extra_data\":{\"dashboard_filter\":\"discovery\"}}]","has_source":true}'
getID = """ return document.getElementsByClassName("_7ty")[0].href """
SCROLL_PAUSE_TIME = 1.5

getName = """ return document.getElementById("pageTitle").text """
getStartingTime = """ return document.getElementsByClassName("_164e")[0].nextSibling.nextSibling.innerText """
getEndingTime = """ return document.getElementsByClassName("_164e")[0].nextSibling.nextSibling.nextSibling.nextSibling.innerText """
getAddr = """ return document.getElementsByClassName("_5xhp fsm fwn fcg")[1].innerText """
getPlace = """ return document.getElementsByClassName("_5xhk")[1].text """
getImage = """ return document.getElementsByClassName("uiScaledImageContainer _3ojl")[0].childNodes[0].src """
getImage2 = """ return document.getElementsByClassName("_m54 _1jto _3htz hidden_elem")[0].childNodes[0].src """

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

while (True):
    try:
        driver.execute_script(getID)
        break
    except:
        print("Waiting")
        time.sleep(0.5)

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    try:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    except:
        print("Waiting")
        time.sleep(0.5)

list = []
for i in range(100):
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
#df.style.format(percent)applymap(color_negative_red, subset=['col1', 'col2']).set_properties(**{'font-size': '9pt', 'font-family': 'Calibri'}).bar(subset=['col4', 'col5'], color='lightblue').render()
pd.set_option('display.max_colwidth', -1)
HTML_file = df.to_html(classes='utf8')
HTML_file += """ <style>
html,
body {
	height: 100%;
}

body {
	margin: 0;
	background: linear-gradient(45deg, #49a09d, #5f2c82);
	font-family: sans-serif;
	font-weight: 100;
  margin: 0;
  background-repeat: no-repeat;
  background-attachment: fixed;
}

.container {
	position: absolute;
	top: 50%;
	left: 50%;
	transform: translate(-50%, -50%);
}

table {
	width: 100%;
    height: 100%;
	border-collapse: collapse;
	box-shadow: 0 0 20px rgba(0,0,0,0.1);
}

th,
td {
	padding: 15px;
	background-color: rgba(255,255,255,0.2);
	color: #fff;
  word-wrap: break-word;
}

th {
	text-align: left;
}

thead {
	th {
		background-color: #55608f;
	}
}
</style>
"""

file = codecs.open('utf8html.html','w','utf-8')
file.write(""" <meta http-equiv="Content-Type" content="text/html;charset=UTF-8"> """)
file.write(HTML_file)
file.close()

with codecs.open("utf8html.html", "r",'utf-8') as fin:
    with codecs.open("events.html", "w",'utf-8') as fout:
        for line in fin:
            fout.write(line.replace("&lt;","<").replace("&gt;",">"))

fout.close()
