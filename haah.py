# str=("q12345abadsuq")
# print(len(str))#长度返回13个
# print(str.count("a"))#查询字符串中a的个数返回3个，
# print(str.startswith("q"))#查询字符串以什么开头，此处输入q返回真（true）
# print(str.endswith("a"))#查询字符串以什么结尾，此处输入a返回真(true)否则返回假flase
# print(str.find("p"))#查询字符串中ab排在第几位,此处返回6,如果不在其中返回-1
# print(str.strip("q"))#删除字符串两头相同的字符，如没有则只删除一个，此处结果为12345abadsu
# print(str.replace("123","789"))#将字符串中的123换成789，返回q78945abadsuq
# print(str.join("heh"))#已指定的字符串heh做为分隔符截取字符串并生成一个新的字符串，
# 返回hq12345abadsuqeq12345abadsuqh
#str.lstrip()截掉字符串左边的空格
#str.rstrip()删除字符串末尾的空格
#str.index()  此方法更find一样只不过字符串不

# lst=[]   #创建一个空列表
# lst=[10,11,12,13,14,'haha','hello']
# print(lst)  创建一个多元素列表

lst1=[1,2,3,4,5]
# lst2=['haha','red','green']
# lst3=lst1+lst2
# print(lst3)  #两个列表相加，返回一个新的列表[1, 2, 3, 4, 5, 'haha', 'red', 'green']

# lst=[12,34,56,[1,2,3]]
# print(lst)  #二维数组列表

 #list的基本操作，切片，索引从左往右，从0开始数起，负向从右往左从-1开始数起
# lst=[10,11,12,13,14,'haha','hello']
#
# print(lst[:]) #原样输出列表，返回[10, 11, 12, 13, 14, 'haha', 'hello']
#
# print(lst[3:])  #取出索引从3开始后面所有的值，返回[13, 14, 'haha', 'hello']
#
# print(lst[1])  #取出列表lst中索引为1的元素，返回11


# lst6=[12,34,56,[1,2,3]]
# print(lst6[3][1])  #取出列表lst6里面索引为3的元素，在取出这个元素中索引为1的元素，结果为2
# lst=[10,11,12,13,14,'haha','hello']
# print(lst[-3:-1])  #取出索引-3到-1的之间元素，返回结果为[14, 'haha']
# print(lst[:2])  #取出索引2前面所有的元素，返回结果[10, 11]

#列表常用方法
# lst=[10,11,12,13,14,'haha','hello']
# print(len(lst)) #查询lst列表内所有的元素个数，返回为7

# lst=[10,11,12,13,14,'haha','hello',14]
# lst.append('hehe')
# print(lst)  #在列表lst末尾 追加新的元素‘hehe’,
    # 返回[10, 11, 12, 13, 14, 'haha', 'hello', 'hehe']，还可以两个列表相加lst.append(['xxx':'xxx'])
# print(lst.count(14))  #查询列表lst中元素14出现的次数，返回为2次

lst=[10,11,12,13,14,'haha','hello',14]
lst.extend([1,2,3])
print(lst) #在列表lst末尾一次性追加一个序列seq，返回[10, 11, 12, 13, 14, 'haha', 'hello', 14, 1, 2, 3]

#lst1=[1,2,3,4,5]
# print(max(lst1))
# print(min(lst1))  #查询列表lst1里面的最大和最小值，返回最大5，最小1，只能对数值做操作

