import requests
from bs4 import BeautifulSoup

url = 'https://scraping-for-beginner.herokuapp.com/udemy'
res = requests.get(url)

# html取得
soup = BeautifulSoup(res.text, 'html.parser')

# 受講生の数
subscribers = soup.find_all('p', attrs={'class': 'subscribers'})[0]
n_subscribers = subscribers.text.split('：')[1]
print(n_subscribers)

# レビューの数
reviews = soup.find_all('p', attrs={'class': 'reviews'})[0]
n_reviews = reviews.text.split('：')[1]
print(n_reviews)