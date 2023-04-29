from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options 
#import org.openqa.selenium.Keys
from response.main import *
import time
import os
import re
service = Service(executable_path=os.path.abspath(__file__ + "/../../..") + "/chromedriver")
driver = None
def open_browser(voice_input):
    global driver
    if not driver:
        driver = webdriver.Chrome(service=service)
        driver.get('https://www.google.com/')


def searchGoogle(voice_input):
    global driver
    if not driver:
        open_browser(voice_input)
        driver.get('https://www.google.com/webhp?hl=uk&ictx=2&sa=X&ved=0ahUKEwi-7-GXl73-AhWpgf0HHbqKCRYQPQgJ')
        search = driver.find_element(By.NAME,'q')

        result = re.match(r'найди (.+)', voice_input)
        try:
            request = result.group(1)
            search.send_keys(request)
            search.submit()
            tts_engine.say(f'Вот результаты поиска по запросу {request}')
        except:
            pass

list_tolking.append(Tolking(
    ['найди'], searchGoogle
))
list_tolking.append(Tolking(
    ['браузер'], open_browser
))

def music(voice_input):
    global driver
    if not driver:
        open_browser(voice_input)
    voice_input = re.match('включи песню (.+)', voice_input).group(1)
    driver.get('https://open.spotify.com/search')
    search = driver.find_elements(By.CLASS_NAME, 'Type__TypeElement-sc-goli3j-0')[0]
    time.sleep(1)
    search.send_keys(voice_input)
    time.sleep(3)
    search = driver.find_elements(By.CLASS_NAME, 'gvLrgQXBFVW6m9MscfFA')[1]
    search.click()
    time.sleep(2)
    search = driver.find_elements(By.CLASS_NAME, 'ButtonInner-sc-14ud5tc-0')[3]
    search.click()
    time.sleep(5)
    button = driver.find_element(By.CLASS_NAME, 'eIvwKg')
    button.click()
    time.sleep(2)
    search = driver.find_element(By.ID, 'login-username')
    search.send_keys('clastbro22@gmail.com')
    search = driver.find_element(By.ID, 'login-password')
    search.send_keys('qwerty123456')
    time.sleep(2)
    search = driver.find_element(By.CLASS_NAME, 'encore-bright-accent-set')               
    search.click()      

list_tolking.append(Tolking(
    ['включи песню'], music
))