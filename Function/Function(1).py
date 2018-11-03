#encoding=utf-8
import sys
import os
import glob
print '''1 写一个函数代码，返回这3个数字中最大的一个。
a = 123
b = 345
c = 444'''
print '''code :
def max(*array):
    max=array[0]
    for x in array:
        if x>max:
            max=x
    return max
a=123
b=345
c=444
max=max(a,b,c)
print max
result:'''
def max(*array):
    max=array[0]
    for x in array:
        if x>max:
            max=x
    return max
a=123
b=345
c=444
max=max(a,b,c)
print max
print '''2 分别写2个函数，完成下面的功能：
2.1 调用函数：ainfo(x=88,y=22,z=44) 你定义ainfo函数体里面的内容并且返回结果：
[22, 44, 88]
code :
def ainfo(**tuple):
    return tuple.values()
ainfo(x=88,y=22,z=44)
result:'''
def ainfo(**tuple):
    return tuple.values()
list=ainfo(x=88,y=22,z=44)
print list
print '''2.2 调用函数：cinfo(x=88,y=22,z=44) 你定义cinfo函数体里面的内容并且返回结果：
('xaay','yaay','zaay')
code :
def cinfo(**tuple):
    list=tuple.keys()
    result=[]
    for x in list:
        result.append(x+'aay')
    return result
list=cinfo(x=88,y=22,z=44)
result:'''
def cinfo(**tuple):
    list=tuple.keys()
    result=[]
    for x in list:
        result.append(x+'aay')
    result.sort()
    return result
list=cinfo(x=88,y=22,z=44)
print list
print '''3. 定义一个方法 func，该func可以引入任意多的整型参数，结果返回其中最大与最小的值
code :
def maxAndMin(*array):
    for x in array:
        if isinstance(x,int):
            pass
        else:
            return "输入的参数必须为整型"
    a=sorted(array)
    max=a[-1]
    min=a[0]
    return {'max':max,'min':min}
result=maxAndMin(4,5,2,1,6,7,8,5)
result:'''
def maxAndMin(*array):
    for x in array:
        if isinstance(x,int):
            pass
        else:
            return "输入的参数必须为整型"
    a=sorted(array)
    max=a[-1]
    min=a[0]
    return {'max':max,'min':min}
result=maxAndMin(4,5,2,1,6,7,8,5)
print result
print '''4. 定义一个方法func，该func可以引入任意多的字符串参数，结果返回（长度）最长的字符串
code :
def maxLength(*array):
    for x in array:
        if not isinstance(x,str):
            return "输入的参数必须为字符串"
    a=sorted(array,key =lambda k:len(k))
    return a[-1]
result=maxLength('123','3453','33333','12')
result:'''
def maxLength(*array):
    for x in array:
        if not isinstance(x,str):
            return "输入的参数必须为字符串"
    a=sorted(array,key =lambda k:len(k))
    return a[-1]
result=maxLength('123','3453','33333','12')
print result
print '''5. 定义一个方法get_doc(module)，module参数为该脚本中导入或定义的模块对象，该函数返回module的帮助文档
code 1):
def get_doc(module):
    __import__(module)
    my_module=sys.modules[module]
    doc=my_module.__doc__
    return doc
doc=get_doc('os')
result:'''
def get_doc(module):
    __import__(module)
    my_module=sys.modules[module]
    doc=my_module.__doc__
    return doc
doc=get_doc('os')
print doc
print '''code 2):
def get_doc(module):
    exec "import %s" %module
    doc=module+".__doc__"
    exec "print %s"%doc
doc=get_doc('os')
'''
def get_doc(module):
    exec "import %s" %module
    doc=module+".__doc__"
    exec "print %s" %doc
get_doc('os')
print '''6. 定义一个方法get_text(f),f参数为任意一个文件的磁盘路径，该函数返回f文件的内容
code :
def get_text(f):
    if os.path.exists(f):
        with open(f,'r') as g:
            return g.read()
    return "file isn't exists"
doc_str=get_text('/home/joker/code/python/FoundationTypes/info.txt')
result:'''
def get_text(f):
    if os.path.exists(f):
        with open(f,'r') as g:
            return g.read()
    return "file isn't exists"
doc_str=get_text('/home/joker/code/python/FoundationTypes/info.txt')
print doc_str
print '''定义一个方法get_dir(folder),folder参数为任意一个文件夹，该函数返回folder文件夹的文件列表
code :
def get_dir(folder):
    for x in glob.glob(folder+'\*'):
        print x
get_dir('/home/joker/code/python')
result:'''
def get_dir(folder):
    for x in glob.glob(folder+'/*'):
        print x
get_dir('/home/joker/code/python')
