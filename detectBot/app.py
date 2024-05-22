import sys
import configparser

# Azure Text Analytics
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient
#

from flask import Flask, request, abort
from linebot.v3 import (
    WebhookHandler
)
from linebot.v3.exceptions import (
    InvalidSignatureError
)
from linebot.v3.webhooks import (
    MessageEvent,
    TextMessageContent,
)
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    ReplyMessageRequest,
    TextMessage
)

#Config Parser
config = configparser.ConfigParser()
config.read('config.ini')

#Config Azure Analytics
credential = AzureKeyCredential(config['AzureLanguage']['API_KEY'])
#

app = Flask(__name__)

channel_access_token = config['Line']['CHANNEL_ACCESS_TOKEN']
channel_secret = config['Line']['CHANNEL_SECRET']
if channel_secret is None:
    print('Specify LINE_CHANNEL_SECRET as environment variable.')
    sys.exit(1)
if channel_access_token is None:
    print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
    sys.exit(1)

handler = WebhookHandler(channel_secret)

configuration = Configuration(
    access_token=channel_access_token
)

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessageContent)
def message_text(event):
    output = random_line()####
        
    # temp , point , key_text= azure_sentiment(event.message.text)
    # if temp == 'positive':
    #     text = '正面。'
    # elif temp == 'neutral':
    #     text = '中性。'
    # elif temp == 'negative':
    #     text = '負面。'
    # output = f"{text}分數：{point} 主詞：{key_text}"
    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        line_bot_api.reply_message_with_http_info(
            ReplyMessageRequest(
                reply_token=event.reply_token,
                messages=[TextMessage(text=output)]
            )
        )
def azure_sentiment(user_input):
    text_analytics_client = TextAnalyticsClient(
        endpoint=config['AzureLanguage']['END_POINT'], 
        credential=credential)
    documents = [user_input]
    response = text_analytics_client.analyze_sentiment(
        documents, 
        show_opinion_mining=True,
        language="zh-hant")
    # print("*")
    print(response)
    try:
        key_text = response[0].sentences[0].mined_opinions[0].target.text
    except:
        key_text = '沒有主詞'
    highest_sentiment = max(response[0].sentences[0].confidence_scores.__dict__.values())

    # print("*")
    docs = [doc for doc in response if not doc.is_error]
    for idx, doc in enumerate(docs):
        print(f"Document text : {documents[idx]}")
        print(f"Overall sentiment : {doc.sentiment}")
    return docs[0].sentiment,highest_sentiment,key_text

import random
def random_line():
    lines = [
        "我很煩，對吧？",
        "如果我不在，你一定很輕鬆吧",
        "算了，沒事",
        "你變了",
        "都我錯",
        "反正我也不重要",
        "早知道就不說了",
        "我都是為你好",
        "一定是我不夠好，讓你沒有那麼喜歡我了",
        "你既然口口聲聲說愛我，那為什麼不相信我？",
        "我為這份感情付出這麼多，而我就這麼求你一次",
        "我都已經道歉了，你還想要我怎樣？",
        "情人節你如果想跟朋友一起過可以啊，但我比較喜歡我們單獨過，但看你啦",
        "我可沒說一定要過情人節",
        "禮物是我逼你送的嗎？",
        "不要說得好像是我一個人想過情人節",
        "我沒有在對你情勒哦"
    ]
    return random.choice(lines)

if __name__ == "__main__":
    app.run()