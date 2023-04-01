import requests
from bs4 import BeautifulSoup


def andrew(voice_input):
    result = requests.get("https://rezka.ag/", headers={'Accept': '*/*', 'User-Agent': 'a'})
    soup = BeautifulSoup(result.text, 'html.parser')
    sss = soup.find('div', class_="b-content__inline_item-link")


def olya(voice_input):
    result = requests.get("https://rezka.ag/?filter=watching&genre=2")
    soup = BeautifulSoup(result.text, 'html.parser')
    sereals = soup.find('div', class_="b-content__inline_item-link")
    print(sereals.text)

def diana(voice_input):
    result = requests.get("https://rezka.ag/series/fantasy/1749-sverhestestvennoe-2005.html")
    soup = BeautifulSoup(result.text, 'html.parser')
    name = soup.find('div', class_="b-post__title")
    year = soup.find('a', href="https://rezka.ag/year/2005/") 
    print(name.next_element.text)
    print(year.text)

def art():
    result = requests.get("https://rezka.ag/series/", headers = {'Accept': '*/*', 'User-Agent': 'pon'})
    soup = BeautifulSoup(result.text, 'html.parser')
    name = soup.find('div', class_='b-content__inline_item-link').find('a').text
    god = soup.find('div', class_='b-content__inline_item-link').find('div').text
    print(name)
    print(god)
    
def denisM(voice_input):
    result = requests.get('b-content__inline_item-link')
    soup = BeautifulSoup(result.text, 'html.parser')
    nazvanie = soup.find('div', class_ = 'b-post__title').text

def art(voice_input):
    res = requests.get('https://www.unian.ua/?utm_source=siteua&utm_medium=siteua&utm_campaign=siteua')
    soup = BeautifulSoup(res.text, 'html.parser')
    
    capt = soup.find('a', class_ = 'main-unit__title').text
    
    print(capt)
      

def vanya(voice_input):
    result = requests.get('https://rezka.ag/?filter=watching&genre=2')  
    soup = BeautifulSoup(result.text, 'html.parser')
    name = soup.find('div', class_= 'b-content')
      
def danya(voice_input):
    response = requests.get("https://rezka.ag/?filter=watching&genre=2",{'Accept': '*/*', 'User-Agent': 'a'})
    soup = BeautifulSoup(response.text,"html.parser")
    now_watching = soup.find('a',class_ = 'b-content__main_filters_link active')
    first = soup.find('div', class_ = 'b-content__inline_item-link')
    print(now_watching.text)
    print(first.text)



def denisk(voice_input):
    result = requests.get('https://rezka.ag/?filter=watching&genre=2')
    # soup = BeautifulSoup(response.text,'html.parser')
    # a = sop.find('div',class = )
 
    



    