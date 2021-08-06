from typing import BinaryIO
import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import pandas as pd


browser = webdriver.Chrome()
browser.get('https://scraping-for-beginner.herokuapp.com/login_page')

# ユーザーネーム
elem_username =  browser.find_element_by_id('username')
elem_username.send_keys('imanishi')

# パスワード
elem_password = browser.find_element_by_id('password')
elem_password.send_keys('kohei')

# ログインボタンクリック
elem_login_btn = browser.find_element_by_id('login-btn')
elem_login_btn.click()

# 一括取得
elems_th = browser.find_elements_by_tag_name('th')
keys = []

for elem_th in elems_th:
  key = elem_th.text
  print(key)
  keys.append(key)
  
elems_td = browser.find_elements_by_tag_name('td')
values = []

for elem_td in elems_td:
  value = elem_td.text
  print(value)
  values.append(value)
  
df = pd.DataFrame()
df['項目'] = keys
df['値'] = values

df.to_csv('講師情報.csv', index=False)

browser.quit()