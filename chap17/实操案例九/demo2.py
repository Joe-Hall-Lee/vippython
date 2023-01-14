def show(lst):
    for item in lst:
        for i in item:
            print(i, end='   ')
        print()


lst = [['01', '水浒全传(SK)', ' 25', '   500000'],
       ['02', '三国前传(SK)', ' 30', '   411000'],
       ['03', '三国正传(SK)', ' 46', '   51312']]
print('编号\t\t书名\t\t  章节数\t\t播放量')
show(lst)
print('------------------格式化-------------------------------')
print('编号\t\t书名\t\t  章节数\t\t播放量')
for item in lst:
    item[0] = '000'+item[0]
    item[3] = '🎖️{:.2f}'.format(int(item[3]))
show(lst)
'''    for item in lst:
        for i in item:
            print(i,end='   ')      print()
'''
