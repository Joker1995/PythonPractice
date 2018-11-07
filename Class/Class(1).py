#encodig=utf-8
print('''1. 定义一个列表的操作类：Listinfo
包括的方法:
1 列表元素添加: add_key(keyname)  [keyname:字符串或者整数类型]
2 列表元素取值：get_key(num) [num:整数类型]
3 列表合并：update_list(list)	  [list:列表类型]
4 删除并且返回最后一个元素：del_key()

list_info = Listinfo([44,222,111,333,454,'sss','333'])
code :
class Listinfo(object):
    def __init__(self,list=None):
        self.list=list
    def add_key(self,keyname):
        self.list.append(keyname)
    def get_key(self,num):
        return self.list.__getitem__(num)
    def update_list(self,list):
        self.list.extend(list)
    def del_key(self):
        return self.list.pop()
list_info = Listinfo([44,222,111,333,454,'sss','333'])
list_info.add_key('666')
print(list_info.list)
print(list_info.get_key(0))
list_info.update_list(['7777',999])
print(list_info.list)
print(list_info.del_key())
result:''')
class Listinfo(object):
    def __init__(self,list=None):
        self.list=list
    def add_key(self,keyname):
        self.list.append(keyname)
    def get_key(self,num):
        return self.list.__getitem__(num)
    def update_list(self,list):
        self.list.extend(list)
    def del_key(self):
        return self.list.pop()
list_info = Listinfo([44,222,111,333,454,'sss','333'])
list_info.add_key('666')
print(list_info.list)
print(list_info.get_key(0))
list_info.update_list(['7777',999])
print(list_info.list)
print(list_info.del_key())
print('''定义一个集合的操作类：Setinfo
包括的方法:
1 集合元素添加: add_setinfo(keyname)  [keyname:字符串或者整数类型]
2 集合的交集：get_intersection(unioninfo) [unioninfo :集合类型]
3 集合的并集： get_union(unioninfo)[unioninfo :集合类型]
4 集合的差集：del_difference(unioninfo) [unioninfo :集合类型]

set_info =  Setinfo(你要操作的集合)
code :
class Setinfo(object):
    def __init__(self,list=None):
        self.set=set(list)
    def add_setinfo(self,keyname):
        self.set.add(keyname)
    def get_intersection(self,unioninfo):
        return self.set & unioninfo
    def get_union(self,unioninfo):
        return self.set | unioninfo
    def del_difference(self,unioninfo):
        return self.set - unioninfo
set_info =  Setinfo('abcd')
set_info.add_setinfo('23')
print(set_info.set)
print(set_info.get_intersection(set('ace')))
print(set_info.get_union(set('ace')))
print(set_info.del_difference(set('ace')))
result :''')
class Setinfo(object):
    def __init__(self,list=None):
        self.set=set(list)
    def add_setinfo(self,keyname):
        self.set.add(keyname)
    def get_intersection(self,unioninfo):
        return self.set & unioninfo
    def get_union(self,unioninfo):
        return self.set | unioninfo
    def del_difference(self,unioninfo):
        return self.set - unioninfo
set_info =  Setinfo('abcd')
set_info.add_setinfo('23')
print(set_info.set)
print(set_info.get_intersection(set('ace')))
print(set_info.get_union(set('ace')))
print(set_info.del_difference(set('ace')))
