
import csv
import requests
from bs4 import BeautifulSoup

HEADER = ['打順', '守備位置', '選手名', '打', '打率']

url = 'https://2020.yahoo.co.jp/event/bb/genre/event-baseball/result/SFNL/detail/000100--/top'
res = requests.get(url)

soup = BeautifulSoup(res.text, 'html.parser')

player = {}
spot = soup.find_all('table', attrs={'class': 'bb-splitsTable'})[1].tbody
lists = spot.find_all('tr', attrs={'class': 'bb-splitsTable__row'})
with open('日本代表スタメン.csv', 'w', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(HEADER)
    for list in lists:
        list_texts = list.find_all('td', attrs={'class': 'bb-splitsTable__data'})
        order = list_texts[0].text
        position = list_texts[1].text
        player = list_texts[2].text.replace('\n', '')
        hit = list_texts[3].text
        average = list_texts[4].text.split('.')[1]
        
        row = [order, position, player, hit, average]
        writer.writerow(row)
        
        print(order)
        print(position)
        print(player)
        print(hit)
        print(average)
        print('----------------------')