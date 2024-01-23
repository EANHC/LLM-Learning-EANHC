# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 20:14:40 2024

@author: 86137
"""

import SparkApi
#以下密钥信息从控制台获取
appid = "239dc1f3"     #填写控制台中获取的 APPID 信息
api_secret = "YjJhMDBlODg5ZDRjZDc2ZWI2YTNlODFj"   #填写控制台中获取的 APISecret 信息
api_key ="55bae99c9fd7bfe36b8b3dbc715ce525"    #填写控制台中获取的 APIKey 信息

#用于配置大模型版本，默认“general/generalv2”
domain = "general"   # v1.5版本
# domain = "generalv2"    # v2.0版本

#云端环境的服务地址
Spark_url = "ws://spark-api.xf-yun.com/v1.1/chat"  # v1.5环境的地址
# Spark_url = "ws://spark-api.xf-yun.com/v2.1/chat"  # v2.0环境的地址

def getText(role, content, text = []):
    # role 是指定角色，content 是 prompt 内容
    jsoncon = {}
    jsoncon["role"] = role
    jsoncon["content"] = content
    text.append(jsoncon)
    return text

text1=f"""今天我和月月鸟、土狗、吗喽、lzy打了绵阳换三张麻将，然后排队等了很久，吃了六月雪干锅，出来之后路过了霸王茶姬店和七彩豆豆礼品店，逛了装修之后的马家巷，最后我坐公交车回家了"""


prompt1 = f"""
帮我对用“```”分隔的语句，进行一个实体识别，找出句子中的人物地点事件时间天气情感等存在的元素，如果没有的话就回复无，你要注意事件应该包含全面，事件中也可能隐含地点

句子：
```{text1}```

"""

question1 = getText("user", prompt1)

response1 = SparkApi.main(appid,api_key,api_secret,Spark_url,domain,question1)
response1


print("\n")

text2=f"""今天我和月月鸟、土狗、吗喽、lzy打了绵阳换三张麻将，然后排队等了很久，吃了六月雪干锅，出来之后路过了霸王茶姬店和七彩豆豆礼品店，逛了装修之后的马家巷，最后我坐公交车回家了"""


prompt2 = f"""
帮我对用“```”分隔的语句，进行一个词性标注，用中文标注词性，标注内容用括号括起来,括号里直接是中文词性

句子：
```{text2}```

"""

question2 = getText("user", prompt2)

response2 = SparkApi.main(appid,api_key,api_secret,Spark_url,domain,question2)
response2







