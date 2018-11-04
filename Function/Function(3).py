#encoding=utf-8
print('''1. 定义一个方法get_fundoc(func),func参数为任意一个函数对象，返回该函数对象的描述文档，如果该函数没有描述文档，则返回"not found"
code :
def get_fundoc(func):
    if not callable(func):
        return "func 参数不是函数对象"
    elif str(type(func)) == "<type 'classobj'>" or str(type(func)) == "<type 'module'>":
         return "func 参数不是函数对象"
    else:
        if func.__doc__==None:
            return "no found"
        else:
            return func.__doc__
print(get_fundoc(sorted))
result:''')
def get_fundoc(func):
    if not callable(func):
        return "func 参数不是函数对象"
    elif str(type(func)) == "<type 'classobj'>" or str(type(func)) == "<type 'module'>":
         return "func 参数不是函数对象"
    else:
        if func.__doc__==None:
            return "no found"
        else:
            return func.__doc__
print(get_fundoc(sorted))
print('''2. 定义一个方法get_cjsum(),求1-100范围内的所有整数的平方和。返回结果为整数类型
code:
def get_cjsum():
    count=0
    for x in range(1,100):
        count+=x*x
    return count
print(get_cjsum())
result:''')
def get_cjsum():
    count=0
    for x in range(1,100):
        count+=x*x
    return count
print(get_cjsum())
print('''定义一个方法list_info(list), 参数list为列表对象，怎么保证在函数里对列表list进行一些相关的操作，不会影响到原来列表的元素值，比如：
a = [1,2,3]
def list_info(list):
   '要对list进行相关操作，不能直接只写一句return[1,2,5]，这样就没意义了'
print list_info(a):返回结果：[1,2,5]
print a 输出结果：[1,2,3]
写出函数体内的操作代码。
code:
def list_info(list):
    list=a[:]
    list[-1]=5
    return list
print('result array:'+list_info(a))
print('source array:'+a)
result:''')
a = [1,2,3]
def list_info(list):
    list=a[:]
    list[-1]=5
    return list
print('result array:'+str(list_info(a)))
print('source array:'+str(a))
print('''定义一个方法get_funcname(func),func参数为任意一个函数对象，需要判断函数是否可以调用，如果可以调用则返回该函数名(
类型为str)，否则返回 “fun is not function"
code:
def get_funcname(func):
    if not callable(func):
        result "fun is not function"
    else:
        if "func_name" in dir(func):
            print(func.func_name)
        elif str(type(func))=="<type 'classobj'>" or str(type(func))=="<type 'modules'>":
            result "fun is not function"
        else:
            return "fun is not function"
print(get_funcname(max))
result:''')
def get_funcname(func):
    if not callable(func):
        return "fun is not function"
    else:
        if "__name__" in dir(func):
            return func.__name__
        elif str(type(func))=="<type 'classobj'>" or str(type(func))=="<type 'modules'>":
            return "fun is not function"
        else:
            return "fun is not function"
print(get_funcname(list_info))
