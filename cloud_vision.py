#!/usr/bin/python
#coding:utf-8
import base64
import json
import time
import sys
from requests import Request, Session


# Cloud Vision APIで画像を分析
# CAPTCHAの分析
# CAPTCHA画像の読み込み
#bin_captcha = open('demo-image.jpg', 'rb').read()

# base64でCAPTCHA画像をエンコード
#str_encode_file = base64.b64encode(bin_captcha)

def get_label(filename, label_num):

    # APIのURLを指定
    str_url = "https://vision.googleapis.com/v1/images:annotate?key="

    # 事前に取得したAPIキー
    str_api_key = "AIzaSyAh5zYBWfiPMDnt8GFPEye8fImsP7JStFs"

    # Content-TypeをJSONに設定
    str_headers = {'Content-Type': 'application/json'}

    img = open(filename, 'rb').read()
    str_encode_file = base64.b64encode(img)#jpeg文字列からバイナリに変換

    # Cloud Vision APIの仕様に沿ってJSONのペイロードを定義。
    str_json_data = {
        'requests': [
                     {
                     'image': {
                     'content': str_encode_file
                     },
                     'features': [
                                  {
                                  'type': "LABEL_DETECTION",
                                  'maxResults': 10
                                  }
                                  ]
                     }
                     ]
                     }

    # リクエスト送信
    obj_session = Session()
    obj_request = Request("POST",str_url + str_api_key,
                                      data=json.dumps(str_json_data),
                                      headers=str_headers
                                      )
    obj_prepped = obj_session.prepare_request(obj_request)
    obj_response = obj_session.send(obj_prepped,verify=True,timeout=60)

    # 分析結果の取得
    #if obj_response.status_code == 200:
    #print obj_response.text
    jsonData = json.loads(obj_response.text)
    param = jsonData["responses"][0]["labelAnnotations"][int(label_num)]["description"]
    return param

if __name__ == "__main__":
    label = get_label(sys.argv[1])
    print label
