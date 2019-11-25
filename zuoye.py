# print('heheh word')
# print('蔡小敏''18岁')
# print('100+100=',100+100)
# print(100+100+100-100)

# name=input("请输入名字：")
# print(name)

# a = 'cai'
# type(a)
# print(type(a))

# # a=100
# # b='haha'
# x,y,z=1,2,'woshixiaoming'
# print(x,y,z)

# a='100'
# print(int(a)+10)
# a=10  #定a b 两个变量
# b=21
# print(a+b) #输出a+b的和
# print(b-a,a+b)  #同时输出差与和
# print(a*b)    #输出两数相乘的结果
# print(b/a)   #除法
# print(a//b)   #除法 取其整数部分
# print(b%a)   #除法   取其余数部分
# print(a**b)    #多少次方   此题就是10的21次方。

# print('我是一个学生 \n今年30岁了\n很爱看书')
# print('我是一个学生 ，今年30岁了， 很爱看书\
# hjjjk')

# a=[1,2,'sc']
# print('这个列表是 %s' % a)

# a,b=1,'caicai'
# print('%d是一个数字\n%s是一个字符串' % (a,b))
# print('%d是一个数字,%s是一个字符串' % (a,b))


# 字符串的操作
# a='wahaha'
# b='haohe'
# lst=[1,2,3,4,5,'wo',[7,8],9]
# print(a+b)
# print(a*3,b*2)
# print(a,b)
# print(a[1:4],b[3])
# print("wa" not in a)
# print(len(a))
# print(len(lst))
# print(lst[6][1])

# # print(a.count('a'))   #查询某字符在字符串中出现的次数
# print(a.startswith('wa'))  #查询是否以某字符串开头
# a='wahaha'
# b='haohe'
# print(b.endswith('he')) #查询是否以某字符串结尾,返回真True和假False
# print(b.find('haha'))
# print(b.index('he'))     #查询某字符是否在字符串中,返回开始索引，没有就返回-1

# print(a.rfind('haha'))
# print(b.rindex('he'))   #加上‘r’基本同理，只是从右边开始查找，默认的一般从左往右
#
# print(a.replace('wahaha','chihuo'))#替换字符命令
# print(a.join('ha'))
# print(b.split('o'))

# lst=[1,2,3,4,5,'wo',[7,8],9]

# A=['h','a','b']
# B=[1,2,3,[5,6]]
# C=A+B
# a=lst[5]
# lst[6]='shi'#替换列表中的元素
# print(lst)

# 1)已知x =3, 那么执行x+=6之后，x的值为？
# x=3
# x=x+6
# print(x)
# 2)[3] in [1,2,3,4]
# print([3]in [1,2,3,4])

# 3)任意长度的列表、元组、字符串的最后 一个元素下标为？
# 4)list(range(1,10,5))值？
# print(list(range(1,10,5)))
# 5)d = {'a': 1, 'b': 2}, d.setdefault('x','yes')
# d = {'a': 1, 'b': 2}
# (d.setdefault('x','yes'))
# print(d)
# 6)求li = [3,6,9,11,15] 的长度
# li = [3,6,9,11,15]
# print(len(li))    #5
# 7)字典对象中返回字典中“键”列表的方法是？#dict keys()
# 8)1<2<3结果
# print(1<2<3)
# 9)li = [3,5,7], li.append([1,2])
# li = [3,5,7]
# (li.append([1,2]))
# print(li)
# 10)无穷循环while True:的循环体中可用什么语句退出循环？#break
# def fun(number):
#     number = number//100
#     if number == 0:
#             return
#     print(number)
# fun(100)
#结果是543