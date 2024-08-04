x = 97  # 代表的是 a 的 ASCⅡ 值
for _ in range(1, 27):
    print(chr(x), '--->', x)
    x += 1

print('-------------------------------------')
x = 97
while x < 123:
    print(chr(x), '--->', x)
    x += 1
