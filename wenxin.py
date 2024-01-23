# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 23:23:33 2024

@author: 86137
"""

import requests  
import json  
  
def get_access_token():  
    """  
    使用 API Key，Secret Key 获取access_token，替换下列示例中的应用API Key、应用Secret Key  
    """  
    url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=MKFKszGo4iWDyEVGLKByI8YR&client_secret=8LNpGgE0LR0G15HFBGgOVLoajVdRedl1"  
    payload = {}  
    headers = {  
        'Content-Type': 'application/json',  
        'Accept': 'application/json'  
    }  
    try:  
        response = requests.request("POST", url, headers=headers, data=payload)  
        response.raise_for_status()  # 如果不是200-399的HTTP状态码，将引发HTTPError异常  
        return response.json().get("access_token")  
    except requests.RequestException as e:  
        print(f"Error occurred while getting access token: {e}")  
        return None  
  
access_token = get_access_token()  
if access_token is None:  
    print("Failed to get access token.")  
else:  
    print(f"Access token: {access_token}")  
  
def get_wenxin(prompt):  
    url = f"https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/eb-instant?access_token={access_token}"  
    payload = {  
        "messages": [  
            {  
                "role": "user",  
                "content": prompt  
            }  
        ]  
    }  
    headers = {  
        'Content-Type': 'application/json'  
    }  
    try:  
        response = requests.request("POST", url, headers=headers, data=json.dumps(payload))  
        response.raise_for_status()  # 如果不是200-399的HTTP状态码，将引发HTTPError异常  
        js = response.json()  
        print(js.get("result"))  
    except requests.RequestException as e:  
        print(f"Error occurred while getting Wenxin response: {e}")  
  
get_wenxin("你好")
-