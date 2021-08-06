import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

options = Options()
options.add_argument('--headless')


# 指定のURLにアクセス
browser = webdriver.Chrome(options=options)
url = 'https://scraping-for-beginner.herokuapp.com/login_page'
browser.get(url)

sleep(2)

# ユーザーネーム
elem_username =  browser.find_element_by_id('username')
elem_username.send_keys('imanishi')

# パスワード
elem_password = browser.find_element_by_id('password')
elem_password.send_keys('kohei')

# ログインボタンクリック
elem_login_btn = browser.find_element_by_id('login-btn')
elem_login_btn.click()
browser.quit()