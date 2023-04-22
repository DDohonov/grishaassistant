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
driver = webdriver.Chrome(service=service)


def searchGoogle(voice_input):
    
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