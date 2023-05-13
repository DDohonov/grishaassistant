from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
import random
import os
from urllib.parse import urlencode
import random
from selenium.webdriver.common.action_chains import ActionChains
import random

service = Service(executable_path=os.path.abspath(__file__ + "/..") + "/chromedriver")
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(5)
# driver.set_page_load_timeout(5)

def registr():
    time.sleep(5)
    # driver.get('https://accounts.spotify.com/uk-UA/login?continue=https%3A%2F%2Fopen.spotify.com%2F')
    log_search = driver.find_element(By.TAG_NAME ,"input")
    log_search.send_keys('clastbro22@gmail.com')
    psw_search = driver.find_elements(By.TAG_NAME,"input")[1]
    psw_search.send_keys('qwerty123456')
    time.sleep(5)
    search = driver.find_element(By.CLASS_NAME, 'encore-bright-accent-set')
    search.click()

def andrew(voice_input):
    driver.get('https://1plus1.video/ru/playlist/serialy')
    time.sleep(3)
    search = random.choices(driver.find_elements(By.CLASS_NAME, 'poster-item-thumbnail'))
    search[0].click()
    # search.send_keys(voice_input)    driver.execute_script("window.scrollTo(0, -250);")
    time.sleep(4)
    search = driver.find_element(By.CLASS_NAME, "o-thumbnail")
    search.click()
    time.sleep(1)
    search = driver.find_elements(By.TAG_NAME, "button")[12]
    search.click()
andrew('qw')
# clastbro22@gmail.com
# qwerty123456


def olya(voice_input):
    driver.get('https://uakino.club/filmy/')
    search = driver.find_element(By.CLASS_NAME,'fa fa-play-circle go-watch')
    search.click()
    #search.send_keys(voice_input)
    search = driver.find_element(By.ID, '_atssh492')
    search.click
    #time.sleep(4)
    #search = driver.find_element(By.CLASS_NAME,'ScCoreLink-sc-16kq0mq-0 fQAQWb tw-link')
    #search.click()

   
    
def diana(voice_input):
    driver.get('https://kinozed.com')
    number = random.choice(driver.find_element(By.CLASS_NAME, 'short-title'))
    time.sleep(4)
    
    search = driver.find_element(By.CLASS_NAME, 'mask flex-col ps-link')
    search.click()
    time.sleep(3)

    search = driver.find_element(By.CLASS_NAME, 'go__link js-scroll__to')
    search.click()
    time.sleep(3)

    search = driver.find_element(By.CLASS_NAME, 'tabs-b video-box visible')
    search.click()
# diana('ee')

    #encore-bright-accent-set
def denisM(voice_input):
    driver.get('https://hd-rezka.pro/serialy/')
    serii = driver.find_elements(By.CLASS_NAME, 'short-title')
    choise = random.choice(serii)
    choise.click()
    time.sleep(3)
    knopka = driver.find_element(By.CLASS_NAME, 'button_1_nBS iconMD_2O8pO')
    choise.click()
    
#It will be worked!!!        
def art(voiceinput):
    driver.get('https://hd-rezka.biz/serialy/')
    time.sleep(2)
    x_button = driver.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/span')
    x_button.click()
    time.sleep(2)
    serial = driver.find_elements(By.CLASS_NAME, 'short-story')
    choise = random.choice(serial)
    choise.click()
    time.sleep(2)
    x_button = driver.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/span')
    x_button.click()    
    time.sleep(1)
    play_video = driver.find_element(By.CLASS_NAME, 'center_1Q6uP')
    play_video.click()
art('rrr')

def vanya(voice_input):
    driver.get('https://megogo.net/ru/series/main')
    search = random.choice(driver.find_element(By.CLASS_NAME,'promoSlide-poster entered loaded'))
    search.click()
    search = driver.find_element(By.CLASS_NAME,'loaded entered loading')
    
    
    
    
    


def danya(voice_input):
    driver.get("https://filmix.ac/random_serial")
    entrentr = driver.find_elements(By.CLASS_NAME, "name")[14]
    time.sleep(8)
    entrentr.click()
    # sksk = driver.send_keys(voice_input) 
    # sksk.submit()
    time.sleep(5)
    vidvid = driver.find_elements(By.CLASS_NAME, "fancybox")[1]
    vidvid.click()


def denisk(voice_input):
    driver.get('https://open.spotify.com/')
    search = driver.find_element(By.ID,"search")
    search.send_keys(voice_input)
    search.submit()

def maksg(voice_input):
    driver.get('https://hd-rezka.biz')
    search = driver.find_element(By.ID, 'search-input')
    search.click()
    search.send_keys()
    search.submit()





    