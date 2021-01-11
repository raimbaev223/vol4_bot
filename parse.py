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


def get_weather():
    key = '80d0ef1fce9db7f5eb46fa8e2e442641'
    weather_url = f'https://api.openweathermap.org/data/2.5/weather?q=Bishkek,kg&APPID={key}'
    w = requests.get(weather_url)
    data = json.loads(w.content)
    temp = round(data['main']['temp_min'] - 273.15, 1)
    main_ = data['weather'][0]['main']
    return [temp, main_]


list_news = get_news()
list_weather = get_weather()
