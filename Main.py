import json

from linebot import LineBotApi
from linebot.models import TextSendMessage

file = open('info.json','r')
info =json.load(file)