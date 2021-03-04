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

def ifttt_webhoook(event_id):
	ifttt_url = 'https://maker.ifttt.com/trigger/'+event_id+'/with/key/'+IFTTT_KEY
	response = requests.post(ifttt_url)
	print(response)

# 必須ではないけれど、サーバに上がったとき確認するためにトップページを追加しておきます。
@app.route('/')
def top_page():
	return 'Here is root page.'

@app.route('/test1')
def test1():
	print("test1") 
	time.sleep(2)
	request.get('https://www.google.co.jp')
	print('fin1')

# ユーザがメッセージを送信したとき、この URL へアクセスが行われます。
@app.route('/callback', methods=['POST'])
def callback_post():
	if request.headers['test-Signature'] == 'abc':
		print('before')
		ifttt_webhoook(webhooks_test)

		
		return 'OK'

if __name__ == '__main__':
	app.run()
