from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
import os
from selenium.webdriver.common.action_chains import ActionChains


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
    driver.get('https://open.spotify.com/search')
    time.sleep(5)
    search =  driver.find_element(By.TAG_NAME, 'input')
    search.click()
    search.send_keys(voice_input)
    search.submit()
    time.sleep(5)
    search = driver.find_element(By.CLASS_NAME, '_gB1lxCfXeR8_Wze5Cx9')
    search.click()
    time.sleep(5)
    search = driver.find_elements(By.CLASS_NAME, 'PFgcCoJSWC3KjhZxHDYH')[1]
    search.click()
    time.sleep(5)
    search = driver.find_element(By.CLASS_NAME, 'eIvwKg')
    search.click()
    registr()
andrew('rock')
# clastbro22@gmail.com
# qwerty123456


def olya(voice_input):
    driver.get('https://open.spotify.com/')
    search = driver.find_element(By.CLASS_NAME,'Type__TypeElement-sc-goli3j-0 bNyYSN QO9loc33XC50mMRUCIvf')
    search.click()
    search.send_keys(voice_input)
    search.submit()
    time.sleep(4)
    search = driver.find_element(By.CLASS_NAME,'Type__TypeElement-sc-goli3j-0 gYqKuy t_yrXoUO3qGsJS4Y6iXX standalone-ellipsis-one-line')
    search.click()
   
   
    
def diana(voice_input):
    driver.get('https://open.spotify.com')
    search =  driver.find_element(By.ID, 'buttonPrimary')
    search.send_keys(Keys.ENTER)
    time.sleep(5)
    
    user = driver.find_element(By.ID, 'login-username')
    user.send_keys('clastbro22@gmail.com')
    user.submit()
    time.sleep(5)
    
    password = driver.find_element(By.ID, 'login-password')
    password.send_keys('qwerty123456')
    password.submit()
    time.sleep(5)
    
    entrance = driver.find_element(By.ID, 'type')
    entrance.click()
    time.sleep(5)
    
    search1 = driver.find_element(By.CLASS_NAME, 'Type__TypeElement-sc-goli3j-0 jqNXli ellipsis-one-line')
    search1.click()
    time.sleep(5)

    search2 = driver.find_element(By.CLASS_NAME, 't2K4_iLmAyDtH7mcT5Wy')
    search2.send_keys('Rock')
    search2.submit()
    


    #encore-bright-accent-set
def denisM(voice_input):
    driver.get('https://open.spotify.com/search')
    search = driver.find_elements(By.CLASS_NAME, 'Type__TypeElement-sc-goli3j-0')[0]
    time.sleep(1)
    search.send_keys('Rock')
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

    
# rock
def art(voice_input):
    driver.get('https://open.spotify.com/search')
    time.sleep(3)
    search =  driver.find_element(By.TAG_NAME, 'input')
    search.click()
    search.send_keys(voice_input)
    search.submit()


def vanya(voice_input):
    driver.get('https://open.spotify.com')
    search = driver.find_element(By.CLASS_NAME, 'link-subtle UYeKN11KAw61rZoyjcgZ')
    search.click()
    time.sleep(3)
    search.send_keys(voice_input)
    search.submit()
    time.sleep(3)
    search.driver.find_element(By.CLASS_NAME,'_gB1lxCfXeR8_Wze5Cx9')
    search.click()
    time.sleep(3)
    search.driver.find_element(By.CLASS_NAME, 'ButtonInner-sc-14ud5tc-0 fipMme encore-bright-accent-set')
    search.click()
    
      
def danya(voice_input):
    driver.get("https://open.spotify.com/search")
    entr = driver.find_element(By.CLASS_NAME,"ButtonInner-sc-14ud5tc-0 iIKcFo encore-inverted-light-set")
    time.sleep(6)
    entr.click()
    entr2 = driver.find_element(By.CLASS_NAME, "Input-sc-1gbx9xe-0 eRUvFB")
    time.sleep(6)
    entr2.click()
    time.sleep(2.5)
    entr2.send_keys("clastbro22@gmail.com")
    entr3 = driver.find_element(By.CLASS_NAME, "Input-sc-1gbx9xe-0 fOpTaL")
    time.sleep(6)
    entr3.click()
    time.sleep(2.5)
    entr3.send_keys("qwerty123456")
    entr4 = driver.find_element(By.CLASS_NAME, "Type__TypeElement-sc-goli3j-0 kwLSIj sc-eDvSVe itlAHd")
    entr4.click()
    
def denisk(voice_input):
    driver.get('https://open.spotify.com/')
    search = driver.find_element(By.ID,"search")
    search.send_keys(voice_input)
    search.submit()

def maksg(voice_input):
    driver.get('https://open.spotify.com')
    search = driver.find_element(By.CLASS_NAME, 'Type__TypeElement-sc-goli3j-0 jqNXli ellipsis-one-line')
    search.click
    search.send_keys()
    search = driver.find_element(By.CLASS_NAME, '')
    search.submit()
    



    