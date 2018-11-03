#encoding=utf-8
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
