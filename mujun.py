#coding:utf-8
import OSC
import wn_hype
import cloud_vision
import sys
from microsofttranslator import Translator
#翻訳APIのセットアップ
translator = Translator("twitter_interaction","un+j9nSC3U4tTQvEZmcrj6lDAAc5tIjDqQMDnjwUakI=")
#OSCの初期設定
client = OSC.OSCClient()
msg = OSC.OSCMessage()
msg.setAddress("/words")

label = cloud_vision.get_label(sys.argv[1],sys.argv[2]) #引数で指定した画像を解析し、指定した番号のラベルを取得
print label
label_ja = translator.translate(label,"ja") #ラベルを日本語化
#print label_ja
words = wn_hype.abstract_word(label_ja) #ラベルの上位語の下位語をすべて取得
for abst_word in words:
    msg.append(abst_word.encode('utf_8'))
    #print '-', abst_word
client.sendto(msg, ('127.0.0.1', 8000))
