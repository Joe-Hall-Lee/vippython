'''
要求输出 1 到 50 之间所有 5 的倍数：5, 10, 15, 20, 25, ...
5 的倍数的共同点：和 5 的余数为 0 的数都是 5 的倍数
什么样的数不是 5 的倍数：1, 2, 3, 4, 6, 7, 8, 9, ... 与 5 的倍数不为 0 的数不是 5 的倍数
要求使用 continue 实现
'''

for item in range(1, 51):
    if item % 5 == 0:
        print(item)

print('-----------使用continue-------------')
for item in range(1, 51):
    if item % 5 != 0:
        continue
    print(item)
