#Import Selenium Webdriver
from selenium import webdriver


# Resize the window to the desired screen width/height


#Open URL
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get('https://app.zapptales.com/en/chats/39a3fb4a-4b36-4847-9b5b-3d98c06c90b2')

# Close welcome screen
#To find element id right click on button and hit select inspect element
#The name will be in a bubble above the text.
#In our case the element id is close welcome screen
counter = 0
while True:
    elem = driver.execute_script("return document.getElementsByClassName('pagination pagination--mobile')[0].getElementsByTagName('li')[3].children[0]")
    elem.click();
    driver.save_screenshot('screenshot' + counter + '.png')
    counter+=1


#save screenshot


#close window
driver.quit()
