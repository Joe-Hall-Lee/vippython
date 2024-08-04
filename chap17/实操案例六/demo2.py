lst = []
for i in range(0, 5):
    goods = input('请输入食物编号和食物名称，每次只能输入一样食物：\n')
    lst.append(goods)
for item in lst:
    print(item)

cart = []
while True:
    num = input('请输入开学之后想吃（喝）的食物编号：')
    for item in lst:
        if item.find(num) != -1:
            cart.append(item)
            break  # 退出 for
    if num == 'q':
        break  # 退出 while 循环
print('您的食物清单为：')
'''
for m in cart:
    print(m)
'''
for i in range(len(cart) - 1, -1, -1):
    print(cart[i])
