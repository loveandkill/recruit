__author__ = 'xny'
# date : 2018/6/27
from bs4 import BeautifulSoup
import requests

url="http://127.0.0.1:8090/recruit.students/login/in?"
#把请求头信息进行处理，去掉一些没用的，保留一些有用头信息·
headers = {
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    "Referer": "http://127.0.0.1:8090/recruit.students/login/view",
  }
# URL参数
payload = {'account': 'admin','pwd':'660B8D2D5359FF6F94F8D3345698F88C'}
# 发送get请求
response = requests.get(url,headers = headers,params=payload)

# 查看响应内容，response.text 返回的是Unicode格式的数据
html=response.text
#创建 Beautiful Soup 对象
soup = BeautifulSoup(html,"lxml")
# 获取“退出登录”文本
info =soup.select('.toprighthref')[0].get_text()

#断言，检查客户端发送get请求结果是否符合预期。
try:
    assert info == "退出登录"
    print('-------pass--------')
except ValueError:
    print("------fail------")









