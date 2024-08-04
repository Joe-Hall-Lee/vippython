for item in 'Python':  # 第一次取出来的是 P，将 P 赋值给 item，将 item 的值输出
    print(item)

# range() 产生一个整数序列-->也是一个可迭代对象
for i in range(10):
    print(i)

# 如果在循环体中不需要使用自定义变量，可将自定义变量写为“_”
for _ in range(5):
    print('人生苦短，我用 Python')

print('使用 for 循环，计算 1 到 100 之间的偶数和')

sum = 0  # 用于存储偶数和
for item in range(1, 101):
    if item % 2 == 0:
        sum += item

print('1 到 100 之间的偶数和为:', sum)
