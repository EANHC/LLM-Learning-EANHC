# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 00:44:12 2024

@author: 86137
"""

from wenxin_llm import Wenxin_LLM

from dotenv import find_dotenv, load_dotenv
import os

# 读取本地/项目的环境变量。

# find_dotenv()寻找并定位.env文件的路径
# load_dotenv()读取该.env文件，并将其中的环境变量加载到当前的运行环境中
# 如果你设置的是全局的环境变量，这行代码则没有任何作用。
_ = load_dotenv(find_dotenv())

# 获取环境变量 OPENAI_API_KEY
wenxin_api_key = os.environ["wenxin_api_key"]
wenxin_secret_key = os.environ["wenxin_secret_key"]
llm = Wenxin_LLM(api_key=wenxin_api_key, secret_key=wenxin_secret_key)
llm("你好")