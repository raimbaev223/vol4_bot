import requests
from bs4 import BeautifulSoup
import json


def get_news():
    response = requests.get('https://kloop.kg/').text

    soup = BeautifulSoup(response, 'html.parser')
    posts = soup.find_all('a', class_='elementor-post__thumbnail__link')
    links = []
    for p in posts:
        href = p.get('href')
        links.append(href)
    return links


list_news = get_news()

# key = '80d0ef1fce9db7f5eb46fa8e2e442641'
# weather = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID={key}')
