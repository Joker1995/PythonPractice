#encoding=utf-8
import urllib.request
print ('1. 定义一个方法get_num(num),num参数是列表类型，判断列表里面的元素为数字类型。'\
'其他类型则报错，并且返回一个偶数列表：（注：列表里面的元素为偶数）')
code ='''code :
def get_num(num):
    if type(num)!= list:
        return "您传入的不是列表！"
    else:
        for i in num:
            if not isinstance(i,int):
                return "请全部传入整数！"
        return list(filter(lambda x:x%2==0,num))
result=get_num([1,5,9,3,2,5,4])
result:'''
print(code)
def get_num(num):
    if type(num)!= list:
        return '您传入的不是列表！'
    else:
        for i in num:
            if not isinstance(i,int):
                return '请全部传入整数！'
        return list(filter(lambda x:x%2==0,num))
print(get_num([1,5,9,3,2,5,4]))
print ('2. 定义一个方法get_page(url),url参数是需要获取网页内容的网址，返回网页的内容。提示（可以了解python的urllib模块）')
code='''code :
def get_page(url):
    response=urllib.request.urlopen(url)
    html=response.read()
    return html
print(get_page("http://wwww.baidu.com"))')'''
print(code)
def get_page(url):
    response=urllib.request.urlopen(url)
    html=response.read()
    return html
#print(get_page('http://wwww.baidu.com'))
print('定义一个方法 func，该func引入任意多的列表参数，返回所有列表中最大的那个元素')
code='''code 1):
def func(args):
    list=[]
    for x in args:
        if not isinstance(x,list):
            return "里面有至少一个非列表"
	    list.append(max(x))
    return max(list)
print(func([1,2],[33],[3,4,5,6],[7,7,8,9,8,9,8,3],[67,88]))
result:'''
print(code)
def func(*args):
    ls=[]
    for x in args:
        if not isinstance(x,list):
            return "里面有至少一个非列表"
        ls.append(max(x))
    return max(ls)
print(func([1,2],[33],[3,4,5,6],[7,7,8,9,8,9,8,3],[67,88]))
