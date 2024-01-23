# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 01:00:54 2024

@author: 86137
"""

from wenxin_llm import Wenxin_LLM  
from dotenv import load_dotenv  
import os  
  
# 加载环境变量  
# 注意：这里假设.env文件位于当前工作目录或项目根目录  
load_dotenv()  
  
try:  
    # 从环境变量中获取Wenxin API密钥和秘密密钥  
    wenxin_api_key = os.getenv("wenxin_api_key")  
    wenxin_secret_key = os.getenv("wenxin_secret_key")  
      
    # 检查密钥是否存在  
    if not wenxin_api_key or not wenxin_secret_key:  
        raise ValueError("Wenxin API key or secret key is missing from environment variables.")  
      
    # 创建Wenxin_LLM对象  
    llm = Wenxin_LLM(api_key=wenxin_api_key, secret_key=wenxin_secret_key)  
      
    # 调用LLM模型  
    # 注意：这里假设Wenxin_LLM对象是可调用的，且接受一个字符串参数  
    response = llm("你好")  
    print(response)  # 或者根据实际需要处理response  
      
except ValueError as e:  
    # 处理环境变量缺失的情况  
    print(f"An error occurred: {e}")  
except Exception as e:  # 捕获其他所有异常  
    # 处理其他异常情况  
    print(f"An unexpected error occurred: {e}")