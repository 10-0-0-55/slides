# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup

headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'}#浏览器代理

def  getHTMLText(url):
    try:
        #print(url)
        r = requests.get( url,headers = headers )
        #print(r)
        r.encoding = 'utf-8'
        return r.text
    except:
        return "错误"

url = 'http://www.baidu.com'
txt = getHTMLText(url)
#print txt
soup = BeautifulSoup(txt,"html.parser")
print soup.p
