try:
    score = int(input('请输入分数:'))
    if 0 <= score <= 100:
        print('分数为：', score)
except ValueError as e:
    print(e)
