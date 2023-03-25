from response.main import *
from bs4 import BeautifulSoup
import requests

def currency(voice_input):
    result = requests.get("https://minfin.com.ua/ua/currency/")

    currency_dict = {
        'доллара': 0,
        "евро": 1,
        "польской злоты": 2,
        "фунта": 3,
        "франка": 4
    }

    soup = BeautifulSoup(result.text, 'html.parser')
    for i in currency_dict.keys():
        if i in voice_input:
            course = soup.find_all("td", {'data-title':'Середній курс в банках'})[currency_dict[i]].text.split('\n')
            tts_engine.say(f'Средний курс {i} в банках: Продажа - {course[1]} Покупка{course[6]}')

list_tolking.append(Tolking(
    ['какой курс'], currency
))