#encoding=utf-8
import os
import requests
print('''1. 定义一个函数func(filename) filename:文件的路径
函数功能：打开文件，并且返回文件内容，最后关闭，用异常来处理可能发生的错误
code :
def func(filename):
    try:
        with open(filename,'r') as g:
            return g.read()
    except:
        print('open file:'+filename+' error')
result :''')
def func(filename):
    try:
        f = open(filename)
        return f.read()
    except Exception as err:
        return err
    finally:
        f.close()
print(func('/home/joker/code/python/FoundationTypes/info.txt'))
print('''2. 定义一个函数func(urllist)   urllist:为URL的列表，例如：["http://xx.com","http://www.xx.com","http://www.xxx.com"...]
函数功能：要求依次打开url，打印url对应的内容，如果有的url打不开，则把url记录到日志文件里，并且跳过继续访问下个url
code :
def get_url(urllist):
    for url in urllist:
        try:
            print(url)
            response=requests.get(url)
            html=response.content.decode('utf-8')
            response.close()
            print(html)
        except Exception as er:
            f = open('/home/joker/code/python/Exception/error.log', "a")
            f.write(url + '\r\n' + str(er) + '\r\n')
            print('error url: ', url)
            f.close()
result :''')
def get_url(urllist):
    for url in urllist:
        try:
            response=requests.get(url)
            html=response.content.decode('utf-8')
            response.close()
            print(html)
        except Exception as er:
            f = open('/home/joker/code/python/Exception/error.log', "a")
            f.write(url + '\r\n' + str(er) + '\r\n')
            print('error url: ', url)
            f.close()
url_list = ['http://www.xxx.com','www.qq.com']
# get_url(url_list)

print('''定义一个函数func(domainlist)   domainlist:为域名列表，例如：["xx.com","www.xx.com","www.xxx.com"...]
函数功能：要求依次ping 域名，如果ping 域名返回结果为：request time out，则把域名记录到日志文件里，并且跳过继续ping下个域名
code :
def pingDomain(domainlist):
    for domain in domainlist:
        try:
            os.system("ping "+domain+"  -n 1 -w 1 ")
        except Exception as er:
            f = open('/home/joker/code/python/Exception/error.log', "a")
            f.write(domain + '\r\n' + str(er) + '\r\n')
            print('error domain: ', domain)
            f.close()
pingDomain(['xx.com','www.xx.com','www.xxx.com'])
result :''')
def pingDomain(domainlist):
    for domain in domainlist:
        try:
            os.system("ping "+domain+"  -n 1 -w 1 ")
        except Exception as er:
            f = open('/home/joker/code/python/Exception/error.log', "a")
            f.write(domain + '\r\n' + str(er) + '\r\n')
            print('error domain: ', domain)
            f.close()
pingDomain(['xx.com','www.xx.com','www.xxx.com'])
