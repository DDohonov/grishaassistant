from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
import os


service = Service(executable_path=os.path.abspath(__file__ + "/..") + "/chromedriver")
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(5)


def andrew(voice_input):
    driver.get('https://drivemusic.club/best_music.html')
    search =  driver.find_element(By.ID, 'form-search')
    search.click()
    search.send_keys(voice_input)
    search.submit()
    search = driver.find_element(By.CLASS_NAME, 'btn_player')
    search.click()
andrew('rock')




def olya(voice_input):
    driver.get('https://music.youtube.com/')
    search = driver.find_element(By.ID,'icon')
    search.click()
    time.sleep(4)
    search = driver.find_element(By.CSS_SELECTOR,'.search-box input')
    
    search.send_keys(voice_input)
    time.sleep(4)
    search.send_keys(Keys.ENTER)
    time.sleep(4)
    video = driver.find_elements(By.TAG_NAME,'ytmusic-play-button-renderer')[1]
    print(video)
    video.click()

    
def diana(voice_input):
    driver.get('https://sefon.pro/search/')
    search =  driver.find_element(By.NAME, 'q')
    search.send_keys(voice_input)
    search.submit()
    button1 = driver.find_element(By.CLASS_NAME, 'btn play')
    button1.click()


    
def denisM(voice_input):
    pass

    

    
# rock
def art(voice_input):
    driver.get("https://music.youtube.com/moods_and_genres")
    search = driver.find_element(By.CLASS_NAME, 'style-scope ytmusic-grid-renderer')[44]
    search.click()
    play_search = driver.find_element(By.CLASS_NAME, 'style-scope ytmusic-carousel')[19]
    play_search.click()


def vanya(voice_input):
    driver.get('https://music.youtube.com')
    search = driver.find_element(By.ID, 'placeholder')
    search.click()
    time.sleep(3.0)
    # search = driver.find_element(By.)
    search.send_keys(voice_input)
    search.submit()
      
def danya(voice_input):
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com/")
    search_box = driver.find_element_by_name("search_query")
    search_box.send_keys("бах")
    search_box.submit()
    first_video = driver.find_element(By.CSS_SELECTOR, "#contents > ytd-video-renderer:nth-child(1) > div > div > div > div > h3 > a")
    first_video.click()


    
def denisk(voice_input):
    driver.get('https://open.spotify.com/')
    search = driver.find_element(By.ID,"search")
    search.send_keys(voice_input)
    search.submit()

def maksg(voice_input):
    driver.get('https://music.youtube.com')
    search = driver.find_element(By.ID, 'search')
    search.send_keys(voice_input)
    search.submit()
    



    