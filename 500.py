import json

from linebot import LineBotApi
from linebot.models import TextSendMessage

file = open('info.json','r')
info =json.load(file)

CHANNEL_ACCESS_TOKEN = info['CHANNEL_ACCESS_TOKEN']
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

def main():
    GROUP_ID = info['GROUP_ID']
    messages=TextSendMessage(text="お疲れ様です!!月初になりますので次来る時は500円玉の準備をしといてもらえると助かります！！")
    line_bot_api.push_message(GROUP_ID,messages=messages)
    
    
if __name__=="__main__":
    main()