#encoding=utf-8
print('''1. 用lambda和filter完成下面功能：输出一个列表，列表里面包括：1-100内的所有偶数。（提示：可以用filter,lambda）
code:
def getNum():
    return filter(lambda x:x%2==0,range(1,100))
list=list(getNum())
result:''')
def getNum():
    return filter(lambda x:x%2==0,range(1,100))
list=list(getNum())
print(list)
print('''2. 用位置匹配，关键字匹配，收集匹配(元组收集,字典收集)分别写4个函数，完成功能:
传递3个列表参数：
[1,2,3],[1,5,65],[33,445,22]
返回这3个列表中元素最大的那个，结果是：445
code 1):
def get_max(list1,list2,list3):
    return max(list1+list2+list3)
result:''')
def get_max(list1,list2,list3):
    return max(list1+list2+list3)
print(get_max([1,2,3],[1,5,65],[33,445,22]))
print('''code 2):
def get_max2(list=[],list2=[],list3=[]):
    c=list+list2+list3
    return max(c)
result:''')
def get_max1(list=[],list2=[],list3=[]):
    c=list+list2+list3
    return max(c)
print(get_max1([1,2,3],[1,5,65],[33,445,22]))
print('''code 3):
def get_max2(*list):
    a=[]
    for x in list:
        a.extend(x)
    return max(a)
result:''')
def get_max2(*list):
    a=[]
    for x in list:
        a.extend(x)
    return max(a)
print(get_max2([1,2,3],[1,5,65],[33,445,22]))
print('''code 4):
def get_max3(**list):
    a=[]
    for x in list:
        a.extend(list[x])
    return max(a)
result:''')
def get_max3(**list):
    a=[]
    for x in list:
        a.extend(list[x])
    return max(a)
print(get_max3(list1=[1,2,3],list2=[1,5,65],list3=[33,445,22]))
print('''3. 定义一个func(name)，该函数效果如下。
assert func("lilei") = "Lilei"
assert func("hanmeimei") = "Hanmeimei"
assert func("Hanmeimei") = "Hanmeimei"
code 1):
def func(str):
    return str[0].upper()+str[1:]
print(func("lilei"))
code 2):
def capstr(str):
    return str.capitalize()
result:''')
def func(str):
    return str[0].upper()+str[1:]
print(func("lilei"))
def capstr(str):
    return str.capitalize()
print(capstr("lilei"))
print('''4. 定义一个func(name,callback=None),效果如下。
assert func("lilei") == "Lilei"
assert func("LILEI",callback=string.lower) == "lilei"
assert func("lilei",callback=string.upper) == "LILEI"
code :
def fun1(str,callback=None):
    if callback == None:
        return str.capitalize()
    else:
        return callback(str)
print(fun1('lilei'))
print(fun1('lilei',callback=string.lower))
result:''')
def fun1(str,callback=None):
    if callback == None:
        return str.capitalize()
    elif callback == 'string.lower':
        return str.lower()
    elif callback == 'string.upper':
        return str.upper()
print(fun1('lilei'))
print(fun1('lilei',callback='string.upper'))
print('''5. 定义一个func(*kargs),效果如下。
l = func(1,2,3,4,5)
for i in l:
	print i,
#输出 1 2 3 4 5
l = func(5,3,4,5,6)
for i in l:
	print i
#输出 5 3 4 5 6
code:
def getitem(*kargs):
    return kargs
result:''')
def getitem(*kargs):
    return kargs
print(getitem(5,3,4,5,6))
print('''6. 定义一个func(name=None,**kargs),该函数效果如下:
assert func(“lilei”) == "lilei"
assert func("lilei",years=4) == "lilei,years:4"
assert func("lilei",years=10,body_weight=20) == "lilei,years:4,body_weight:20"
code :
def getDetail(name=None,**args):
    data=[]
    for x,y in args.items():
        data.extend([',',str(x),':',str(y)])
    info=''.join(data)
    return '%s%s' % (name,info)
print(getDetail("lilei",years=10,body_weight=20))
result:''')
def getDetail(name=None,**args):
    data=[]
    for x,y in args.items():
        data.extend([',',str(x),':',str(y)])
    info=''.join(data)
    return '%s%s' % (name,info)
print(getDetail("lilei",years=10,body_weight=20))
print('''7. 定义一个func(*kargs)，该函数效果如下。
assert func(222,1111,'xixi','hahahah') == "xixi"
assert func(7,'name','dasere') == 'name'
assert func(1,2,3,4) == None
code:
def shortstr(*kargs):
    #过滤非字符串
    list=[]
    for x in kargs:
        if isinstance(x,str):
            list.append(x)
    #收集长度
    len_lis = [len(x) for x in list]
    if len_lis:
    		min_index = min(len_lis)
    		return list[len_lis.index(min_index)]
    return None
print(shortstr(222,1111,'xixi','hahahah'))
result:''')
def shortstr(*kargs):
    #过滤非字符串
    list=[]
    for x in kargs:
        if isinstance(x,str):
            list.append(x)
    #收集长度
    len_lis = [len(x) for x in list]
    if len_lis:
    		min_index = min(len_lis)
    		return list[len_lis.index(min_index)]
    return None
print(shortstr(222,1111,'xixi','hahahah'))
