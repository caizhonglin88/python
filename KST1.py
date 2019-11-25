# 5. 有一个文本文件“person.txt”，内容为:
# 编写代码读取文件中的内容，打印出如下结果，
# 张三的年龄为30
# 李四的年龄为20
# 并将该结果写入一个新的文件“detail.txt”
with open("stest2.txt",'r',encoding='utf-8') as f:
    datas=f.read()
print(datas)
with open('detail.txt','w',encoding='utf-8') as f:
    for date in datas[1:]:
        f.write('%s的年龄为%d' % (tuple(date.split(','))))
        f.flush()
        print(date)