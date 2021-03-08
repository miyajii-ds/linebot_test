from flask import Flask, request, abort

# 環境変数取得のため。
import os

# ログを出力するため。
#import logging
#import sys

import requests
import time

app = Flask(__name__)


# 大事な情報は環境変数から取得。
IFTTT_KEY = os.environ['IFTTT_KEY']
flag = 0
light_flag = False
print(flag)

def ifttt_webhoook(event_id):
	ifttt_url = 'https://maker.ifttt.com/trigger/'+event_id+'/with/key/'+IFTTT_KEY
	response = requests.post(ifttt_url)
	print(response)

# 必須ではないけれど、サーバに上がったとき確認するためにトップページを追加しておきます。
@app.route('/')
def top_page():
	return 'Here is root page.'


@app.route('/ratoc-sensor', methods=['POST'])
def ratoc_sensor():
	global light_flag
	illumi = request.json
	data = request.get_data()
	print('illumi'+str(illumi))
	print('data:'+str(data))
	#illumi = data['illuminance']
	print(illumi["illuminance"])
	print(illumi['illuminance'])
	print(type(illumi))
	return 'ratoc'

# ユーザがメッセージを送信したとき、この URL へアクセスが行われます。
@app.route('/count', methods=['POST'])
def count_post():
	global flag
	print('before')
	ifttt_webhoook('webhooks_test')
	flag += 1
	
	header = request.headers
	print(header)
	data = request.get_data()
	print(data)
	
	print('flag:'+str(flag))
	return 'OK'
	
	
# ユーザがメッセージを送信したとき、この URL へアクセスが行われます。
@app.route('/callback', methods=['POST'])
def callback_post():
	global flag
	print('before')
	if flag >= 3:
		ifttt_webhoook('webhooks_test')
		flag = 0
		print(flag)
	
	
	print('flag:'+str(flag))
	return 'OK'

if __name__ == '__main__':
	app.run()
