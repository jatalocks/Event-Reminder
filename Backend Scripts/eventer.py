import codecs
from variables import *
from variables import eventsPageMaker
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import requests
import string
import re
import sys
import csv
import json
import glob
import os

def getEvents(num,city):
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    chrome_options.add_experimental_option("prefs",prefs)
    driver = webdriver.Chrome(chrome_options=chrome_options)
    asserted = "false"

    days = [datetime.now().strftime('%Y-%m-%d'),
    (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d'),
    (datetime.now() + timedelta(days=2)).strftime('%Y-%m-%d'),
    (datetime.now() + timedelta(days=3)).strftime('%Y-%m-%d'),
    (datetime.now() + timedelta(days=4)).strftime('%Y-%m-%d'),
    (datetime.now() + timedelta(days=5)).strftime('%Y-%m-%d'),
    (datetime.now() + timedelta(days=6)).strftime('%Y-%m-%d'),
    (datetime.now() + timedelta(days=7)).strftime('%Y-%m-%d'),
    (datetime.now() + timedelta(days=8)).strftime('%Y-%m-%d')]

    for day in range(num):
        city = city
        url = eventsPageMaker(city,day)
        driver.get(url)
        time.sleep(1)
        # Loging In
        if asserted == "false":
            assert "Facebook" in driver.title
            elem = driver.find_element_by_id("email")
            elem.send_keys(usr)
            elem = driver.find_element_by_id("pass")
            elem.send_keys(pwd)
            elem.send_keys(Keys.RETURN)
            asserted = "true"
        else:
            print("already asserted, moving on")

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
                try:
                    start = driver.execute_script(getStartingTime2)
                    start = re.findall("(\d{1,2} [A|P]M|\d{1,2}:\d{1,2} [A|P]M)",start)[0]
                except:
                    start = "-"
            try:
                end = driver.execute_script(getEndingTime)
            except:
                try:
                    end = driver.execute_script(getEndingTime2)
                    end = re.findall("(\d{1,2} [A|P]M|\d{1,2}:\d{1,2} [A|P]M)",end)[1]
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
                desc = driver.execute_script(getDesc)
            except:
                desc = "-"
            try:
                img = driver.execute_script(getImage)
                # img = "<img src=" + "\"" + img + "\"" + "></img>"
                img = img
            except:
                try:
                    img = driver.execute_script(getImage2)
                    # img = "<img src=" + "\"" + img + "\"" + "></img>"
                    img = img
                except:
                    img = "-"
            print(link);
            going = "false"
            event = [name,img,start,end,days[day],addr,place,city,link,desc,going]
            allEvents.append(event)

        print("Total Events: " + str(len(allEvents)))

        with open('csvfile.csv','ab') as file:
            file.write(b"Name,Image,Start Time,End Time,Date,Address,Place,City,Link,Description,Going")
            file.write(b"\n")
            for event in allEvents:
                newEvent = []
                for text in event:
                    if text == None or text == "":
                        text = "No_Info"
                        newEvent.append(text)
                    else:
                        if str(text).__contains__(","):
                            text = str(text).replace(",","")
                        newEvent.append(str(text))
                file.write(bytes(newEvent[0], encoding = "utf-8") + b"," + bytes(newEvent[1], encoding = "utf-8") + b"," + bytes(newEvent[2], encoding = "utf-8")
                   + b"," + bytes(newEvent[3], encoding = "utf-8")
                 + b"," + bytes(newEvent[4], encoding = "utf-8")
                  + b"," + bytes(newEvent[5], encoding = "utf-8")
                  + b"," + bytes(newEvent[6], encoding = "utf-8")
                   + b"," + bytes(newEvent[7], encoding = "utf-8")
                    + b"," + bytes(newEvent[8], encoding = "utf-8")
                     + b"," + bytes(newEvent[9], encoding = "utf-8")
                     + b"," + bytes(newEvent[10], encoding = "utf-8"))
                file.write(b'\n')

        file.close()
        driver.refresh();

def main():
    # Erase Old Data
    f = open("csvfile.csv", "w")
    f.write("")
    f.close()

    getEvents(3,"haifa")
    #getEvents(3,"tel_aviv")
    #driver.close()

    csvfile = open('csvfile.csv', 'r',encoding="utf-8")

    fieldnames = ("Name","Image","Start Time","End Time","Date","Address","Place","City","Link","Description","Going")

    reader = csv.DictReader(csvfile, fieldnames)

    out = json.dumps( [ row for row in reader ] )
    print("JSON parsed!")
    # Save the JSON
    f = open('file.json', 'w')
    f.write(out)
    print("JSON saved!")

    url = "https://eventreminder-6487.restdb.io/rest/eventtable"

    headers = {
        'content-type': "application/json",
        'x-apikey': "c22041d43b69ba2e022e2c7a2f2918f995ff7",
        'cache-control': "no-cache"
        }

    response = requests.request("DELETE", 'https://eventreminder-6487.restdb.io/rest/eventtable/*?q={"match_all": {}}', headers=headers)

    print(response.text)

    response = requests.request("POST", url, data=open('file.json','rb'), headers=headers)
    print(response.text)

    list = glob.glob('file.json_*.json')
    for jfile in (list):
        os.remove(jfile)

    size = (os.path.getsize('file.json') / 1000000)

    if (size > 1):
        with open("file.json",'r') as infile:
            o = json.load(infile)
            chunkSize = 200
            for i in range(0, len(o), chunkSize):
                with open("file.json" + '_' + str(i//chunkSize) + '.json', 'w') as outfile:
                    json.dump(o[i:i+chunkSize], outfile)
        list = glob.glob('file.json_*.json')
        print(list)
        for jfile in (list):
            print(jfile)
            response = requests.request("POST", url, data=open(jfile,'rb'), headers=headers)
            print(response.text)
    else:
        response = requests.request("POST", url, data=open('file.json','rb'), headers=headers)
        print(response.text)

    response = requests.request("DELETE", 'https://eventreminder-6487.restdb.io/rest/eventtable/*?q={"Name": "Name"}', headers=headers)
    print(response.text)

if __name__ == "__main__":
    main()
