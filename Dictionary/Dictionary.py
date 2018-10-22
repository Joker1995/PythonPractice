#encoding=utf-8
print '''
已知字典：ainfo = {'ab':'liming','ac':20}
完成下面的操作
1 使用2个方法，输出的结果：ainfo = {'ab':'liming','ac':20,'sex':'man','age':20}
'''
ainfo = {'ab':'liming','ac':20}
print 'code 1):ainfo["sex"]="man",ainfo["age"]=20'
ainfo['sex']='man'
ainfo['age']=20
print ainfo
ainfo.pop('sex')
ainfo.pop('age')
print '2 输出结果：["ab","ac"]'
print 'code :ainfo.keys()'
print ainfo.keys()
print '3 输出结果：["liming",20]'
print 'code :ainfo.values()'
print ainfo.values()
ainfo.update({"sex":"male"})
print '4 通过2个方法返回键名ab对应的值'
print 'code 1): print ainfo["sex"]'
print ainfo["sex"]
print 'code 2): print ainfo.get("sex")'
print ainfo.get("sex")
print '5 通过2个方法删除键名ac对应的值'
print 'before:'+str(ainfo)
print 'code 1):ainfo.pop("sex")'
ainfo.pop("sex")
print 'after:'+str(ainfo)
ainfo.update({"sex":"male"})
print 'before:'+str(ainfo)
print 'code 2):del ainfo["sex"]'
del ainfo["sex"]
print 'after:'+str(ainfo)
