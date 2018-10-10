#coding=utf-8
import os
currentPath=os.path.abspath('.')
print '1. 已知字符串 a = "abcd",用2个方法取出字母d'
a='abcd'
print 'code 1):a[3]'
print a[3]
print 'code 2):a[-1-0]'
print a[-1-0]
#####################################
print '2. a = "jay" b="python" 用字符串拼接的方法输出：my name is jay,i love python.'
a='jay'
b='python'
print 'code 1): "my name is "+a+",i love "+b'
print 'my name is '+a+',i love '+b
print 'code 2): "my name is %s,i love %s" % (a,b)'
## 第三个百分号不可省略
print 'my name is %s,i love %s' % (a,b)
#####################################
print '3. a = "pyer" b = "apple",用字典和format方法实现：my name is pyer, i love apple.'
a='pyer'
b='apple'
print 'code 1):my name is {},i love {} .formar (a,b)'
print 'my name is {},i love {}' .format (a,b)
print 'code 2):my name is {0},i love {1} .formar (a,b)'
print 'my name is {0},i love {1}' .format (a,b)
print 'code 3):my name is {param1},i love {param2} .format (param1=a,param2=b)'
print 'my name is {param1},i love {param2}' .format (param1=a,param2=b)
print 'code 4):my name is %(param1)s,i love %(param2)s % ("param1":a,"param2":b)'
print 'my name is %(param1)s,i love %(param2)s' % {"param1":a,"param2":b}
#####################################
print '4. 打开文件info.txt,并且写入500这个数字'
print """
    a=open(currentPath+'/info.txt','w')
    a.write('500')
    a.close()
    a=open(currentPath+'/info.txt','r')
    a.read(20)
    a.close()
    """
a=open(currentPath+'/info.txt','w')
a.write('500')
a.close()
a=open(currentPath+'/info.txt','r')
a.read(20)
a.close()
