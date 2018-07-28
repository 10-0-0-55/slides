import requests
url = 'http://www.baidu.com'
r = requests.get( url )
'''
如果需要加headers：
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'}#浏览器代理
r = requests.get( url, headers = headers )
'''
print(r.status_code)  # 打印状态码
print(r.url)          # 打印请求url
print(r.headers)      # 打印头信息
print(r.cookies)      # 打印cookie信息
print(r.text)  #以文本形式打印网页源码
print(r.content) #以字节流形式打印
