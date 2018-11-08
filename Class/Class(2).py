#encoding=utf-8
import urllib
import requests
from bs4 import BeautifulSoup
print(''' 写一个网页数据操作类。完成下面的功能：
提示：需要用到urllib模块
get_httpcode()获取网页的状态码，返回结果例如：200,301,404等 类型为int
get_htmlcontent() 获取网页的内容。返回类型:str
get_linknum()计算网页的链接数目
code :
class web(object):
    def get_httpcode(self,url):
        status=requests.get(url).status_code
        return status
    def get_htmlcontent(self,url):
        response=requests.get(url)
        html=response.content.decode('utf-8')
        response.close()
        return html
    def get_linknum(self,url):
        result=[]
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')
        for a in soup.find_all('a'):
            result.append(a['href'])
        return result
baidu=web()
print(baidu.get_httpcode('http://www.baidu.com'))
print(baidu.get_htmlcontent('http://www.baidu.com'))
print(baidu.get_linknum('http://www.baidu.com'))
result :''')
class web(object):
    def get_httpcode(self,url):
        status=requests.get(url).status_code
        return status
    def get_htmlcontent(self,url):
        response=requests.get(url)
        html=response.content.decode('utf-8')
        response.close()
        return html
    def get_linknum(self,url):
        result=[]
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')
        for a in soup.find_all('a'):
            result.append(a['href'])
        return result
baidu=web()
print(baidu.get_httpcode('http://www.baidu.com'))
print(baidu.get_htmlcontent('http://www.baidu.com'))
print(baidu.get_linknum('http://www.baidu.com'))
