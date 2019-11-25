# 自定义一个list,按相反的顺序输出列表的值 （不能使用reverse()方法）
lst=[1,2,3,4,5,6,7,8,9]
# list.reverse(lst)
# print(lst)

for i in range(len(lst)//2):  #把列表中的元素化成相等的两部分；开始循环
    lst[i],lst[len(lst)-1-i]=lst[len(lst)-1-i],lst[i]  #根据元素的索引开始交换

# lst[0],lst[8]=lst[8],lst[0]

print(lst)