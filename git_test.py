from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

# 環境変数取得のため。
import os

# ログを出力するため。
import logging
import sys

import requests

app = Flask(__name__)

# ログを標準出力へ。heroku logs --tail で確認するためです。
# app.logger.info で出力するため、レベルは INFO にする。
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.INFO)

# 大事な情報は環境変数から取得。
CHANNEL_ACCESS_TOKEN = os.environ['CHANNEL_ACCESS_TOKEN']
CHANNEL_SECRET = os.environ['CHANNEL_SECRET']
IFTTT_KEY = os.environ['IFTTT_KEY']

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)


def ifttt_webhoook(event_id):
	ifttt_url = 'https://maker.ifttt.com/trigger/'+event_id+'/with/key/'+IFTTT_KEY
	
	response = requests.post(ifttt_url)




# 必須ではないけれど、サーバに上がったとき確認するためにトップページを追加しておきます。
@app.route('/')
def top_page():
    return 'Here is root page.'


# ユーザがメッセージを送信したとき、この URL へアクセスが行われます。
@app.route('/callback', methods=['POST'])
def callback_post():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info('Request body: ' + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def reply_message(event):
    # reply のテスト。
    if event.message.text in ['リビング照明 ON/OFF']:
        ifttt_webhoook('Go_work')
        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text+'しました。'))

    if event.message.text in 'TV ON/OFF':
        ifttt_webhoook('webhooks_test')
        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text+'しました。'))
        
    if event.message.text in 'エアコン ON/OFF':
        ifttt_webhoook('Aircon')
        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text+'しました。'))




if __name__ == '__main__':
    app.run()
