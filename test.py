from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
import random
import os
import random
from selenium.webdriver.common.action_chains import ActionChains
import random


service = Service(executable_path=os.path.abspath(__file__ + "/..") + "/chromedriver")
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(5)

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
    driver.get('https://rezka.ag/series/')
    time.sleep(3)
    search = random.choices(driver.find_elements(By.CLASS_NAME, 'b-content__inline_item-cover'))
    search.click()
    time.sleep(3)
    # search.send_keys(voice_input)    driver.execute_script("window.scrollTo(0, -250);")
    time.sleep(1)
    search = driver.find_element(By.TAG_NAME, "video")
    search.click()
    time.sleep(1)
    search = driver.find_element(By.ID, "fullscreen13")
    search.click()
# andrew('qw')
# clastbro22@gmail.com
# qwerty123456


def olya(voice_input):
    driver.get('https://uakino.club/filmy/')
    search = driver.find_element(By.CLASS_NAME,'fa fa-play-circle go-watch')
    search.click()
    #search.send_keys(voice_input)
    search = driverfind_element(By.ID, '_atssh492')
    search.click
    #time.sleep(4)
    #search = driver.find_element(By.CLASS_NAME,'ScCoreLink-sc-16kq0mq-0 fQAQWb tw-link')
    #search.click()

   
    
def diana(voice_input):
    driver.get('https://rezka.ag/?filter=last&genre=1')
    number = random.randint(53553, 57253)
    search = driver.find_element(By.ID, number)
    search.click()


    #encore-bright-accent-set
def denisM(voice_input):
    driver.get('https://rezka.ag/series/best/')
    search = driver.find_elements(By.ID, 'search-field')[2]
    time.sleep(2)
    serii = driver.find_element(By.CLASS_NAME, 'b-content__inline_item-link')
    
def art(voiceinput):
    driver.page_load_strategy = 'none'
    driver.get('https://rezka.ag/series/')
    time.sleep(1)
    time.sleep(2)
    driver.stop()
    serial = driver.find_elements(By.CLASS_NAME, 'b-content__inline_item-cover')
    choise = random.choice(serial)
    choise.click()
art('rrr')
def vanya(voice_input):
    driver.get('https://rezka.ag/ps:/ww')
    search = driver.find_element(By.CLASS_NAME, 'b-search__submit')
    search.click()
    


def danya(voice_input):
    driver.get("hhttps://rezka.ag/ssereriebs/be2st/2022/")
    entrentr = driver.find_element(By.ID, "")
    entrentr.click() 
    sksk = driver.send_keys(voice_input) 
    sksk.submit()
    vidvid = driver.find_elements(By.CLASS_NAME, "")[1]
    vidvid.click()


def denisk(voice_input):
    driver.get('https://open.spotify.com/')
    search = driver.find_element(By.ID,"search")
    search.send_keys(voice_input)
    search.submit()

def maksg(voice_input):
    driver.get('https://www.youtube.com')
    search = driver.find_element(By.ID, 'search-input')
    search.click()
    search.send_keys()
    search.submit()





    