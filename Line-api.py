import requests
import datetime
import pytz


# 取得したトークン
TOKEN = '17d7hPD86qomrLYvVeiqHkEpQlhMbKucbEw4M4ilte4'

# APIのURL
api_url = 'https://notify-api.line.me/api/notify'

# 通知内容
send_contents = '中村芽衣です'

# 情報を辞書型にする
TOKEN_dic = {'Authorization': 'Bearer' + ' ' + TOKEN}
send_dic = {'message': send_contents}
print(TOKEN_dic)
print(send_dic)

# requests.post(api_url, headers=TOKEN_dic, data=send_dic)

# 画像ファイルの指定
image_file = './img/img1.jpg'

# バイナリデータで読み込む
binary = open(image_file, mode='rb')

# 指定の辞書型にする
image_dic = {'imageFile': binary}

# lineに画像とメッセージを送る
requests.post(api_url, headers=TOKEN_dic, data=send_dic, files=image_dic)

# 時間
time = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
time = time.strftime('%Y年%m月%d日 %H:%M:%S')
print(time)