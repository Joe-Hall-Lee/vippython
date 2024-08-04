'''流程控制语句 break 与 continue 在二重循环中的使用'''
for i in range(5):  # 代表外层循环要执行 5 次
    for j in range(1, 11):
        if j % 2 == 0:
            # break
            continue
        print(j, end='\t')
    print()
