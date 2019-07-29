__author__ = 'Administrator'
__author__ = 'xny'
# date : 2018/6/28
import requests
import json
from urllib import parse

import requests
# 第一步：登录教育局招生管理系统
url_login="http://127.0.0.1:8090/recruit.students/login/in?account=admin&pwd=660B8D2D5359FF6F94F8D3345698F88C"
#把请求头信息进行处理，去掉一些没用的，保留一些有用头信息·
headers1 = {
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    "Referer": "http://127.0.0.1:8090/recruit.students/login/view",
  }

# 发送get请求
r1 = requests.get(url_login,headers = headers1)
#print(r1.text)

# 禁用学校
url_DisableSchool="http://127.0.0.1:8090/recruit.students/school/manage/enableOrDisableSchool"
#把请求头信息进行处理，去掉一些没用的，保留一些有用头信息·
headers2 = {""
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:62.0) Gecko/20100101 Firefox/62.0",
"Referer": "http://127.0.0.1:8090/recruit.students/school/manage/index",
"Content-Type": "application/json",
"X-Requested-With": "XMLHttpRequest",
"Content-Length": "46",
"Cookie": "JSESSIONID=09CD90A3357DEBD4F3B0F2CF3B387DCA",
"Connection": "keep-alive",
}
# 接口的数据类型是json格式
formdata = {"id":"820890","disable":0,"schoolId":"251"}
# 通过urlencode()转码
postdata = parse.urlencode(formdata)
#打印转码后的数据
print(postdata)
# 创建session对象，可以保存登录Cookie值。
ssion = requests.session()

# 发送附带用户名和密码的请求，并获取登录后的Cookie值，保存在ssion里。
r2 = ssion.post(url_DisableSchool,headers = headers2,data=postdata)
html = r2.text
print(html)

# 查看响应码
print(r2.status_code)
