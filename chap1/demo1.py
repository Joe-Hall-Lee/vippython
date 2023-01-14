# 可以输出数字
print(520)
print(98.5)

# 可以输出字符串
print('helloworld')
print("helloworld")

# 带有运算符的表达式
print(3+1)

# 将数据输出文件中，注意点，1.指定的盘符要存在.2.要用file=
fp = open('D:/text.txt', 'a+')  # a+如果文件不存在就创建，存在就在文件后面的内容继续追加
print('helloworld', file=fp)
fp.close()

# 不进行换行输出（输出内容在一行当中）
print('hello', 'world', 'Python')
