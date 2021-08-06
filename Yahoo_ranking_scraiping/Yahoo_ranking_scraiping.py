import csv
import requests
from bs4 import BeautifulSoup

HEADER = ['ニューステキスト', 'URL']

url = 'https://sports.yahoo.co.jp/'
res = requests.get(url)

soup = BeautifulSoup(res.text, 'html.parser')

pick_up = soup.find('ul', attrs={'id': 'pickup'})

data = []
many_news = pick_up.find_all('li', attrs={'class': 'sn-listPickup__item'})
with open('ピックアップニュース取得.csv', 'w', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(HEADER)
    for news in many_news:
        news_text = news.find('a', attrs={'class': 'sn-listPickup__link'}).text
        news_url = news.find('a', attrs={'class': 'sn-listPickup__link'})['href']

        row = [news_text, news_url]
        writer.writerow(row)