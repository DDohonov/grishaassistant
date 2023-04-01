import requests
from bs4 import BeautifulSoup


result = requests.get("https://rezka.ag/?filter=watching&genre=2", headers={'Accept': '*/*', 'User-Agent': 'a'})
soup = BeautifulSoup(result.text, 'html.parser')
name = soup.find('div', {'class': 'b-content__inline_item-link'}).text
print(name.split(',')[0])